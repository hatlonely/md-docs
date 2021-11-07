# kubernetes sealos 一键部署

## 部署

1. 安装 sealos 工具

    ```shell
    wget -c https://sealyun.oss-cn-beijing.aliyuncs.com/latest/sealos && \
        chmod +x sealos && mv sealos /usr/bin
    ```

2. 下载离线包 <https://www.sealyun.com/vipDetail?end_days=273&name=offline_package>
3. 安装 kubernetes

    ```shell
    sealos init --passwd '' \
        --interface wlo1 \
        --master 192.168.0.10  --master 192.168.0.11  --master 192.168.0.12  \
        --pkg-url kube1.22.3.tar.gz \
        --version v1.22.3 \
     #   --repo registry.aliyuncs.com/google_containers \
     #   --without-cni
    ```

4. kube config 文件 `cat /etc/kubernetes/admin.conf`
5. 修改 calico 网卡自动发现 `kubectl edit daemonset -n kube-system calico-node`

    ```yaml
    - name: IP_AUTODETECTION_METHOD
      value: "interface=eth.*|wlp0s20f3|wlo1"
    ```

6. 安装 calico

    ```shell
    kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
    ```

7. 修改 calico 镜像地址

    ```
    kubectl edit kubectl edit deployments calico-kube-controllers -n kube-system
    kubectl edit daemonset -n kube-system calico-node

    # 修改 docker.io 镜像地址到 docker.mirrors.ustc.edu.cn
    ```

## 卸载

    ```shell
    sealos clean --all -f
    ```