# golang 结构体默认值

[//]: <> (golang, 默认值)

## golang 的默认值

c 语言的结构体默认是无意义的数值，指针可能会指向任意内存，数值可能是任意一个值，不初始化的结构体经常会引发难以排查的 bug，
而 golang 的结构体默认都是零值，指针是 nil，数值都是 0，这样设计让结构体的值有了稳定的预期，减少了 bug。
但是零值还是无法满足所有场景，很多时候，我们希望结构体能有一个期望的初始值，一个典型的场景就是配置对象，比如下面这个 redis 的配置，
我们希望默认的配置是连本机的 redis，重试 3 次，超时间 300ms。

```golang
type RedisOptions struct {
	Addr       string
	Timeout    time.Duration
	MaxRetries int
}
```

显然这个结构体初始化之后都是 0 值，不能满足我们的需求，于是我们不得不在创建对象后再给对象赋值

```golang
var options RedisOptions
options.Addr = "127.0.0.1:6379"
options.Timeout = 300 * time.Milliseconds
options.MaxRetries = 3
```

又或者将要赋的值直接传给对象

```golang
options := &RedisOptions{
    Addr: "127.0.0.1:6379",
    Timeout: 300 * time.Milliseconds,
    MaxRetries: 3,
}
```

然后我们可以提供一个构造方法

```golang
func NewDefaultRedisOptions() *RedisOptions {
    return &RedisOptions{
        Addr: "127.0.0.1:6379",
        Timeout: 300 * time.Milliseconds,
        MaxRetries: 3,
    }
}
```

这个方案已经可以解决大部分问题了，就是每个结构都需要额外提供一个构造方法，还是有些繁琐

## 基于 tag 实现通用的 `SetDefaultValue`

这些 `NewDefaultXXX` 方法需要在代码中显式调用才能生效，假如我们要实现一个通用的将配置文件映射到结构体的功能，
并且要能够支持未配置的字段自动用默认值填充，如果使用上面这种方式，就需要提前知道每种结构的 `NewDefaultXXX`，
而作为一个通用的库肯定不可能依赖这些特定的结构，因此这种逻辑无法通过上面这种方案实现

为了实现这个需求，就必须要解除对 `NewDefaultXXX` 这类方法的依赖，其中一个思路就是用一个统一的方法 `SetDefaultValue` 去实现 `NewDefaultXXX`，
并且 `SetDefaultValue` 这个方法不能有不确定的参数，那么问题来了，默认值如何传递给 `SetDefaultValue` 方法呢，幸运的是，golang 中有一种 tag 语法，
可以在结构体字段的 tag 中增加默认值，就像这样

```golang
type RedisOptions struct {
	Addr        string        `dft:"127.0.0.1:6379"`
	Timeout     time.Duration `dft:"300ms"`
	MaxRetries  int           `dft:"3"`
}
```

`SetDefaultValue` 的实现就是从 tag 中获取默认值，在设置到对应的字段

```golang
func SetDefaultValue(v interface{}) error {
	if reflect.TypeOf(v).Kind() != reflect.Ptr || reflect.TypeOf(v).Elem().Kind() != reflect.Struct {
		return errors.Errorf("expect a struct point. got [%v]", reflect.TypeOf(v))
	}
	rt := reflect.TypeOf(v).Elem()
	rv := reflect.ValueOf(v).Elem()
	for i := 0; i < rv.NumField(); i++ {
		tag := rt.Field(i).Tag.Get("dft")
		if !rv.Field(i).CanSet() {
			continue
		}
		if rt.Field(i).Type.Kind() == reflect.Struct && rt.Field(i).Type != reflect.TypeOf(time.Time{}) && rt.Field(i).Type != reflect.TypeOf(regexp.Regexp{}) {
			if err := SetDefaultValue(rv.Field(i).Addr().Interface()); err != nil {
				return errors.WithMessage(err, "SetDefaultValue failed")
			}
			continue
		}
		if tag == "" {
			continue
		}
		if err := cast.SetInterface(rv.Field(i).Addr().Interface(), tag); err != nil {
			return errors.WithMessage(err, "SetInterface failed")
		}
	}

	return nil
}
```

现在对于任意一个结构体，我们都可以通过下面的调用获得一个默认的对象

```golang
var options RedisOpitons
SetDefaultValue(&options)
```

在结构体嵌套的场景下里面同样可以工作。下面的代码中，Redis 这个成员会被递归地赋值成默认值

```golang
type Options struct {
    Redis RedisOptions
    Mysql MysqlOptions
}

var options Options
SetDefaultValue(&options)
```

## `SetDefaultValueCopy` 对象复用

上面的实现在使用上很方便，但是每次调用都需要去解析 tag，从 tag 获取默认值，再赋值给结构体，这个过程反复利用反射机制，
还涉及到字符串转换成对应类型，对于构造对象来说，都是非常复杂耗时的操作，幸运的是，在配置文件这个场景下，这点性能损耗是可以接受的。

但这个问题同样也是可以优化的，理想情况下，如果已经存在一个默认对象，新对象只需要拷贝默认对象就可以了，在这个思路下，
我们可以缓存之前 `SetDefaultValue` 的结果，在之后的调用中直接从这个缓存中拷贝就可以了

这里直接使用一个 `map` 作为缓存，同时加一个 `mutex` 保证协程安全

另外值得注意的是，这种拷贝是浅拷贝，如果结构体中包含指针，拷贝的只是指针，如果这个结构体是可变的，可能会出现不可预期的结果。
结构体中包含指针的场景，还是使用 `SetDefaultValue` 会更安全一些

```golang
var mutex sync.RWMutex
var defaultValueMap = map[reflect.Type]reflect.Value{}

func SetDefaultValueCopy(v interface{}) error {
	if reflect.ValueOf(v).IsNil() {
		return nil
	}

	rt := reflect.TypeOf(v)
	if rt.Kind() != reflect.Ptr || rt.Elem().Kind() != reflect.Struct {
		return errors.Errorf("expect a struct point. got [%v]", rt)
	}

	mutex.RLock()
	if rv, ok := defaultValueMap[rt]; ok {
		mutex.RUnlock()
		reflect.ValueOf(v).Elem().Set(rv)
		return nil
	}
	mutex.RUnlock()

	if err := SetDefaultValue(v); err != nil {
		return err
	}

	nv := reflect.New(reflect.TypeOf(v).Elem())
	nv.Elem().Set(reflect.ValueOf(v).Elem())

	mutex.Lock()
	defaultValueMap[rt] = nv.Elem()
	mutex.Unlock()
	return nil
}
```

## 参考链接

- 源码地址: <https://github.com/hatlonely/go-kit/blob/master/refx/default.go>
