# k8s pod 绕过 coredns 解析

[//]: <> (coredns, dns, k8s, 网络)

设置 `deployment.spec.template.spec.dnsPolicy` 为 `Default` 即可

- `Default`: Pod 从运行所在的节点继承名称解析配置
- `ClusterFirst`: 默认配置，与配置的集群域后缀不匹配的任何 DNS 查询（例如 "www.kubernetes.io"） 都将转发到从节点继承的上游名称服务器，一般是 coredns。集群管理员可能配置了额外的存根域和上游 DNS 服务器
- `ClusterFirstWithHostNet`：对于以 hostNetwork 方式运行的 Pod，应显式设置其 DNS 策略 "ClusterFirstWithHostNet"
- `None`: 此设置允许 Pod 忽略 Kubernetes 环境中的 DNS 设置。Pod 会使用其 dnsConfig 字段 所提供的 DNS 设置

## 链接

- kubernetes deployment: <https://kubernetes.io/zh/docs/concepts/services-networking/dns-pod-service/>
