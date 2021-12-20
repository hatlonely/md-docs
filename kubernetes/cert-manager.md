# cert-manager

## 部署

```shell
kubectl apply -f https://github.com/jetstack/cert-manager/releases/download/v1.6.1/cert-manager.crds.yaml
helm repo add jetstack https://charts.jetstack.io
helm install cert-manager --namespace cert-manager --version v1.6.1 jetstack/cert-manager

# 卸载
helm delete cert-manager --namespace cert-manager
kubectl delete -f https://github.com/jetstack/cert-manager/releases/download/v1.6.1/cert-manager.crds.yaml
```

## 创建 Acme ClusterIssuer

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-http01
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    privateKeySecretRef:
      name: letsencrypt-http01-account-key
    solvers:
    - http01:
       ingress:
         class: nginx
```

## ingress 使用 Acme 证书

新增如下 annotation 即可

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-http01
    kubernetes.io/ingress.class: nginx
    kubernetes.io/tls-acme: "true"
  labels:
    app: kibana
    heritage: Helm
    release: kibana
  name: kibana-kibana
  namespace: dev
spec:
  rules:
  - host: k8s.kibana.hatlonely.com
    http:
      paths:
      - backend:
          service:
            name: kibana-kibana
            port:
              number: 5601
        path: /
        pathType: ImplementationSpecific
  tls:
  - hosts:
    - k8s.kibana.hatlonely.com
    secretName: kibana-tls
```

## 链接

- artifacthub: <https://artifacthub.io/packages/helm/cert-manager/cert-manager>
- github: <https://github.com/jetstack/cert-manager/tree/v1.6.1/deploy/charts/cert-manager>
