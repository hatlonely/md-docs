# kubernetes sealos 一键部署

## 部署

1. 安装 sealos 工具

    ```
    wget -c https://sealyun.oss-cn-beijing.aliyuncs.com/latest/sealos && \
        chmod +x sealos && mv sealos /usr/bin
    ```

2. 下载离线包 <https://www.sealyun.com/vipDetail?end_days=273&name=offline_package>
3. 安装 kubernetes

    ```
    sealos init --passwd '' \
        --master 192.168.0.10  --master 192.168.0.11  --master 192.168.0.12  \
        --pkg-url kube1.22.3.tar.gz \
        --version v1.22.3 \
        --repo registry.aliyuncs.com/google_containers \
        --without-cni
    ```

4. kube config 文件 `cat /etc/kubernetes/admin.conf`
5. 安装 calico

    ```
    kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
    ```

6. 修改 calico 镜像地址

    ```
    kubectl edit kubectl edit deployments calico-kube-controllers -n kube-system

    # 修改 docker.io 镜像地址到 docker.mirrors.ustc.edu.cn
    ```
