# `objc_util` 写経しつつ理解する

# 📝 2023/01/09

最低限実行までやってみたい

そもそも、class 呼び出さないとだめか

## `ObjCClass` class

### `ObjCClass` コメント翻訳

Objective-Cクラスへのポインタのラッパーで、Objective-Cクラスのメソッドを呼び出すためのプロキシとして動作します。
> Wrapper for a pointer to an Objective-C class; acts as a proxy for calling Objective-C class methods.

メソッド呼び出しは、その場で Objective-C メッセージに変換されます。これは、メソッド名のアンダースコアをセレクタ名のコロンに置き換え、そのセレクタと引数を使用して Objective-C ランタイムの低レベルの Objc_msgSend 関数の呼び出しにセレクタと引数を使用します。例えば、 `NSDictionary.dictionaryWithObject_forKey_(obj, key)` (Python) を呼び出すと、 `[NSDictionary dictionaryWithObject:obj forKey:key]` (Objective-C) に変換されます。
> Method calls are converted to Objective-C messages on-the-fly -- this is done by replacing underscores in the method name with colons in the selector name, and using the selector and arguments for a call to the low-level objc_msgSend function in the Objective-C runtime. For example, calling `NSDictionary.dictionaryWithObject_forKey_(obj, key)` (Python) is translated to `[NSDictionary dictionaryWithObject:obj forKey:key]` (Objective-C).

メソッド呼び出しがObjective-Cオブジェクトを返す場合、それはObjCInstanceでラップされるので、呼び出しを連鎖させることができます（ObjCInstanceは同等のプロキシメカニズムを使用します）。
> If a method call returns an Objective-C object, it is wrapped in an ObjCInstance, so calls can be chained (ObjCInstance uses an equivalent proxy mechanism).

### Python class のコンストラクタ

# 📝 2022/10/24

## 方針

Python3 で実行できるように

## 書き捨て

- mac の環境をPythonista に揃えればよかったかも
- `pyparsing` をPython と環境揃えればよかったかも
