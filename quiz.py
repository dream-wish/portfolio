"""
moshi.csvから模試データを読み込み
Tkinterで表示
"""
import tkinter as tk
import random as r
import csv

root = tk.Tk()
root.minsize(800,600)
root.title("クイズアプリ")
canvas = tk.Canvas(root)
frame = tk.Frame(canvas)

#問題数をカウントする変数
count_q = 0

# 正解数をカウントする変数
count_seikai = 0

#ここから問題を作るのでいったんCSV系の作業に入ります
# 初期設定
# seikai = 0
dict_1 = {}
dict_2 = {}

# Canvasを親とした縦方向のScrollbar
scrollbar = tk.Scrollbar(
    canvas, orient=tk.VERTICAL, command=canvas.yview
)

# スクロールの設定
canvas.configure(scrollregion=(0, 0, 900, 5000))
canvas.configure(yscrollcommand=scrollbar.set)

# 諸々を配置
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.pack(expand=True, fill=tk.BOTH)

# Canvas上の座標(0, 0)に対してFrameの左上（nw=north-west）をあてがうように、Frameを埋め込む
canvas.create_window((0, 0), window=frame, anchor="nw", width=900, height=5000)

with open("moshi.csv","r") as fp:

# reader = csv.reader(fp)
# print(type(reader))#csvリーダー型ができる

    for val in csv.reader(fp):
        dict_sentaku = {}
        """田頭
        これをwithopenの外からここに移動しました。
        for文内で初期化しないと最後の答えが全部の辞書に入ってしまってます。
        （何でそうなるのかよくわからない）"""
        # print(val[0])
        #一つ目の辞書（問題文と選択肢）
        dict_sentaku["A"] = val[1]
        dict_sentaku["B"] = val[2]
        dict_sentaku["C"] = val[3]
        # print(dict_sentaku["B"])
        # 選択肢の文字数によって改行を入れる
        if len(dict_sentaku["A"]) > 15:
            dict_sentaku["A"] = dict_sentaku["A"][:25] + "\n" + dict_sentaku["A"][25:]
        if len(dict_sentaku["B"]) > 15:
            dict_sentaku["B"] = dict_sentaku["B"][:25] + "\n" + dict_sentaku["B"][25:]
        if len(dict_sentaku["C"]) > 15:
            dict_sentaku["C"] = dict_sentaku["C"][:25] + "\n" + dict_sentaku["C"][25:]
            # print(dict_sentaku["B"])
        dict_1[val[0]] = dict_sentaku
        # print(dict_1[val[0]])
        #二つ目の辞書（問題文と正解）
        if len(val[4]) > 15:
            dict_2[val[0]] = val[4][:25] + "\n" + val[4][25:]
        else:
            dict_2[val[0]] = val[4]
print(dict_1)

# #dict1のキーからランダムに10問出題リストを作る 
q_list = r.sample(list(dict_1.keys()), 10) 

# #ユーザーの解答を入れるリスト 
ans = [] 

#出題するのでTkinterに戻ります
def change_q():
    #問題が10問終わったら画面切り替える（ここは作ってない）
    if count_q < 10:
        count_label["text"] = count_q+1
        qes_label["text"] = q_list[count_q]
        # ↑ラベル型["text"]でラベルの中身を書き換えられます
        #問題文を書き換えたので選択肢も書き換えましょう
        btn_a["text"] = dict_1[q_list[count_q]]["A"]
        btn_b["text"] = dict_1[q_list[count_q]]["B"]
        btn_c["text"] = dict_1[q_list[count_q]]["C"]
    else:
        print("おわり")
        go_saiten()
        #ここに採点系のプログラム組み込む

def get_entry(choice):
    """解答を受け取って処理"""
    global ans,count_q
    ans.append(choice)
    #問題数をカウントアップ
    count_q += 1
    #ユーザーが選んだ問題をリストに入れた後に、問題文を書き換える
    change_q()

def go_saiten():
    """採点画面に進む"""
    global count_label,qes_label,btn_a,btn_b,btn_c
    #まず消す
    count_label.destroy()
    qes_label.destroy()
    btn_a.destroy()
    btn_b.destroy()
    btn_c.destroy()
    #次に生む
    make_saiten()

def make_saiten():
    """採点画面を表示"""
    global count_seikai
    #何問正解したか入れるリスト 
    count = [] 
    # place場所リスト
    mondai_basho_x = [10,10,10,10,10,10,10,10,10,10]
    mondai_basho_y = [10,400,790,1180,1570,1960,2350,2740,3130,3520]
    kaitou_basho_x = [10,10,10,10,10,10,10,10,10,10]
    kaitou_basho_y = [160,550,940,1330,1720,2110,2500,2890,3280,3670]
    sentaku_basho_x = [10,10,10,10,10,10,10,10,10,10]
    sentaku_basho_y = [190,580,970,1360,1750,2140,2530,2920,3310,3700]
    seikai_1_basho_x = [10,10,10,10,10,10,10,10,10,10]
    seikai_1_basho_y = [275,665,1055,1445,1835,2225,2615,3005,3395,3785]
    seikai_2_basho_x = [10,10,10,10,10,10,10,10,10,10]
    seikai_2_basho_y = [370,760,1150,1540,1930,2320,2710,3100,3490,3880]
    fuseikai_basho_x = [10,10,10,10,10,10,10,10,10,10]
    fuseikai_basho_y = [370,760,1150,1540,1930,2320,2710,3100,3490,3880]
    ichiran_basho_x = [250,280,310,340,370,400,430,460,490,520]
    ichiran_basho_y = [4075,4075,4075,4075,4075,4075,4075,4075,4075,4075]
    for i in range(len(ans)):
        #問題文を取得 
        print(q_list[i])
        mondai = tk.Label(frame, text=q_list[i],
                            font=("",20,""),
                            wraplength=740,
                            justify=tk.LEFT)
        mondai.place(x=mondai_basho_x[i],y=mondai_basho_y[i])
        #ユーザーの解答（アルファベットと選択した文字列）を表示 
        print(f"解答{ans[i]}")
        kaitou = tk.Label(frame, text=f"解答「{ans[i]}」",
                            font=("",20,""),
                            wraplength=740,
                            justify=tk.LEFT)
        kaitou.place(x=kaitou_basho_x[i],y=kaitou_basho_y[i])
        print(f"選択した文字列{dict_1[q_list[i]][ans[i]]}")
        sentaku = tk.Label(frame, text=f"選択した文字列「{dict_1[q_list[i]][ans[i]]}」",
                            font=("",20,""),
                            wraplength=740,
                            justify=tk.LEFT)
        sentaku.place(x=sentaku_basho_x[i],y=sentaku_basho_y[i])
        print(f"正解{dict_2[q_list[i]]}")
        seikai_1 = tk.Label(frame, text=f"正解「{dict_2[q_list[i]]}」",
                            font=("",20,""),
                            wraplength=740,
                            justify=tk.LEFT)
        seikai_1.place(x=seikai_1_basho_x[i],y=seikai_1_basho_y[i])
        #正解判定（変数に入れてもいいよ） 
        if dict_1[q_list[i]][ans[i]] == dict_2[q_list[i]]: 
            print("正解")
            seikai_2 = tk.Label(frame, text="正解",
                            font=("",20,""),
                            wraplength=740,
                            justify=tk.LEFT,
                            foreground="#0000ff")
            seikai_2.place(x=seikai_2_basho_x[i],y=seikai_2_basho_y[i]) 
            count.append("〇")
            count_seikai += 1
        else: 
            print("不正解") 
            fuseikai = tk.Label(frame, text="不正解",
                                font=("",20,""),
                                wraplength=740,
                                justify=tk.LEFT,
                                foreground="#ff0000")
            fuseikai.place(x=fuseikai_basho_x[i],y=fuseikai_basho_y[i])
            count.append("×") 
    
    # 最後に成績を表示 
    print(count)
    # print(f"{count_seikai}0点")
    # if count_seikai >= 7:
    #     print("合格")
    # else:
    #     print("不合格")
    # for r, c in zip(range(1, 11), count):
    #     print(f"{r}\n{c}")
    kekka = tk.Label(frame, text="採点結果",font=("",20,""))
    kekka.place(x=325,y=3930)

    saiten = tk.Label(frame, text=f"{count_seikai}0点",
                            font=("",20,""),
                            wraplength=740,
                            justify=tk.LEFT)
    saiten.place(x=350,y=3975)
    if count_seikai >= 7:
        goukaku = tk.Label(frame, text="合格",
                            font=("",25,""),
                            wraplength=740,
                            justify=tk.LEFT)
        goukaku.place(x=345,y=4025)
    else:
        fugoukaku = tk.Label(frame, text="不合格",
                            font=("",25,""),
                            wraplength=740,
                            justify=tk.LEFT)
        fugoukaku.place(x=330,y=4025)
    for r, c, r_2 in zip(range(1, 11), count, range(10)):
        ichiran = tk.Label(frame, text=(f"{r}\n{c}"),
                            font=("",20,""),
                            wraplength=740,
                            justify=tk.LEFT)
        ichiran.place(x=ichiran_basho_x[r_2],y=ichiran_basho_y[r_2])
#現在の問題番号を入れる
count_label = tk.Label(text=count_q+1,font=("",20,""))
count_label.place(x=10,y=10)

#問題文を表示するラベルを作成
#wraplengthで740pxで自動改行
#justifyで左寄せ
qes_label = tk.Label(text=q_list[count_q],
                          font=("",20,""),
                          wraplength=740,
                          justify=tk.LEFT)
qes_label.place(x=10,y=45)

# 選択肢を乗っけるボタンを作成(3つ)
# ボタンを押すと次の問題に進む、リストに選択肢を代入して
# if dict_1[q_list[count_q]]["A"] == "1":
#     button = tk.Button(image=img_resize_1,
#                        command=lambda:get_entry("A"))
#     button.place(x=10,y=150)
size=20 #デフォルトの文字サイズ(選択肢が長い場合は変更できるといい)
btn_a = tk.Button(text=dict_1[q_list[count_q]]["A"],
                       width=50,font=("",size,""),
                       command=lambda:get_entry("A"),
                       justify=tk.LEFT)
btn_a.place(x=10,y=150)

btn_b = tk.Button(text=dict_1[q_list[count_q]]["B"],
                       width=50,font=("",size,""),
                       command=lambda:get_entry("B"),
                       justify=tk.LEFT)
btn_b.place(x=10,y=230)

btn_c = tk.Button(text=dict_1[q_list[count_q]]["C"],
                       width=50,font=("",size,""),
                       command=lambda:get_entry("C"),
                       justify=tk.LEFT)
btn_c.place(x=10,y=310)

#終わったらユーザーの解答を出力してみる 
print(ans)

root.mainloop()