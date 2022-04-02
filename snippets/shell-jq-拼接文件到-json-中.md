# shell jq 拼接文件到 json 中

[//]: <> (shell, jq, json)

```shell
for adapter in "doc/convert doc_convert.yaml"; do
    read name definition <<< ${adapter}
    echo '{
    "Action": "CreateAdapter"
    }' | jq --arg definition "$(cat adapter/definition/${definition})" --arg name "${name}" '. + {"Name": $name, "Defintion": $definition}'
done
```

## 链接

- 代码参考: <https://gist.github.com/joar/776b7d176196592ed5d8>
