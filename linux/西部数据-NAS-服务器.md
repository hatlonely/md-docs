# 西部数据 NAS 服务器

[//]: <> (nas, 西部数据, 存储)

## nfs 服务器

### 开启服务

- 浏览器输入 <http//:192.168.0.101> 登陆服务
- 设置 -> 网络 -> SSH -> 开 -> 配置 -> 密码

### 服务器配置

- 连接服务器: `ssh sshd@192.168.0.101`
- 修改 `/etc/exports` 文件，配置 nfs 目录
    ```
    "/nfs/data" 192.168.0.0/24(rw,no_root_squash,async,no_wdelay,insecure_locks,insecure,no_subtree_check,anonuid=501,anongid=1000)
    "/nfs/data2" 192.168.0.0/24(rw,no_root_squash,sync,no_wdelay,insecure_locks,insecure,no_subtree_check,anonuid=1001,anongid=1001)
    ```
- 重新加载 `exportfs -rv` 使配置生效

## nas 服务挂载

### Mac 系统

```
# 挂载
mkdir -p /Users/hatlonely/nas
mount_smbfs //hatlonely@192.168.0.101/data2 /Users/hatlonely/nas

# 卸载
umount /Users/hatlonely/nas
```

Mac 系统挂载后，可以直接通过 Finder 访问

### Centos 系统

```
# 挂载
mkdir -p /root/k8s
mount -t nfs -o hard,nfsvers=3 192.168.0.101:/nfs/data2 /root/k8s

# 卸载
umount /root/k8s
```
