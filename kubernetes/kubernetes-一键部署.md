# kubernetes sealos 一键部署

[//]: <> (kubernetes, sealos, k8s)

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
     #   --without-cni
    ```

## 卸载

    ```shell
    sealos clean --all -f
    ```

## 常见问题

### cni plugin not initialized

**问题表现**

- `kubectl get pods -A` 显示 calico 和 coredns 处于 Pending 状态
- `kubectl describe pods -n kube-system coredns-xxx` 显示由于没有 ready 的节点可以调度
- `kubectl get nodes -A` 显示 node NotReady
- `kubectl describe nodes node0` 显示 `KubeletNotReady  container runtime network not ready: NetworkReady=false reason:NetworkPluginNotReady message:Network plugin returns error: cni plugin not initialized`
- `ifconfig` 查看节点网络，calico 网络没有创建出来

**问题原因**

猜测可能是之前卸载的时候，网络环境有一些冲突

**问题解决**

重启所有节点后重新安装

### kibana 和 phpadmin ingress 没有外部端点

**问题表现**

- `kubectl get ingress -A` 显示 kibana 和 phpadmin 能创建出来，但是没有端点
- 和有端点的节点对比，发现有节点的端点设置了 `ingressClassName: nginx`

**问题原因**

猜测这个版本的 ingress 需要设置 ingressClassName 才能暴露外部端点，但是 dashboard 同样没有 ingressClassName 但是可以暴露外部端点

**问题解决**

- `kubectl edit ingress kibana-kibana -n dev` 修改 ingress，添加 ingressClassName 后恢复

## 链接

- sealyun 官网: <https://www.sealyun.com/>
- sealos github 项目: <https://github.com/fanux/sealos>
