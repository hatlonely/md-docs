# python3 for else 预发

[//]: <> (python3, for, else, 循环)

重试逻辑里面，重试次数达到上限之后进行异常处理，一般的 for 循环需要增加一个 flag，看起来非常丑陋，for-else 语法可以非常优雅地解决这个问题

```python
for j in range(retry.attempts):
    res = ctx[step["ctx"]].do(req)
    step_result.res = res
    if retry.condition == "" or not expect_val(None, retry.condition, case=case_result, step=step_result, var=var):
        break
    time.sleep(retry.delay.total_seconds())
else:
    raise RetryError()
```

## 链接

- Why does python use else after for and while loops: <https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops>
