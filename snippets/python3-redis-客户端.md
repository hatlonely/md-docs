# python3 redis 客户端

[//]: <> (python3, redis, 数据库)

安装

```
pip3 install redis
```

代码样例

```python
import unittest
import redis


class TestRedis(unittest.TestCase):
    def setUp(self) -> None:
        self.client = redis.Redis(
            host='localhost',
            port=6379,
            db=0,
            password=None,
            decode_responses=True,
        )

    def test_set(self):
        ok = self.client.set("name", "hatlonely123")
        print(ok)

    def test_get(self):
        res = self.client.get("name")
        print(res)

    def test_hset(self):
        num = self.client.hset("key", "f1", "v1")
        print(num)

    def test_hget(self):
        res = self.client.hget("key", "f1")
        print(res)


if __name__ == '__main__':
    unittest.main()
```

## 连接

- redis: <https://github.com/redis/redis-py>
