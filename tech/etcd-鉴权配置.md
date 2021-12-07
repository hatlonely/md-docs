# etcd 鉴权配置

etcd 默认访问是没有鉴权的，存在一定的安全隐患。etcd 从 2.1 版本之后引入了鉴权机制，2.1 之前任何人都可以通过 api 修改任何 key

## 基本概念

- 用户(user): 访问 api 的需要用户凭证，包括用户名密码
- 角色(role): 用户能对某些资源的某些操作叫做权限，一个角色可以拥有多种权限，一个用户可以扮演多种角色

特殊的用户和角色

- 用户 root: 用户 root 必须在安全特性开启之前创建，并且 root 用户拥有 root 角色，root 角色拥有所有的权限
- 角色 root: 角色 root 是不能被修改的，拥有所有权限，包括读取和修改任意 key 和读取和修改任何其他的授权策略
- 角色 guest: 角色 guest 是所有不带鉴权访问 api 所具有的权限，在开启安全特性后，默认的 guest 角色可以访问任何 key

## 鉴权相关配置

etcd 的鉴权配置主要通过 etcd 客户端工具 `etcdctl` 来实现

### 鉴权相关

```shell
# 创建 root 用户
etcdctl user add root:123456
# 开启授权
etcdctl auth enable
# 关闭授权
etcdctl -u root:123456 auth disable
# 禁止匿名访问
etcdctl -u root:123456 role remove guest
```

### 角色相关

```shell
# 角色列表
etcdctl -u root:123456 role list
# 新增角色
etcdctl -u root:123456 role add service-config-rw
etcdctl -u root:123456 role add service-config-ro
etcdctl -u root:123456 role add service-config-wo
# 授权角色权限
etcdctl -u root:123456 role grant service-config-rw -path '/service/config/*' -readwrite
etcdctl -u root:123456 role grant service-config-ro -path '/service/config/*' -read
etcdctl -u root:123456 role grant service-config-wo -path '/service/config/*' -write
# 回收角色权限
etcdctl -u root:123456 role revoke service-config-rw -path '/service/config/*' -write
# 查看角色
etcdctl -u root:123456 role get service-config-rw
# 删除角色
etcdctl -u root:123456 role remove service-config-rw
```

### 用户相关

```shell
# 用户列表
etcdctl -u root:123456 user list
# 新增用户
etcdctl -u root:123456 user add hatlonely:123456
# 授权用户角色
etcdctl -u root:123456 user grant hatlonely -roles service-config-ro
etcdctl -u root:123456 user grant hatlonely -roles service-config-wo
# 回收用户角色
etcdctl -u root:123456 user revoke hatlonely -roles service-config-wo
# 查看用户
etcdctl -u root:123456 user get hatlonely
# 删除用户
etcdctl -u root:123456 user remove hatlonely
# 修改密码
etcdctl -u root:123456 user passwd hatlonely
```

### 带鉴权的访问

```shell
# 设置 key
etcdctl -u hatlonely:123456 set /service/config/key val
# 获取 key
etcdctl -u hatlonely:123456 get /service/config/key
```

## 鉴权配置脚本

下面这个脚本，创建了一个用户，授权这个用户所有 key 的读写，并且禁用匿名的访问

```shell
ETCD_ROOT_PASSWORD=123456
ETCD_USERNAME=hatlonely
ETCD_PASSWORD=123456
ETCD_ROLE=all-keys-rw

etcdctl user add root:${ETCD_ROOT_PASSWORD}
etcdctl role add ${ETCD_ROLE}
etcdctl role grant ${ETCD_ROLE} -path '/*' -readwrite
etcdctl user add ${ETCD_USERNAME}:${ETCD_PASSWORD}
etcdctl user grant ${ETCD_USERNAME} -roles ${ETCD_ROLE}
etcdctl auth enable
etcdctl -u root:${ETCD_ROOT_PASSWORD} role remove guest
```

## 链接

- etcd v2.3 鉴权: <https://etcd.io/docs/v2.3/authentication/>
