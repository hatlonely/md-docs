# python3 eval 传入额外的字典变量

[//]: <> (python3, eval)

`locals()` 中包含了当前的作用域的局部变量，通过 `update` 方法可以添加新的环境变量到当前作用域，这样 `eval` 就能访问到这些字典变量了

```python
def py_eval(rule, **kwargs):
    locals().update(**kwargs)
    return eval(rule)
```

## 链接

- Pass kwargs to dynamically instantiated Python Class: <https://stackoverflow.com/questions/11927936/pass-kwargs-to-dynamically-instantiated-python-class>
