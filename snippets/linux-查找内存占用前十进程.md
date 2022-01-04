# linux 查找内存占用前十进程

[//]: <> (linux, ps, awk, 运维)

## 问题

打印内存占用前十的进程名以及所占用的内存，内存大小以方便人类可读的格式输出

## 解决

1. 使用 ps 命令获取内存（rss）和进程名，通过内存排序
2. 使用 head 命令获取前十个进程
3. 使用 awk 格式化内存大小

## 代码

```shell
ps --no-headers -e -Ao "rss,etime,command" --sort=-rss | head -10 | awk '{
    hr[1024**2]="GB"; hr[1024]="MB";
    for (x=1024**3; x>=1024; x/=1024) {
        if ($1>=x) {
            printf("%-.1f%-5s ", $1/x, hr[x]); break
        }
    }
    printf ("\t%-12s", $2)
    for ( x=3 ; x<=NF ; x++ ) {
        printf(" %s",$x)
    } 
    print ("")
}'
```

输出样例

```txt
2.5GB           87-18:07:16  /data/weboffice/bin/editserver -core webet
2.2GB           06:33:33     webet ver:20210929220102-c9fcf70066 key:edit/49840998255 lang:zh-CN
1.3GB           08:04:49     webet ver:20210929220102-c9fcf70066 key:edit/45441051812 lang:zh-CN
742.3MB         01:00:33     webet ver:20210929220102-c9fcf70066 key:edit/44995496582 lang:zh-CN
665.5MB         07:44:52     webet ver:20210929220102-c9fcf70066 key:edit/39948839310 lang:zh-CN
652.3MB         4-02:28:07   webet ver:20210929220102-c9fcf70066 key:edit/49218545242 lang:zh-CN
620.6MB         9-00:20:24   webet ver:20210929220102-c9fcf70066 key:edit/48091796415 lang:zh-CN
579.7MB         03:15:16     webet ver:20210929220102-c9fcf70066 key:edit/47679133570 lang:zh-CN
577.0MB         06:24:31     webet ver:20210929220102-c9fcf70066 key:edit/49607735853 lang:zh-CN
562.2MB         05:42:19     webet ver:20210929220102-c9fcf70066 key:edit/19939283109 lang:zh-CN
```
