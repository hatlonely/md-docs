# python3 exec 执行 python 代码

[//]: <> (python3, exec)

动态执行 python 表达式获取结果，可以使用 eval 实现，但是 eval 只能执行表达式。
要执行 python 代码，可以通过 eval + lambda 表达式实现，但是 lambda 表达式只支持单行。
如果要执行多行代码，则只能使用 exec 实现。exec 是用来执行 python 代码的，没有返回值，
但是可以讲其执行的结果变量中获取执行中产生的变量，exec 所需要捕获的变量，也需要通过环境参数传递进去

```python
def exec_with_res(code, val=None, case=None, step=None, var=None, x=None):
    loc = {}
    env = globals()
    env.update(val=val)
    env.update(case=case)
    env.update(step=step)
    env.update(var=var)
    env.update(x=x)
    exec(code, env, loc)
    return loc["res"]
```

## 链接

- 获取 exec 返回值: <https://stackoverflow.com/questions/23917776/how-do-i-get-the-return-value-when-using-python-exec-on-the-code-object-of-a-fun>
