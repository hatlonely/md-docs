# python3 datetime timestamp 互转

[//]: <> (python3, datetime, timestamp)

datetime 转 timestamp

```python
from datetime import datetime

dt = datetime.now()
ts = datetime.timestamp(dt)
```

timestamp 转 datetime

```python
from datetime import datetime

ts = 1642343681
dt = datetime.fromtimestamp(ts)
```

## 链接

- timestamp datetime: <https://www.programiz.com/python-programming/datetime/timestamp-datetime>
