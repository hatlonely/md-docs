# python3 生成器遍历多个 list

[//]: <> (python3, generator, list)

`itertools.chain` 就是这个场景

```python
import itertools

a = [5, 8, 9]
b = [6, 1, 0]

for x in itertools.chan(a,b):
    print(x)
```

## 链接

- How do I make a generator from two lists in python: <https://stackoverflow.com/questions/16346375/how-do-i-make-a-generator-from-two-lists-in-python>

