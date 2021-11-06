# linux 命令行工具 jq

## 简介

jq 是一个类似 sed 用来处理 JSON 数据的命令行工具，你可以用它对结构化数据进行分片，过滤，映射和转换，就像 sed/awk/grep 处理文本一样轻松； 
jq 使用可移植的 C 语言编写，而且没有任何运行时的依赖，你可以下载一个二进制，scp 到同一个类型的远程机器上，并且与其它能够工作； 
jq 可以轻而依据地将已有的数据格式转换成你期望的数据格式，而且这样的程序通常比你与其的更短、更简单。

## 安装

```
# Mac
brew install jq

# Centos
yum install jq
```

## 命令行参数

- `-c`: 输出到同一行
- `-r, --raw-output`: 输出原值数值（字符串去掉引号，utf8 字符逆转义）
- `--args <key> <val>`: 传入变量，过滤器中使用 `$key` 引用
- `--tab`: 使用 tab 来缩进，默认是两个空格
- `--indent <n>`: 缩进 n 个空格
- `-s, --sort-keys`: 输出的字段按 key 排序
- `-j, --join-output`: 在每个结果后面不输出空行
- `-f <filename>, --from-file <filename>`: 从文件中读去过滤器

## 样例参考

测试文件

``` shell
cat <<EOF > test.json
{"key1": "val11", "key2": 12, "key3": [1, 2, 3, 4], "key4.key5": "val14"}
{"key1": "val21", "key2": 22, "key3": [1, 2, 3, 4], "key4.key5": "val24"}
{"key1": "val31", "key2": 32, "key3": [1, 2, 3, 4], "key4.key5": "val34"}
{"key1": "val41", "key2": 42, "key3": [1, 2, 3, 4], "key4.key5": "val44"}
EOF
```

- `jq . test.json`: 格式化 `test.json`
- `cat test.json | jq .`: 格式化 `test.json`
- `jq '.key1' <<< "$(cat test.json)"`: 格式化 shell 变量
- `cat test.json | jq -c .`: 格式化并输出在同一行 `test.json`
- `cat test.json | jq '.key1'`: 按路径取值
- `cat test.json | jq -r '.key1'`: 按路径去原始值（如果是字符串去掉引号）
- `cat test.json | jq '.key3[0]'`: 按路径取值
- `cat test.json | jq '.["key4.key5"]'`: 按路径取值
- `cat test.json | jq -c '[.key1, .key2]'`: 重组
- `cat test.json | jq -c '{a: .key1, b: .key2}'`: 重组
- `cat test.json | jq -c '. | select(.key1 == "val21" and .key2 >= 11)'`: 过滤
- `cat test.json | jq -c ". | select(.key1 == \"val21\" and .key2 >= 11)"`: 过滤
- `cat test.json | jq -c ". | select(.key3 != null) | .key3"`: 过滤空值
- `cat test.json | jq -c ". | select(.key1 == \"val21\" and .key2 >= 11) | .key3"`: 管道
- `cat test.json | jq --arg foo 123 --arg bar 456 '{key1: .key1, foo: $foo, bar: $bar}'`: 变量

## 链接

- 官网: <https://stedolan.github.io/jq/>
- 手册: <https://stedolan.github.io/jq/manual/>

