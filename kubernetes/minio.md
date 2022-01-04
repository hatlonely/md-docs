# minio

## minio 命令行工具 mc

- 创建凭证: `mc alias set home http://k8s.minio.hatlonely.com console console123 --api S3v4`
- 创建 bucket: `mc mb home/article`
- 上传: `mc cp * home/article`

## 常见问题

### 413 Request Entity Too Large

**问题原因**

nginx ingress 默认限制上传大小为 1M

**问题解决**

在 ingress 的 annotation 中增加注解：`nginx.ingress.kubernetes.io/proxy-body-size: "100m"`

## 链接

- github minio: <https://github.com/minio/minio>
- github minio go client: <https://github.com/minio/minio-go>
- minio 命令行 mc: <https://docs.min.io/docs/minio-admin-complete-guide.html>
