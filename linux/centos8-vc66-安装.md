# centos8 vc66 安装

## 准备

1. vc66
2. 键盘鼠标
3. 显示器
4. 刻录 centos8 的 U 盘

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
   2. 创建新用户
   3. 点击 `FINISH CONFIGURATION` 完成配置
