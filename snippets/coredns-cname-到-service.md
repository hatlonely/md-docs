# coredns cname 到 service

[//]: <> (coredns, cname, k8s, 网络)

在 k8s 内部将一个域名解析到一个 service，可以直接通过 coredns 实现

```
rewrite name abc.hatlonely.com abc-service.namespace.svc.cluster.local
```

## 链接

- coredns rewrite: <https://coredns.io/plugins/rewrite/>
- k8s通过coredns配置cname: <https://blog.horus-k.com/2021/05/13/k8s%E9%80%9A%E8%BF%87coredns%E9%85%8D%E7%BD%AEcname/>
