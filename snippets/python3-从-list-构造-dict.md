# python3 从 list 构造 dict

[//]: <> (python3, dict, list)

```
d = dict([("key1", "val1"), ("key2", "val2")])
```

阿里云表格存储 GetRow 接口返回的数据字段是数组格式，可以通过下面的代码快速转化成字典格式

```
dict([(i[0], i[1]) for i in row.attribute_columns])
```

## 链接

- python3 创建字典: <https://stackoverflow.com/questions/37715995/how-can-i-create-dictionary-in-python3>
