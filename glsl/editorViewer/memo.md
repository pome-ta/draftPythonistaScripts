# editorViewer

glsl の Shader コードを編集してるところから、Pythonista のショートカットを使って呼び出し

外部ファイルからショートカット登録ができないみたいで、github との連携は少し面倒

# ShaderCodes

正規化の呼び出しが、変に事前処理で

``` .glsl
v_tex_coord = (gl_FragCoord.xy) / resolution.xy;
```

こんな感じになってる可能性あり

正規化あきらめか？
