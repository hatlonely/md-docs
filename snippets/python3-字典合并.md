# python3 字典合并

[//]: <> (python3, dict, 字典合并)

```
# python 3.9
d = d1 | d2

# python 3.5
d = {**d1, **d2}

# python 3.4 以下

def merge_two_dicts(x, y):
    z = x.copy()   # start with keys and values of x
    z.update(y)    # modifies z with keys and values of y
    return z

z = merge_two_dicts(x, y)
```

# 链接

- 字典合并: <https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-take-union-of-dictionari>
