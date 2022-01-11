# kubernetes ingress 代理 oss bucket

[//]: <> (ack, ingress, k8s, oss, 阿里云, wechat)

业务为了支持客户的微信小程序，需要在域名的根目录下增加一个验证文件

之前是通过制作一个 nginx 镜像，将验证文件添加到镜像中，用这个镜像启动一个 service，然后通过 ingress 转到到这个 service 上，

这个方案有几个缺陷：

1. 每次一个新的客户过来都需要制作一个新的镜像，发布一次服务；
2. 另外镜像制作的新镜像有可能有问题，比如出现过文件权限不对，导致发布不生效的问题；
3. 小程序文件的维护比较困难，之前的小程序的文件维护在 git 上，出现过分支未 merge 导致原有的验证文件缺失，发布上线后导致原有客户小程序不可用；

考虑将文件存储 oss 中，用 ingress 代理 oss 方案

## 创建 bucket

使用 `ossutil` 工具创建公共读的 bucket，并将原有的小程序文件上传至 bucket 中

``` shell
ossutil -i "${OPS_AK}" -k "${OPS_SK}" -e "oss-${REGION_ID}.aliyuncs.com" mb "oss://${OSS_WECHAT_BUCKET}" --acl=public-read
for file in ops/wechat/docker/wechat/*; do
    ossutil -i "${OPS_AK}" -k "${OPS_SK}" -e "oss-${REGION_ID}.aliyuncs.com" cp -r "${file}" "oss://${OSS_WECHAT_BUCKET}/$(basename $file)"
done
```

## 创建 Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: wechat-oss-proxy
  namespace: ${NAMESPACE}
spec:
  type: ExternalName
  externalName: ${OSS_WECHAT_BUCKET}.oss-${REGION_ID}.aliyuncs.com
```

## 创建 Ingress

service 能将请求转发到 oss 服务，但是 url 地址中的 host 还需要修改成 oss 的地址，
可以使用 `nginx.ingress.kubernetes.io/configuration-snippet` annotation 实现这个功能

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/ssl-redirect: "false"
    nginx.ingress.kubernetes.io/configuration-snippet: |
      proxy_set_header Host ${OSS_WECHAT_BUCKET}.oss-${REGION_ID}.aliyuncs.com;
  labels:
    app.kubernetes.io/component: "${OSS_WECHAT_BUCKET}"
    app.kubernetes.io/instance: "${OSS_WECHAT_BUCKET}"
    app.kubernetes.io/name: "${OSS_WECHAT_BUCKET}"
  name: wechat-oss-proxy
  namespace: ${NAMESPACE}
spec:
  rules:
    - host: ${HOST}
      http:
        paths:
          - path: /
            backend:
              serviceName: wechat-oss-proxy
              servicePort: 80
  tls:
    - hosts:
        - ${HOST}
      secretName: ${TLS_SECRET}
```

## 链接

- ossutil: <https://help.aliyun.com/document_detail/120050.html>
- kubernetes ingress代理访问阿里云oss记: <https://developer.aliyun.com/article/783999>
- 修改 ingress host: <https://stackoverflow.com/questions/54624647/is-it-possible-to-rewrite-host-header-in-k8s-ingress-controller>
