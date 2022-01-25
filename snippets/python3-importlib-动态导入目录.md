# python3 importlib 动态导入目录

[//]: <> (python3, importlib, import)

目录需要是一个包含 `__init__.py` 的 python 包

```python
# 当执行目录和脚本目录不在一个目录下时，需要将执行目录加入到系统包搜索路径
import sys
sys.path.append(".")

import importlib
module = importlib.import_module(filename.replace("/", "."), "custom")
print(module)
```

## 链接

- how to import the module: <https://programming.vip/docs/given-the-full-path-how-to-import-the-module.html>
