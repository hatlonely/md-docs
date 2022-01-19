# python3 解析 golang duration 字符串

[//]: <> (python3, golang, duration, pyduration)

durationpy 库可以解决这个问题

```shell
pip3 install durationpy
```

```python
import durationpy

td = durationpy.from_str("4h3m2s1ms")
durationpy.to_str(td)
```

## 链接

- duration py: <https://github.com/icholy/durationpy>
