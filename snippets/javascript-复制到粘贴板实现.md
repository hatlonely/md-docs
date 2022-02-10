# javascript 复制到粘贴板实现

[//]: <> (javascript, clipboard)

剪切板默认只能从 input 元素中获取，通过创建一个临时的不可见 input 元素，可以实现任意元素的内容复制，input 元素选择 textarea 是因为其可以支持换行

```js
function copyToClipboard(elementId) {
    var aux = document.createElement("textarea");
    aux.value = document.getElementById(elementId).textContent;
    aux.style.height = "0";
    aux.style.overflow = "hidden";
    aux.style.position = "fixed";
    document.body.appendChild(aux);
    aux.select();
    document.execCommand("copy");
    document.body.removeChild(aux);
}
```

在 button 中注册点击事件即可

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

## 参考

- How to easily copy text to clipboard with JavaScript: <https://cravencode.com/post/javascript/copy-text-to-clipboard/>
