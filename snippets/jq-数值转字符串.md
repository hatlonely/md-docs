# jq 数值转字符串

[//]: <> (shell, jq, linux)

```shell
jq -r '(.assertionSucc|tostring) + "/" + ((.assertionFail + .assertionSucc)|tostring)' test_result.json

# 输出: 2/2
```

不加括号有问题，可能和运算符优先级有关系

## 链接

- how do i use jq to convert number to string: <https://stackoverflow.com/questions/35365769/how-do-i-use-jq-to-convert-number-to-string>
