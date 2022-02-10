# python3 html 模板渲染

[//]: <> (python3, jinja2, html, template)

jinja2 是一个优秀的模板渲染库

使用如下命令安装

```shell
pip3 install Jinja2
```

基本用法

```python
class TestJinja(unittest.TestCase):
    def test_jinja(self):
        tpl = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>My Webpage</title>
        </head>
        <body>
            <ul id="navigation">
            {% for item in navigation %}
                <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
            {% endfor %}
            </ul>

            <h1>My Webpage</h1>
            {{ a_variable }}

            {# a comment #}
        </body>
        </html>
        """

        template = Environment(loader=BaseLoader).from_string(tpl)
        data = template.render(navigation=[{
            "href": "href1",
            "caption": "caption1",
        }, {
            "href": "href2",
            "caption": "caption2",
        }], a_variable="hello world")
        print(data)
```

可以在 env 中增加自定义函数

```python
env = Environment(loader=BaseLoader)
env.globals.update(format_timedelta=HtmlReporter.format_timedelta)
env.globals.update(hashlib=hashlib)
env.globals.update(json=json)
env.globals.update(render_test=self.render_test)
env.globals.update(render_case=self.render_case)
env.globals.update(render_step=self.render_step)
env.globals.update(render_sub_step=self.render_sub_step)
env.globals.update(format_sub_step_res=HtmlReporter.format_sub_step_res)
env.globals.update(len=len)
env.globals.update(brief_mode=True)
env.globals.update(markdown=markdown.markdown)
self.report_tpl = env.from_string(_report_tpl)
self.test_tpl = env.from_string(_test_tpl)
self.case_tpl = env.from_string(_case_tpl)
self.step_tpl = env.from_string(_step_tpl)
self.sub_step_tpl = env.from_string(_sub_step_tpl)
```

通过设置自定义函数，可以实现，递归渲染

```python
tpl = """key: {{ val.key }}
{% for sub in val.subs %}
{% print(render(sub)) %}
{% endfor %}
"""


class TestJinja2(unittest.TestCase):
    def setUp(self) -> None:
        env = Environment(loader=BaseLoader)
        env.globals.update(render=self.render)
        self.template = env.from_string(tpl)

    def render(self, val):
        return "\n".join(["  " + line for line in self.template.render(val=val).split("\n")])

    def test_recursive(self):
        res = self.template.render(val={
            "key": "val1",
            "subs": [{
                "key": "val2",
                "subs": [{
                    "key": "val3",
                }]
            }, {
                "key": "val4",
                "subs": [{
                    "key": "val5"
                }, {
                    "key": "val6"
                }]
            }]
        })
        print(res)
```

## 链接

- 官网: <https://jinja.palletsprojects.com/en/latest/>
