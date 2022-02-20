# python3 pip 上传库

1. 注册 pypi 账号: <https://pypi.org/account/register/>
2. 编写代码
   - `README.rst`: 必须是 rst 格式，需要解析到 python 官网，[样例参考](https://github.com/gmyrianthous/example-publish-pypi)
   - `LICENSE`: 开源协议
   - `setup.py`: 安装代码，[样例参考](https://github.com/hatlonely/qas/blob/master/setup.py)
3. 制作安装包，`python3 setup.py sdist`
4. 安装 twine，`pip3 install twine`
5. 上传到 pypi，`twine upload dist/*`

## 链接

- upload your python package to pypi: <https://towardsdatascience.com/how-to-upload-your-python-package-to-pypi-de1b363a1b3>
- 样例项目: <https://github.com/gmyrianthous/example-publish-pypi/blob/main/setup.py>
- 添加 requirements.txt 依赖: <https://stackoverflow.com/questions/6947988/when-to-use-pip-requirements-file-versus-install-requires-in-setup-py>
