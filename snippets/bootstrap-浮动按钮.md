# bootstrap 浮动按钮

[//]: <> (bootstrap, float, button)

`float-end` 类可以创建一个浮动的块，在块中加入按钮即可

```html
<div class="card-body">
    <div class="float-end">
        <button type="button" class="btn btn-sm py-0" onclick="copyToClipboard('{{ name }}-res')"
            data-bs-toggle="tooltip" data-bs-placement="top" title="复制">
            <i class="bi-clipboard"></i>
        </button>
    </div>
    <pre id="{{ name }}-res">{{ format_sub_step_res(sub_step) }}</pre>
</div>
```

## 链接

- bootstrap float <https://getbootstrap.com/docs/5.1/utilities/float/>
