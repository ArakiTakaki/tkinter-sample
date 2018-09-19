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
