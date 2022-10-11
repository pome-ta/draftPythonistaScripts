# 📝 2022/10/11

## `scipy` の`signal.spectrogram`

めんどくさそうだから、ペンディング


## モーション関係の`CMMotionManager`

### `startAccelerometerUpdatesToQueue_withHandler_` の内部

[startAccelerometerUpdatesToQueue:withHandler: | Apple Developer Documentation](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616148-startaccelerometerupdatestoqueue)

[CMAccelerometerHandler | Apple Developer Documentation](https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler?language=objc)


- `NSOperationQueue`
  - `NSOperationQueue.mainQueue()`
    - `NSOperationQueue.currentQueue()` は`null` だった
  - 単純に突っ込めば良さそう
- `CMAccelerometerHandler`
  - `Type Alias` だから深掘り
  - `CMAccelerometerData`

`block` 使う、、、

> CMAccelerometerHandler型のブロックは、処理すべき加速度センサーのデータがあるときに呼び出される。startAccelerometerUpdatesToQueue:withHandler:に第2引数としてこのブロックを渡す。このタイプのブロックは値を返さないが、2つの引数を取る。


### プル型とプッシュ型？

[加速度センサとジャイロで体の動きを感じるアプリを作る（1/3） - ＠IT](https://atmarkit.itmedia.co.jp/fsmart/articles/ios_sensor02/01.html)


[startAccelerometerUpdates | Apple Developer Documentation](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616171-startaccelerometerupdates?language=objc)



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

