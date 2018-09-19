# tkinter-sample

## 文字を配置する

`tkinter.Label(Tk)`

| 引数 | 型     | メソッド           |
| :--- | :----- | :----------------- |
| font | font   | フォントの設定     |
| text | string | 表示テキストの設定 |
| fg   | string | フォントの色       |
| bg   | string | backgroundの色     |

`tinker.Label().pack()`

| 引数 | 型     | メソッド           |
| :--- | :----- | :----------------- |
| side | string   | 配置場所(top,right,bottom,left)     |

`from tkinter import font`

`font.Font`

| 引数   | 型     | メソッド |
| :----- | :----- | :------- |
| family | string | フォント |
| size   | int    | 大きさ   |
| weight | string | 太さ     |

## 文字を表示するsample_code

```python3
import tkinter
from tkinter import font

root = tkinter.Tk()
root.title("sample window")
root.geomer("600x400")

# text viewの略
tvSampleText = "sample text"
tvSampleBg = "red"
tvSampleFg = "blue"

# fontの略
ftMainFontFamily = "Helvetica"
ftMainSize = 20
ftMainWeight = "bold"

ftMain = font.Font(
  family=ftMainFontFamily,
  size=ftMainSize,
  weight=ftMainWeight)

tvSampleLabel = tkinter.Label(
  root,
  text=tvSampleText,
  fg=tvSampleFg,
  bg=tvSampleBg,
  font=ftMain)

tvSampleLabel.pack(side=tkinter.TOP)

root.mainloop()
```

tips

- 直接指定も可能であるが、基本的に`tvSampleText`という形で設定ファイルを分割してあげると保守性が上がる？
- MacOSの場合Helveticaが美しいので、おすすめ