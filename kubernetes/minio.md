# minio

## minio 命令行工具 mc

- 创建凭证: `mc alias set home http://k8s.minio.hatlonely.com console console123 --api S3v2`
- 创建 bucket: `mc mb home/article`
- 上传: `mc cp * home/article`

## 链接

- github minio: <https://github.com/minio/minio>
- github minio go client: <https://github.com/minio/minio-go>
- minio 命令行 mc: <https://docs.min.io/docs/minio-admin-complete-guide.html>
