import tkinter as tk

root = tk.Tk()
root.minsize(270,330)
root.title("電卓")

def call(event,num):#数字用
    """ボタンを押してテキストエリアに表示する
    """
    text.insert(tk.END,num)

def call2(event,num):#演算子用
    """ボタンを押して一つ前が演算子で
    なかったらテキストエリアに表示する"""
    # テキストエリアの内容を取得して
    # 最後の1文字printしてみよう
    last_str = text.get()
    if len(last_str) > 0:
        # last_str[-1]が+,-,*,/でなければ
        # テキストエリアに演算子を表示する
        #in演算子便利
        if last_str[-1] not in ["+","-","*","/"]:
            text.insert(tk.END,num)

def clear(event,name):
    """テキストエリアを空にする
    """
    text.delete(0,tk.END)

def calc(event):
    """式を取得して画面に計算結果を出す
    """
    shiki = text.get()
    text.delete(0,tk.END)
    text.insert(tk.END,eval(shiki))
    # print(eval(shiki))#テキストボックスの式を表示
    # print(type(shiki))#文字列型

# 一段目
text = tk.Entry()
text.place(x=30, y=30, width=150,height=35)

btn_c = tk.Button(text="C",bg="#33cccc")
btn_c.bind("<1>",lambda event:clear(event,""))
btn_c.place(x=210, y=30, width=35,height=35)

# 二段目
btn_7 = tk.Button(text="7")
btn_7.bind("<1>",lambda event:call(event,"7"))
btn_7.place(x=30, y=90, width=35,height=35)

btn_8 = tk.Button(text="8")
btn_8.bind("<1>",lambda event:call(event,"8"))
btn_8.place(x=90, y=90, width=35,height=35)

btn_9 = tk.Button(text="9")
btn_9.bind("<1>",lambda event:call(event,"9"))
btn_9.place(x=150, y=90, width=35,height=35)

btn_waru = tk.Button(text="/",bg="#ffffff")
btn_waru.bind("<1>",lambda event:call2(event,"/"))
btn_waru.place(x=210, y=90, width=35,height=35)

# 三段目
btn_4 = tk.Button(text="4")
btn_4.bind("<1>",lambda event:call(event,"4"))
btn_4.place(x=30, y=150, width=35,height=35)

btn_5 = tk.Button(text="5")
btn_5.bind("<1>",lambda event:call(event,"5"))
btn_5.place(x=90, y=150, width=35,height=35)

btn_6 = tk.Button(text="6")
btn_6.bind("<1>",lambda event:call(event,"6"))
btn_6.place(x=150, y=150, width=35,height=35)

btn_kakeru = tk.Button(text="*",bg="#ffffff")
btn_kakeru.bind("<1>",lambda event:call2(event,"*"))
btn_kakeru.place(x=210, y=150, width=35,height=35)

# 四段目
btn_1 = tk.Button(text="1")
btn_1.bind("<1>",lambda event:call(event,"1"))
btn_1.place(x=30, y=210, width=35,height=35)

btn_2 = tk.Button(text="2")
btn_2.bind("<1>",lambda event:call(event,"2"))
btn_2.place(x=90, y=210, width=35,height=35)

btn_3 = tk.Button(text="3")
btn_3.bind("<1>",lambda event:call(event,"3"))
btn_3.place(x=150, y=210, width=35,height=35)

btn_mainasu = tk.Button(text="-",bg="#ffffff")
btn_mainasu.bind("<1>",lambda event:call2(event,"-"))
btn_mainasu.place(x=210, y=210, width=35,height=35)

# 五段目
btn_0 = tk.Button(text="0")
btn_0.bind("<1>",lambda event:call(event,"0"))
btn_0.place(x=30, y=270, width=35,height=35)

btn_d = tk.Button(text=".")
btn_d.bind("<1>",lambda event:call(event,"."))
btn_d.place(x=90, y=270, width=35,height=35)

btn_e = tk.Button(text="=",bg="#ffffff")
btn_e.bind("<1>",lambda event:calc(event))
btn_e.place(x=150, y=270, width=35,height=35)

btn_plus = tk.Button(text="+",bg="#ffffff")
btn_plus.bind("<1>",lambda event:call2(event,"+"))
btn_plus.place(x=210, y=270, width=35,height=35)

root.mainloop()