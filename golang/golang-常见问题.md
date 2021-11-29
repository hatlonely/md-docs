# golang 常见问题

## go mod tidy 报 unknown revision 错误

```shell
go: gitlab.com/user/repo@v0.1.64: reading gitlab.com/user/repo/go.mod at revision v0.1.64: unknown revision v0.1.64
```

可能是 cache 缓存出问题了，直接 `go clean --modcache` 清理缓存后恢复


