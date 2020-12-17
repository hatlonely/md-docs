# golang docker 镜像制作最佳实践

长期以来，我们的镜像制作都是利用 golang 的本地交叉编译，再用 COPY 命令将编译结果拷贝到镜像中，这种方式存在如下问题

1. 不同的宿主机环境不同，编译出来的二进制可能会不一致
2. golang 版本更新流程比较复杂
3. 本地调试时，需要修改 Makefile，当然也可以增加一个命令专门用来编译本地二进制解决

为了解决这些问题，引入 docker 编译和镜像制作

## Docker 镜像编译

```Dockerfile
FROM golang:1.14 AS build
COPY . /go/src/
WORKDIR /go/src/
RUN make build

FROM centos:centos7
COPY --from=build /go/src/build /work/myapp
WORKDIR /work/myapp
CMD [ "bin/myapp", "-c", "config/myapp.json" ]
```

这里有两个镜像，`golang:1.14` 用来编译，再将编译的结果 `COPY` 到目标镜像中，这样可以减少镜像大小

目标镜像选用 `centos:centos7`，主要是考虑 `centos` 比较稳定，工具也比较全面，对 centos 的有更多的运维经验，比较适合我们的技术栈，最终的镜像大小大概在 300M 左右

如果想要更小的镜像，可以考虑 `alpine`，对应的编译镜像也选择 `alpine` 对应版本即可 `golang:1.14-alpine`

## GFW

google 的一些库，由于众所周知的原因，无法访问到，可以通过 `GOPROXY` 解决，在 Makefile 中增加如下代码

```Makefile
export GOPROXY=https://goproxy.cn
```

## 私有代码库

go mod 默认只支持共公的代码库，如果有私有代码库的依赖，通过 `GOPRIVATE` 解决，在 Makefile 中增加如下代码

```Makefile
export GOPRIVATE=gitlab.hatlonely.com
```

如果私有代码库不是公共的，可以通过 `git config` 替换 `url` 成带上授权信息的 `url`，在 Dockerfile 中增加如下代码

```Dockerfile
RUN git config --global url."https://<user>:<password/private-token>@gitlab.hatlonely.com".insteadOf "https://gitlab.hatlonely.com"
```

`private-token` 在 gitlab 的 Account 页面可以找到

## 隐藏授权信息

上一步中的 `password/private-token` 属于敏感信息，提交到代码里面会有安全风险，可以通过 Docker 的 ARG 命令传入，Dockerfile 中新增如下代码

```Dockerfile
ARG git_url
ARG git_url_instand_of
RUN git config --global url."$git_url".insteadOf "$git_url_instand_of"
```

Makefile 中新增

```Makefile
.PHONY: image
image:
	docker build --build-arg git_url=${GOPRIVATE_GIT_URL} --build-arg git_url_instand_of=${GOPRIVATE_GIT_URL_INSTEAD_OF} --tag=${dockeruser}/${repository}:${version} .
```

在宿主机的环境变量中设置

```sh
export GOPRIVATE_GIT_URL=https://<user>:<password/private-token>@gitlab.hatlonely.com
export GOPRIVATE_GIT_URL_INSTEAD_OF=https://gitlab.hatlonely.com
```

这样授权信息通过宿主机的环境变量，传给 Makefile，Makefile 传给 docker build，最终在 dockerfile 中通过 ARG 命令获取到授权信息

## 完整代码

### Dockerfile

```dockerfile
FROM golang:1.14 AS build

ARG git_url
ARG git_url_instand_of
RUN git config --global url."$git_url".insteadOf "$git_url_instand_of"

COPY . /go/src/
WORKDIR /go/src/
RUN make build

FROM centos:centos7
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "Asia/Shanghai" >> /etc/timezone

COPY --from=build /go/src/build /work/myapp
WORKDIR /work/myapp
CMD [ "bin/myapp", "-c", "config/myapp.json" ]
```

### Makefile

```makefile
binary=myapp
dockeruser=hatlonely
gituser=hatlonely
repository=myapp
version=1.0.1
export GOPROXY=https://goproxy.cn
export GOPRIVATE=gitlab.hatlonely.com

.PHONY: build
build: cmd/main.go internal/*/*.go Makefile vendor
	mkdir -p build/bin
	go build -ldflags "-X 'main.Version=`sh scripts/version.sh`'" cmd/main.go && mv main build/bin/${binary} && cp -r config build/

vendor: go.mod go.sum
	@echo "install golang dependency"
	go mod tidy
	go mod vendor

codegen: api/myapp.proto
	mkdir -p api/gen/go && mkdir -p api/gen/swagger
	protoc -I.. -I. --gofast_out=plugins=grpc,paths=source_relative:api/gen/go/ $<
	protoc -I.. -I. --grpc-gateway_out=logtostderr=true,paths=source_relative:api/gen/go $<
	protoc -I.. -I. --swagger_out=logtostderr=true:api/gen/swagger $<

.PHONY: image
image:
	docker build --build-arg git_url=${GOPRIVATE_GIT_URL} --build-arg git_url_instand_of=${GOPRIVATE_GIT_URL_INSTEAD_OF} --tag=${dockeruser}/${repository}:${version} .
```

## 链接

- Dockerfile 最佳实践: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
