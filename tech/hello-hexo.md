# hello hexo

hexo 是一个静态网站生成器，支持 markdown 文件，有非常多主题可以挑选，非常适合用来生成博客网站

## 安装

hexo 使用 Node.js，因此需要 node 环境

```shell
brew install node
npm install hexo-cli -g
```

## 建站

下面命令会创建一个 blog 目录，其中 `source/_posts` 目录中是静态的文件

- `_config.yml`: 全局配置文件
- `package.json`: 应用信息，由 npm 管理，一般不需要关注
- `scaffolds`: 模板文件夹，新建文章的默认填充内容
- `source`: 资源文件夹
    - `_posts`: markdown 文件目录
- `themes`: 主题文件夹，需要自定义开发时才会需要，不建议使用

```shell
hexo init blog
cd blog
npm install
hexo server
```

## 配置 fluid 主题

默认的主题比较简陋，可以从[官网](https://hexo.io/themes/)挑选喜欢的主题，以 fluid 为例

1. 安装主题 `npm install --save hexo-theme-fluid`
2. 修改 `_config.yml`

```yaml
theme: fluid
language: zh-CN
```

3. 创建关于也: `hexo new page about`
4. 开启字数统计，在 `scaffolds/post.md` 模板中添加

```yaml
title: {{ title }}
date: {{ date }}
tags:
wordcount:
min2read:
```

5. 主题更新 `npm update --save hexo-theme-fluid`

更多配置参考[fluid用户手册](https://hexo.fluid-dev.com/docs/start)

## 生成静态页面

执行下面命令会生成静态文件到 `public` 文件夹中

```
hexo generate
```

## 部署

hexo 还提供了一键部署功能，可以将生成的静态页面部署到 github

1. 安装部署器 `npm install hexo-deployer-git --save`
2. 配置部署器，修改 `_config.yml`

```yaml
deploy:
  type: git
  repo: <repository url>
```

## 链接

- Hexo 中文官网: <https://hexo.io/zh-cn/>
- Hexo 主题: <https://hexo.io/themes/>
- Hexo Fluid 用户手册: <https://hexo.fluid-dev.com/docs/start>
