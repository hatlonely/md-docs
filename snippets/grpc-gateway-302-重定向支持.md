# grpc gateway 302 重定向支持

[//]: <> (grpc-gateway, 302, curl, http)

grpc gateway 可以通过 metadata 设置返回的 header

```go
func (s *ExampleService) Echo(ctx context.Context, req *api.EchoReq) (*api.EchoRes, error) {
	header := metadata.Pairs("Location", "https://www.baidu.com")
	if err := grpc.SendHeader(ctx, header); err != nil {
		return nil, errors.Wrap(err, "grpc.SendHeader failed")
	}

	return &api.EchoRes{Message: req.Message}, nil
}
```

mux server 支持重写返回结果，判断返回的 header 中是否包含 Location，如果包含，返回 302 跳转地址

```go
func MuxForwardResponseOption() runtime.ServeMuxOption {
	return runtime.WithForwardResponseOption(func(ctx context.Context, w http.ResponseWriter, _ proto.Message) error {
		headers := w.Header()
		if location, ok := headers["Location"]; ok {
			w.Header().Set("Location", location[0])
			w.WriteHeader(http.StatusFound)
		}
		return nil
	})
}
```

初始化 mux server 时需要传入上面的选项

```go
muxServer := runtime.NewServeMux(
    runtime.WithForwardResponseOption(MuxForwardResponseOption()),
)
```

curl -L 参数可以支持 302 跳转，可以用来简单测试代码逻辑功能

```shell
curl -L 127.0.0.1/v1/echo
```

## 链接

- stackoverflow: <https://stackoverflow.com/questions/49878855/how-to-do-a-302-redirect-in-grpc-gateway>
- grpc gateway: <https://grpc-ecosystem.github.io/grpc-gateway/docs/mapping/customizing_your_gateway/#mutate-response-messages-or-set-response-headers>
