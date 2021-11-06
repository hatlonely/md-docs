# centos8 vc66 安装

## 准备

1. vc66
2. 键盘鼠标
3. 显示器
4. 刻录 centos8 的 U 盘
5. 路由器

## 安装

1. 修改引导从 U 盘启动系统
   1. 按 `<F2>` 进入系统引导
   2. `Boot` 页，第一启动项，选择 U 盘的 centos
   3. `Exit` 页，保存并重启
2. 重启后选择 `Instanll Centos Linux 8` 进入安装界面
   1. 语言选择 `English`，点击 `Continue`
   2. 磁盘分区 `System` -> `Installation Destination`
      1. 选择一块磁盘，直接点击 `Done`
      2. 提示没有磁盘，点击 `Reclaim space` 释放磁盘
      3. `Delete all` 释放所有磁盘空间
   3. 点击 `Root Password` 设置 root 密码
   4. 点击 `Begin Installation` 开始安装
3. 重启设置 centos
   1. 接受 License
   2. 创建新用户 `hatlonely`
   3. 点击 `FINISH CONFIGURATION` 完成配置

## 固定 IP

1. 在 vc66 终端中执行 `ifconfig` 找到机器 IP
2. 浏览器打开 `192.168.0.1` 登陆路由器
3. 【应用管理】 -> 【IP与MAC绑定】找到 vc66 IP 点击绑定
4. 修改节点名称和 IP
5. 重启 vc66（如果重启没有生效，可以尝试重启路由器）

## 连接

1. 免密登陆，拷贝公钥到服务器

    ```
    ssh-copy-id -i ~/.ssh/id_rsa.pub hatlonely@192.168.0.10
    ssh-copy-id -i ~/.ssh/id_rsa.pub hatlonely@192.168.0.11
    ssh-copy-id -i ~/.ssh/id_rsa.pub hatlonely@192.168.0.12
    ```

2. ssh 登陆 vc66 机器，修改 sshd 配置 `vim /etc/ssh/sshd_config`

    ```
    # 不允许 root 登陆
    PermitRootLogin no

    # 不允许密码登陆
    PasswordAuthentication no
    ```

3. 重启 etcd 是配置生效 `service sshd restart`
