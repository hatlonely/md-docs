# linux 获取本机 ip 地址

## 获取公网 ip

```shell
dig +short myip.opendns.com @resolver1.opendns.com
curl ifconfig.me
curl ipinfo.io/ip
curl api.ipify.org
curl ident.me
curl ipecho.net/plain
```

## 获取内网 ip

```shell
ifconfig -a | grep -C 4 en0 | grep inet | grep netmask | grep broadcast | grep -Eo "inet \d+.\d+.\d+.\d+" | grep -Eo "\d+.\d+.\d+.\d+"
```
