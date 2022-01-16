# python3 subprocess 执行 shell 命令

```python
import unittest

class TestSubprocess(unittest.TestCase):
    def test_bash(self):
        process = subprocess.run(["/bin/bash", "-c", "echo ${PATH}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(process.returncode, process.stdout, process.stderr)

    def test_python(self):
        process = subprocess.run(["python3", "-c", "print('hello world')"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(process.returncode, process.stdout, process.stderr)

if __name__ == '__main__':
    unittest.main()
```

## 链接

- subprocess: <https://docs.python.org/3/library/subprocess.html>
