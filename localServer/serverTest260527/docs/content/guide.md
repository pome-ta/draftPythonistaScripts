# Guide: `guide.md`




```inject
<div style="padding: 1rem; background: #e0f2fe; border-radius: 8px;">
  <p>がいどここは直接書いたHTMLです！</p>
  <button id="my-btn">がいどクリックしてね</button>
</div>

<script>
  // DOMが展開された直後に実行されます
  document.getElementById('my-btn').addEventListener('click', () => {
    alert('がいどMarkdown内に書かれたJSが実行されました！');
  });
</script>
```
