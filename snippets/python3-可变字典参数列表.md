# python3 可变字典参数列表

[//]: <> (python3, kwargs)

`**kwargs` 参数是一个可变字典参数列表，`func` 可以接收任何字典参数，这些参数会被当成字典放入 `kwargs` 变量中

```python
def func(**kwargs):
    print(kwargs)
    for k in kwargs:
        print(k, "=>", kwargs[k])

func(a="hello", b="world")
```
