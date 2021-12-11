# tunnel 开放家庭网络环境

[//]: <> (tunnel, 网络, k8s, kubernetes)

## 背景

在家庭的网络环境下搭建了一个 kubernetes，但是目前只能在路由器内网访问，现在想要实现公网访问，正常情况下，只要有一个固定的 ip 就可以解决这个问题，
但是由于运营商的限制，家庭网络是没有固定 ip 的，甚至运营商不允许路由器和光猫之间使用桥接方式连接，出口的 ip 和端口无法固定。

## 方案

首先需要一个固定的 ip 和端口，这里我使用阿里云的 ecs 服务，使用这台机器作为流量入口将请求转发到家庭网路。

但是这个转发不同于一般的反向代理，服务端是没有固定的出口 ip 和端口，ecs 是无法访问到的，但是服务端是可以访问公网的，
由服务端向 ecs 主动发起链接建立一条隧道是可行的，而 [tunnel](https://github.com/hatlonely/go-kit/blob/master/cmd/tunnel/README.md) 
刚好可以解决这个问题

## 解决

1. 新建一台 ecs，开放端口 80/443/6443/5080/5443/11443
2. 分发 tunnel-server 到 ecs，分发 tunnel-client 到内部节点

    ```shell
    scp -i ~/.ssh/dev.hatlonely.com.pem build/bin/tunnel-server root@123.57.26.76:/root
    
    scp build/bin/tunnel-agent 192.168.0.10:/home/hatlonely
    scp build/bin/tunnel-agent 192.168.0.11:/home/hatlonely
    scp build/bin/tunnel-agent 192.168.0.12:/home/hatlonely
    ```

3. 在 ecs 上启动 tunnel-server

   ```shell
   nohup ./tunnel-server --server.serverPort 80 --server.tunnelPort 5080 --server.workerNum 16 --server.acceptNum 5 --server.connQueueLen 200 --useStdoutJsonLogger &
   nohup ./tunnel-server --server.serverPort 443 --server.tunnelPort 5443 --server.workerNum 16 --server.acceptNum 5 --server.connQueueLen 200 --useStdoutJsonLogger &
   nohup ./tunnel-server --server.serverPort 6443 --server.tunnelPort 11443 --server.workerNum 16 --server.acceptNum 5 --server.connQueueLen 200 --useStdoutJsonLogger &
   ```

4. 在内部节点启动 tunnel-client

   ```shell
   nohup ./tunnel-agent --agent.tunnelAddr 123.57.26.76:5080 --agent.serverAddr 192.168.0.10:80 --useStdoutJsonLogger &
   nohup ./tunnel-agent --agent.tunnelAddr 123.57.26.76:5443 --agent.serverAddr 192.168.0.10:443 --useStdoutJsonLogger &
   nohup ./tunnel-agent --agent.tunnelAddr 123.57.26.76:11443 --agent.serverAddr 192.168.0.10:6443 --useStdoutJsonLogger &
   ```

5. 修改本地的 `~/.kube/config` 文件，跳过证书验证（因为证书只有本地 ip）

   ```yaml
   apiVersion: v1
   clusters:
   - cluster:
       server: https://123.57.26.76:6443
       insecure-skip-tls-verify: true
     name: home-k8s
   ```

## 链接

- tunnel : <https://github.com/hatlonely/go-kit/blob/master/cmd/tunnel/README.md>
