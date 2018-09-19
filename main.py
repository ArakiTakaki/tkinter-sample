import tkinter
from tkinter import font

root = tkinter.Tk()

# Windowのタイトル
root.title("Window Title")

# Windowサイズの指定
root.geometry("1010x1010")

# 文字を配置する。
label1 = tkinter.Label(root, text="Hallo")
label1.pack(side="top")

font1 = font.Font(family='Helvetica', size=20, weight='bold')
label2 = tkinter.Label(root, text="Bye", bg="blue", font=font1)
label2.pack(side="top")

font2 = font.Font(family='Times', size=40)
label2 = tkinter.Label(root, text="See you", fg="red", font=font2)
label2.pack(side="top")

# 実行
root.mainloop()