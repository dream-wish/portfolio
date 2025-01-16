import tkinter as tk
import requests
import json
from datetime import date

#画面作成
root = tk.Tk()
root.minsize(400,300)
root.title("今日の占い")

#関数
#占い結果を取得する関数を作る
def get_uranai(num):
    """引数で受け取ったの星座の結果を辞書型で取得してprintする関数"""
    #今日の日付を取得(yyyy-mm-dd)
    today = str(date.today()).replace("-","/")
    res = requests.get(f"http://api.jugemkey.jp/api/horoscope/free/{today}")
    result = json.loads(res.text)
    # print(result['horoscope'][today][num])
    view_uranai(result['horoscope'][today][num])

def view_uranai(dic):
    """辞書型の引数を受け取り内容を画面に表示"""
    global name,text1,text2,text3,text4,text5,text6,text7
    name = tk.Label(text=dic["sign"],font=("",13,""))
    name.pack(pady=5)
    text1 = tk.Text(width=50,height=4)
    text1.insert(tk.END,dic["content"])
    text1.pack(pady=3)
    love = "★" * dic["love"]
    text2 = tk.Label(text=f"恋愛運:{love}")
    text2.pack()
    money = "★" * dic["money"]
    text3 = tk.Label(text=f"金運:{money}")
    text3.pack()
    job = "★" * dic["job"]
    text4 = tk.Label(text=f"仕事運:{job}")
    text4.pack()
    total = "★" * dic["total"]
    text5 = tk.Label(text=f"全体運:{total}")
    text5.pack()
    item = f"ラッキーアイテム:{dic['item']}"
    text6 = tk.Label(text=item)
    text6.pack()
    color = f"ラッキーカラー:{dic['color']}"
    text7 = tk.Label(text=color)
    text7.pack()
    make_return() 

def make_return():
    """戻るボタンを表示する"""
    global back
    back = tk.Button(text="戻る")
    back.bind("<1>",back_main)
    back.pack()

def back_main(event):
    """スタート画面に戻る"""
    global name,text1,text2,text3,text4,text5,text6,text7,back
    #まず消す
    name.destroy()
    text1.destroy()
    text2.destroy()
    text3.destroy()
    text4.destroy()
    text5.destroy()
    text6.destroy()
    text7.destroy()
    back.destroy()
    #次に生む
    make_btn()


def make_btn():
    global btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12,btn_list
    btn1 = tk.Button(text="おひつじ座",font=("",14,""),width=10)
    btn1.bind("<1>",lambda event:clear_btn(event,0))
    btn1.place(x=10,y=50)
    btn2 = tk.Button(text="おうし座",font=("",14,""),width=10)
    btn2.bind("<1>",lambda event:clear_btn(event,1))
    btn2.place(x=143,y=50)
    btn3 = tk.Button(text="ふたご座",font=("",14,""),width=10)
    btn3.bind("<1>",lambda event:clear_btn(event,2))
    btn3.place(x=283,y=50)

    btn4 = tk.Button(text="かに座",font=("",14,""),width=10)
    btn4.bind("<1>",lambda event:clear_btn(event,3))
    btn4.place(x=10,y=100)
    btn5 = tk.Button(text="しし座",font=("",14,""),width=10)
    btn5.bind("<1>",lambda event:clear_btn(event,4))
    btn5.place(x=143,y=100)
    btn6 = tk.Button(text="おとめ座",font=("",14,""),width=10)
    btn6.bind("<1>",lambda event:clear_btn(event,5))
    btn6.place(x=283,y=100)

    btn7 = tk.Button(text="てんびん座",font=("",14,""),width=10)
    btn7.bind("<1>",lambda event:clear_btn(event,6))
    btn7.place(x=10,y=150)
    btn8 = tk.Button(text="さそり座",font=("",14,""),width=10)
    btn8.bind("<1>",lambda event:clear_btn(event,7))
    btn8.place(x=143,y=150)
    btn9 = tk.Button(text="いて座",font=("",14,""),width=10)
    btn9.bind("<1>",lambda event:clear_btn(event,8))
    btn9.place(x=283,y=150)

    btn10 = tk.Button(text="やぎ座",font=("",14,""),width=10)
    btn10.bind("<1>",lambda event:clear_btn(event,9))
    btn10.place(x=10,y=200)
    btn11 = tk.Button(text="みずがめ座",font=("",14,""),width=10)
    btn11.bind("<1>",lambda event:clear_btn(event,10))
    btn11.place(x=143,y=200)
    btn12 = tk.Button(text="うお座",font=("",14,""),width=10)
    btn12.bind("<1>",lambda event:clear_btn(event,11))
    btn12.place(x=283,y=200)

    #ボタン型が入ったリストを作る（消す時便利）
    btn_list = [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12]


#ボタンを全部消す関数
def clear_btn(event,num):
    global btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12,btn_list
    for val in btn_list:
        val.destroy()
    
    # 占い結果を表示する関数を呼び出す
    get_uranai(num)
    


#ずっと出てる文字
text = tk.Label(text="今日の占い",font=("",14,""),fg="#336699")
text.pack(pady=5)



#ボタン類生み出す
make_btn()

root.mainloop()


# import tkinter as tk
# import requests
# import json
# from datetime import date

# root = tk.Tk()
# root.minsize(270,330)
# root.title("占い")

# #関数
# #占い結果を取得する関数を作る
# def get_uranai(num):
#     """引数で受け取った星座（どれでもいい）の結果を辞書型
#     で取得してprintする関数"""
#     #今日の日付を取得(yyyy-mm-dd)
#     today = str(date.today()).replace("-","/")
#     res = requests.get(f"https://api.jugemkey.jp/api/horoscope/free/{today}")
#     result = json.loads(res.text)
#     # print(result["horoscope"][today][num])
#     view_uranai(result["horoscope"][today][num])

# def view_uranai(dic):
#     """辞書型の引数を受け取り内容を画面に表示"""
#     # print(dic["content"])
#     global name,text1,item,i_text
#     name = tk.Label(text=dic["sign"],font=("",13,""))
#     name.pack(pady=5)
#     text1 = tk.Text(width=50,height=4)
#     text1.insert(tk.END,dic["content"])
#     text1.pack(pady=3)
#     #(あとで結果を足そう)
#     item = tk.Label(text="アイテム",font=("",13,""))
#     item.pack(pady=5)
#     i_text = tk.Text(width=20,height=1)
#     i_text.insert(tk.END,dic["item"])
#     i_text.pack(pady=3)
    
#     item = tk.Label(text="アイテム",font=("",13,""))
#     item.pack(pady=5)
#     i_text = tk.Text(width=20,height=1)
#     i_text.insert(tk.END,dic["item"])
#     i_text.pack(pady=3)
#     make_return()

# def make_return():
#     """戻るボタンを表示する"""
#     global back
#     back = tk.Button(text="戻る")
#     back.bind("<1>",back_main)
#     back.pack()

# def back_main(event):
#     """スタート画面に戻る"""
#     global name,text1,back,item,i_text
#     #まず消す
#     name.destroy()
#     text1.destroy()
#     back.destroy()
#     item.destroy()
#     i_text.destroy()
#     #次に生む
#     make_btn()

# def make_btn():
#     global text,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12,btn_list
#     text = tk.Label(text="占い")
#     text.pack()
#     btn1 = tk.Button(text="牡羊座")
#     btn1.bind("<1>",lambda event:clear_btn(event,0))
#     btn1.place(x=30, y=90, width=35,height=35)

#     btn2 = tk.Button(text="牡牛座")
#     btn2.bind("<1>",lambda event:clear_btn(event,1))
#     btn2.place(x=90, y=90, width=35,height=35)

#     btn3 = tk.Button(text="双子座")
#     btn3.bind("<1>",lambda event:clear_btn(event,2))
#     btn3.place(x=150, y=90, width=35,height=35)

#     btn4 = tk.Button(text="蟹座")
#     btn4.bind("<1>",lambda event:clear_btn(event,3))
#     btn4.place(x=210, y=90, width=35,height=35)

#     btn5 = tk.Button(text="獅子座")
#     btn5.bind("<1>",lambda event:clear_btn(event,4))
#     btn5.place(x=30, y=150, width=35,height=35)

#     btn6 = tk.Button(text="乙女座")
#     btn6.bind("<1>",lambda event:clear_btn(event,5))
#     btn6.place(x=90, y=150, width=35,height=35)

#     btn7 = tk.Button(text="天秤座")
#     btn7.bind("<1>",lambda event:clear_btn(event,6))
#     btn7.place(x=150, y=150, width=35,height=35)

#     btn8 = tk.Button(text="蠍座")
#     btn8.bind("<1>",lambda event:clear_btn(event,7))
#     btn8.place(x=210, y=150, width=35,height=35)

#     btn9 = tk.Button(text="射手座")
#     btn9.bind("<1>",lambda event:clear_btn(event,8))
#     btn9.place(x=30, y=210, width=35,height=35)

#     btn10 = tk.Button(text="山羊座")
#     btn10.bind("<1>",lambda event:clear_btn(event,9))
#     btn10.place(x=90, y=210, width=35,height=35)

#     btn11 = tk.Button(text="水瓶座")
#     btn11.bind("<1>",lambda event:clear_btn(event,10))
#     btn11.place(x=150, y=210, width=35,height=35)

#     btn12 = tk.Button(text="魚座")
#     btn12.bind("<1>",lambda event:clear_btn(event,11))
#     btn12.place(x=210, y=210, width=35,height=35)

#     #ボタン型が入ったリストを作る（消すとき便利）
#     btn_list = [text,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12]
    
# # ボタンを全部消す関数
# def clear_btn(event,num):
#     global text,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12,btn_list
#     # text.destroy()
#     # btn1.destroy()
#     # btn2.destroy()
#     # btn3.destroy()
#     # btn4.destroy()
#     # btn5.destroy()
#     # btn6.destroy()
#     # btn7.destroy()
#     # btn8.destroy()
#     # btn9.destroy()
#     # btn10.destroy()
#     # btn11.destroy()
#     # btn12.destroy()
#     for val in btn_list:
#         val.destroy()
    
#     #占い結果を表示する関数を呼び出す
#     get_uranai(num)

# #ボタン類
# make_btn()

# root.mainloop()