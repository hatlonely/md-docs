# python3 datetime 日期计算

[//]: <> (python3, datetime, 日期计算)

```python
from datetime import datetime, timedelta

d1 = datetime.now()
d2 = datetime.now() + timedelta(seconds=5)
delta = d2 - d1

print(delta.total_seconds())
```

## 链接

- substract tow datetime: <https://stackoverflow.com/questions/32211596/subtract-two-datetime-objects-python>
