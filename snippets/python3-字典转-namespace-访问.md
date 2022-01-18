# python3 字典转 namespace 访问

[//]: <> (python3, dict, SimpleNamespace)

使用 `SimpleNamespace` 库可以实现这个需求

```python
from types import SimpleNamespace

d = {'key1': 'value1', 'key2': 'value2', 'key3': {'key4': 'value5', 'key5': 5, 'key6': ['value61', 'value62'], 'key7': [{'key8': 'value8'}]}}
n = SimpleNamespace(**d)

# namespace(key1='value1', key2='value2', key3={'key4': 'value5', 'key5': 5, 'key6': ['value61', 'value62'], 'key7': [{'key8': 'value8'}]})
```

上面的代码只能将字典的第一层 key 转成 namespace 访问方式，如果需要递归，可以借住 `json` 的 `object_hook` 来实现（咋想到的😂）

```python
import json
from types import SimpleNamespace

def dict_to_sns(d):
    return SimpleNamespace(**d)

d = {'key1': 'value1', 'key2': 'value2', 'key3': {'key4': 'value5', 'key5': 5, 'key6': ['value61', 'value62'], 'key7': [{'key8': 'value8'}]}}
n = json.loads(json.dumps(d), object_hook=dict_to_sns)

# namespace(key1='value1', key2='value2', key3=namespace(key4='value5', key5=5, key6=['value61', 'value62'], key7=[namespace(key8='value8')]))
```

## 链接

- How to use dot notation for dict in python: <https://stackoverflow.com/questions/16279212/how-to-use-dot-notation-for-dict-in-python>
- Creating a namespace with a dict of dicts: <https://stackoverflow.com/questions/50490856/creating-a-namespace-with-a-dict-of-dicts>
