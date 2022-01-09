# linux 端口连通性测试

[//]: <> (linux, telnet, 网络, 连通性测试)

使用 telnet 命令可以查看网络连通性，直接 `telnet <ip/host> <port>` 即可

```shell
telnet 123.57.26.76 5443
```

连接成功

```
Trying 123.57.26.76...
Connected to 123.57.26.76.
Escape character is '^]'.
```

连接失败，会一直卡在 Trying 界面

```
Trying 123.57.26.76...
```

## 链接

- 测试端口连通性的四种方法: <https://www.cnblogs.com/young233/p/11718392.html>
