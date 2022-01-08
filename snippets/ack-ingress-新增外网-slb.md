# ack ingress 新增外网 slb

[//]: <> (ack, ingress, k8s, slb, 阿里云)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-ingress-lb-internet
  namespace: kube-system
  labels:
    app: nginx-ingress-lb-internet
  annotations:
    # 指明SLB实例地址类型为私网类型。
    service.beta.kubernetes.io/alicloud-loadbalancer-address-type: internet
    # 修改为您的私网SLB实例ID。
    service.beta.kubernetes.io/alicloud-loadbalancer-id: "lb-uf6fvcn436neplqmkozev"
    # 是否自动创建SLB端口监听（会覆写已有端口监听），也可手动创建端口监听。
    service.beta.kubernetes.io/alicloud-loadbalancer-force-override-listeners: 'true'
spec:
  type: LoadBalancer
  # route traffic to other nodes
  externalTrafficPolicy: "Cluster"
  ports:
  - port: 80
    name: http
    targetPort: 80
  - port: 443
    name: https
    targetPort: 443
  selector:
    # select app=ingress-nginx pods
    app: ingress-nginx
```

## 链接

- 使用已有的 slb 创建服务: <https://help.aliyun.com/document_detail/181518.html>
