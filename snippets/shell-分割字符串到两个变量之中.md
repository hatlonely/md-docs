# shell 分割字符串到两个变量之中

[//]: <> (shell, read)

```shell
for adapter in "doc/convert doc_convert.yaml" "doc/preview doc_preview.yaml"; do
    read name definition <<< ${adapter}
    echo ${name} ${definition}
done
```

## 链接

- How to split one string into multiple variables in bash shell: <https://stackoverflow.com/questions/10520623/how-to-split-one-string-into-multiple-variables-in-bash-shell>
