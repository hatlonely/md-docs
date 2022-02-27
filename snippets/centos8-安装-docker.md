# centos8 安装 docker

1. 添加 repository
    ```shell
    dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
    ```
2. 安装 docker
    ```shell
    dnf list docker-ce
    dnf install docker-ce --nobest -y
    ```
3. 启动 docker
    ```shell
    systemctl start docker
    systemctl enable docker
    ```

## 链接

- install docker ce centos8: <https://www.linuxtechi.com/install-docker-ce-centos-8-rhel-8/>
