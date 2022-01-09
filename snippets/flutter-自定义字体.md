# flutter 自定义字体

[//]: <> (flutter, web, font)


flutter web 不支持直接使用系统字体，默认的字体来自于于 google，下载很慢，而中文字体又比较大，耗时很长，可以考虑将字体放到本地服务中

首先需要下载字体到项目的根目录 assets/fonts 目录下

```yaml
fonts:
  step:
    - mkdir -p ${TMP}/assets/fonts && mkdir -p flutter_article/assets/fonts
    - wget https://fonts.google.com/download?family=Roboto -O ${TMP}/assets/fonts/Roboto.zip
    - unzip -o ${TMP}/assets/fonts/Roboto.zip -d flutter_article/assets/fonts/Roboto
    - wget https://fonts.google.com/download?family=Roboto%20Condensed -O ${TMP}/assets/fonts/RobotoCondensed.zip
    - unzip -o ${TMP}/assets/fonts/RobotoCondensed.zip -d flutter_article/assets/fonts/RobotoCondensed
    - wget https://fonts.google.com/download?family=Source%20Code%20Pro -O ${TMP}/assets/fonts/SourceCodePro.zip
    - unzip -o ${TMP}/assets/fonts/SourceCodePro.zip -d flutter_article/assets/fonts/SourceCodePro
    - wget https://fonts.google.com/download?family=Noto%20Sans%20SC -O ${TMP}/assets/fonts/NotoSansSC.zip
    - unzip -o ${TMP}/assets/fonts/NotoSansSC.zip -d flutter_article/assets/fonts/NotoSansSC
    - wget https://fonts.google.com/download?family=Noto%20Serif%20SC -O ${TMP}/assets/fonts/NotoSerifSC.zip
    - unzip -o ${TMP}/assets/fonts/NotoSerifSC.zip -d flutter_article/assets/fonts/NotoSerifSC
    - wget https://fonts.google.com/download?family=ZCOOL%20XiaoWei -O ${TMP}/assets/fonts/ZCOOLXiaoWei.zip
    - unzip -o ${TMP}/assets/fonts/ZCOOLXiaoWei.zip -d flutter_article/assets/fonts/ZCOOLXiaoWei
    - wget https://github.com/adobe-fonts/source-han-sans/releases/download/2.004R/SourceHanSansSC.zip -O ${TMP}/assets/fonts/SourceHanSansSC.zip
    - unzip -o ${TMP}/assets/fonts/SourceHanSansSC.zip -d flutter_article/assets/fonts/SourceHanSansSC
    - wget https://fonts.google.com/download?family=Cousine -O ${TMP}/assets/fonts/Cousine.zip
    - unzip -o ${TMP}/assets/fonts/Cousine.zip -d flutter_article/assets/fonts/Cousine
```

在 pubspec.yaml 中配置

```yaml
fonts:
    - family: Roboto
      fonts:
        - asset: assets/fonts/Roboto/Roboto-Thin.ttf
          weight: 100
        - asset: assets/fonts/Roboto/Roboto-Light.ttf
          weight: 300
        - asset: assets/fonts/Roboto/Roboto-Regular.ttf
          weight: 400
        - asset: assets/fonts/Roboto/Roboto-Medium.ttf
          weight: 500
        - asset: assets/fonts/Roboto/Roboto-Bold.ttf
          weight: 700
        - asset: assets/fonts/Roboto/Roboto-Black.ttf
          weight: 900
        - asset: assets/fonts/Roboto/Roboto-ThinItalic.ttf
          weight: 100
          style: italic
        - asset: assets/fonts/Roboto/Roboto-LightItalic.ttf
          weight: 300
          style: italic
        - asset: assets/fonts/Roboto/Roboto-Italic.ttf
          weight: 400
          style: italic
        - asset: assets/fonts/Roboto/Roboto-MediumItalic.ttf
          weight: 500
          style: italic
        - asset: assets/fonts/Roboto/Roboto-BoldItalic.ttf
          weight: 700
          style: italic
        - asset: assets/fonts/Roboto/Roboto-BlackItalic.ttf
          weight: 900
          style: italic
```

## 链接

- flutter 自定义字体: <https://docs.flutter.dev/cookbook/design/fonts>
- 字体下载代码样例: <https://github.com/hatlonely/flutter-article/blob/master/.ops.yaml>
- pubspec.yaml 样例: <https://github.com/hatlonely/flutter-article/blob/master/flutter_article/pubspec.yaml>
