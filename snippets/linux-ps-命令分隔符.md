# ps 命令分隔符号

ps 命令的 command 字段有时候会出现空格，不方便后面使用 awk 作字段分割

ps 提供了一种类似于 `printf` 的格式化输出方式，可以解决这个问题

```
ps -A -o "|%U|%t|%C|%z|%a|"
```

输出样例

```
|USER    |    ELAPSED|%CPU|   VSZ|COMMAND                    |
|weboffi+|43-00:21:13| 0.0| 16032|/bin/sh -c ulimit -c 0 && /|
|root    |43-00:21:12| 0.0| 27132|/usr/sbin/crond -i         |
|weboffi+|43-00:21:12| 0.1|1195328|/data/weboffice/bin/editser|
|weboffi+|43-00:21:12| 0.0|391396|webet ready                |
|weboffi+|43-00:21:12| 0.0|391816|webet ready                |
|weboffi+|43-00:21:12| 0.0|391624|webet ready                |
|weboffi+|43-00:21:12| 0.0|391624|webet ready                |
|weboffi+|43-00:21:12| 0.0|391392|webet ready                |
|weboffi+|43-00:21:12| 0.0|391628|webet ready                |
|weboffi+|43-00:21:12| 0.0|391816|webet ready                |
|weboffi+|43-00:21:12| 0.0|391528|webet ready                |
|weboffi+|43-00:21:12| 0.0|391632|webet ready                |
|weboffi+|43-00:21:12| 0.0|391788|webet ready                |
|weboffi+|43-00:21:12| 0.0|391788|webet ready                |
|weboffi+|      15:27| 0.0| 16164|/bin/sh                    |
|weboffi+|      00:00| 0.0| 40296|ps -A -o |%U|%t|%C|%z|%a|  |
```

但是并不是所有字段都有对应的格式化输出的字段，比如 etimes（进程运行时长）和 rsz（rss 实际内存占用）就没有，
这种情况，可以把 command 字段放到最后，awk 处理的时候将超出长度的字段用空格拼接在一起

格式化支持的字段

| CODE | NORMAL | HEADER  |
| ---- | ------ | ------- |
| %C   | pcpu   | %CPU    |
| %G   | group  | GROUP   |
| %P   | ppid   | PPID    |
| %U   | user   | USER    |
| %a   | args   | COMMAND |
| %c   | comm   | COMMAND |
| %g   | rgroup | RGROUP  |
| %n   | nice   | NI      |
| %p   | pid    | PID     |
| %r   | pgid   | PGID    |
| %t   | etime  | ELAPSED |
| %u   | ruser  | RUSER   |
| %x   | time   | TIME    |
| %y   | tty    | TTY     |
| %z   | vsz    | VSZ     |

## 链接

- stackoverflow: <https://stackoverflow.com/questions/3114741/generating-a-csv-list-from-linux-ps>
- manual ps: <https://man7.org/linux/man-pages/man1/ps.1.html#AIX_FORMAT_DESCRIPTORS>

