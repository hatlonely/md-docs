# linux 僵尸进程清理

[//]: <> (linux, ps, awk, 运维)

## 问题

线上进程 myapp 由于未知的原因偶而会进入到 cpu 空转状态，且无法自动恢复，这种进程多了之后，会将 cpu 打满，进而引发稳定性问题

通过 top 命令观察这些进程，有两个明显特点：

1. 运行时间特别长，超过 1 天
2. cpu 占用率在 100% 左右（多核处理器）

## 解决

1. 使用 ps 命令获取进程的 pid，名称，cpu 和运行时间，按照 cpu 利用率排序
2. 使用 grep 过滤异常的进程名
3. 使用 awk 过滤 cpu 大于 96 和运行时间超过 1 天的 pid
4. 通过管道传给 kill 命令清理僵尸进程

## 代码

```shell
ps -e -o pid,ppid,cmd,%mem,etimes,%cpu --sort=-%cpu | head -20 | grep "myapp" | awk '{
    pid=$1
    time=$6
    cpu=$7
    if (cpu > 96 && time > 3600*24) {
        print pid
    }
}' | xargs kill
```
