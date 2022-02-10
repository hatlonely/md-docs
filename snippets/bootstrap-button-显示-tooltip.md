# bootstrap button 显示 tooltip

[//]: <> (bootstrap, button, tooltip)

出于性能问题，bootstrap 需要手动开启 tooltip 功能

在 html 的 body 后面加上如下代码即可给所有的元素都开启 tooltip 功能

**注意** 要等所有元素都加载之后才能执行，否则不能生效，这也是为什么要放到 body 后面执行

```js
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="top" title="Tooltip on top">
  Tooltip on top
</button>
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="right" title="Tooltip on right">
  Tooltip on right
</button>
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Tooltip on bottom">
  Tooltip on bottom
</button>
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="left" title="Tooltip on left">
  Tooltip on left
</button>

<script>
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
    })
</script>
```

## 链接

- bootstrap tooltips: <https://getbootstrap.com/docs/5.1/components/tooltips/>
