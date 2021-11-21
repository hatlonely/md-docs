# flutter mac 开发环境搭建

[//]: <> (flutter, 开发环境, mac)

## 安装 Android Studio

<https://developer.android.google.cn/studio/>

## 安装 flutter

```shell
brew install flutter
flutter doctor

export PATH=/Users/hatlonely/Library/Android/sdk/tools/bin/:$PATH
sdkmanager --install "cmdline-tools;latest"
```

## 创建 flutter 项目

```shell
mkdir flutter-article && cd flutter-article
flutter create flutter_article
```

## 设置 Android Studio

1. 安装 flutter 插件
2. 打开一个 flutter 项目
3. 设置 dart sdk: `/usr/local/Caskroom/flutter/2.5.3/flutter/bin/cache/dart-sdk`

## 链接

- Android Studio: <https://developer.android.google.cn/studio/>
- Flutter 官网文档: <https://docs.flutter.dev/get-started/install>

