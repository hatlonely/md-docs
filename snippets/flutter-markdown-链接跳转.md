# flutter markdown 链接跳转

flutter markdown 链接点击默认是不会跳转的，需要设置 `onTapLink` 参数

```dart
MarkdownBody(
    ...
    onTapLink: (String text, String? href, String title) async {
    if (!await launch(href!)) throw 'Could not launch $href';
    },
    ...
)
```

`launch` 函数在 `url_launcher` 包中，通过如下命令获取

```shell
flutter pub add url_launcher
```

## 链接

- flutter-markdown: <https://pub.dev/packages/flutter_markdown>
- 如何在 flutter markdown 中增加超链接: <https://stackoverflow.com/questions/60821607/how-to-add-hyperlink-to-text-in-a-markdown-in-flutter>
- url_launcher: <https://pub.dev/packages/url_launcher>
