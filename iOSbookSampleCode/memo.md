# 📝 2022/10/10

## `AVAudioRecorder` の`settings`

`enum.Enum` だと読み込めない？class のスタテック変数で指定してみている


## `.wav` の読み込み


`scipy` がないので、Pythonista で使えるモノで読み込み


- `wave` モジュール
  - こっちで進める
    - `getframerate` と`readframes` で、バイトデータを整理できる
- `pathlib` モジュール
  - 使わない
    - `read_bytes` だと、header 情報もまとめて持って来てしまう
    - フレームレートやらチャンネルやら、フレキシブルに使えないと思う

### `wavfile.read` 調査

[scipy/wavfile.py at main · scipy/scipy](https://github.com/scipy/scipy/blob/main/scipy/io/wavfile.py)


`wave` モジュールで進めるにあたり、ステレオ16bit の決め打ちで読み出してる
