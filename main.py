import tkinter
from tkinter import font
import strings

root = tkinter.Tk()

# Windowのタイトル
root.title("Window Title")

# Windowサイズの指定
root.geometry("1010x1010")

# 文字を配置する。
label1 = tkinter.Label(root, text="Hallo")
label1.pack(side="top")

text = "test"
ftMain = font.Font(family='Helvetica', size=20, weight='bold')
font1 = font.Font(family='Helvetica', size=20, weight='bold')
label2 = tkinter.Label(root, text=text, bg="blue", font=font1)
label2.pack(side="top")


# text viewの略
tvSampleBg = "red"
tvSampleFg = "blue"

tvSampleLabel = tkinter.Label(
  root,
  text=strings.tvSample,
  fg=tvSampleFg,
  bg=tvSampleBg,
  font=ftMain)

tvSampleLabel.pack(side=tkinter.TOP)

font2 = font.Font(family='Times', size=40)
label2 = tkinter.Label(root, text="See you", fg="red", font=font2)
label2.pack(side="top")

# 画面の下部にステータスバーを追加する
status = tkinter.Label(root, text="Now processing..", borderwidth=2, relief="groove")
status.pack(side=tkinter.BOTTOM, fill=tkinter.X)

# 実行
root.mainloop()