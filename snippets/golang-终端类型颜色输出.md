# golang 终端类型颜色输出

`github.com/mattn/go-isatty` 包提供 `isatty.IsTermanal` 方法可以判断程序是运行在交互式的终端中还是程序中，这个特性可以用来判断是否要进行颜色输出

```golang
func Info(format string, args ...interface{}) {
	if isatty.IsTerminal(os.Stdout.Fd()) || isatty.IsCygwinTerminal(os.Stdout.Fd()) {
		fmt.Println(Render(fmt.Sprintf(format, args...), FormatSetBold, ForegroundGreen))
	} else {
		Trac(format, args...)
	}
}
```

## 链接

- How to check if your program is running in a terminal: <https://www.socketloop.com/tutorials/golang-how-to-check-if-your-program-is-running-in-a-terminal>
- go-kit 源码: <https://github.com/hatlonely/go-kit/blob/master/strx/color.go>
