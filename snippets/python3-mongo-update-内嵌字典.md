# python3 mongo update 内嵌字典

`pymongo` 的 `update_one` 接口只能支持最外层 key 的 update，不能递归嵌套 update

如下面的例子，整个 key3 都会直接被覆盖成新的值

```python
collection.insert_one({
    "key1": "value1",
    "key2": "value2",
    "key3": {
        "key4": "value5",
        "key5": 5,
        "key6": [
            "value61",
            "value62"
        ],
        "key7": [
            {
            "key8": "value8"
            }
        ]
    }
})

collection.update_one({"_id": ObjectId("61ef739496089fa658380996")}, {
    "$set": {
        "key3": {
            "key4": "newval",
        }
    }
})

collection.find_one(ObjectId("61ef739496089fa658380996"))

# {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": {
#         "key4": "newval"
#     }
# }
```

如果要设置内层的对象的值，需要指定 key 的路径

```python
collection.update_one({"_id": ObjectId("61ef739496089fa658380996")}, {
    "$set": {
        "key3.key4": "newval",
    }
})

# {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": {
#         "key4": "newval",
#         "key5": 5,
#         "key6": [
#             "value61",
#             "value62"
#         ],
#         "key7": [
#             {
#             "key8": "value8"
#             }
#         ]
#     }
# }
```

为了方便调用，可以做一个辅助函数，自动打平内嵌的字典

```python
def flat(d):
    res = {}
    _flat_recursive([], d, res)
    return res


def _flat_recursive(k, d, res):
    for key in d:
        if isinstance(d[key], dict):
            _flat_recursive(k + [key], d[key], res)
        else:
            res[".".join(k + [key])] = d[key]

collection.update_one({"_id": ObjectId("61ef739496089fa658380996")}, {
    "$set": flat({
        "key3": {
            "key4": "newval",
        })
    }
}
```
