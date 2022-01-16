# python3 终端颜色显示

[//]: <> (python3, colorama, 颜色)


正在用 python 作一个工具，其中有个功能需要用红色字体显示错误信息，绿色字体显示正常信息，colorama 库可以满足这个需求

使用如下命令安装

```
pip3 install colorama
```

```
from colorama import Fore, Back, Style

# 红色字体显示
print(Fore.RED + "some red text" + Fore.RESET)

# 绿色字体显示
print(Fore.GREEN + "some green text" + Fore.RESET)

# 绿色背景显示
print(Back.GREEN + "some text" + Back.RESET)
```

## 链接

- colorama: <https://pypi.org/project/colorama/>
