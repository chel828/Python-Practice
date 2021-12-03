from tkinter import *
from tkinter import ttk

#クラスを作成。
class busyou:
    #関数を定義。
    def start():
        #インポート文
        import random as r
        import tkinter,tkinter.messagebox

        #tkinterの初期化
        root = tkinter.Tk()
        root.withdraw()

        #メッセージボックスの表示
        tkinter.messagebox.showinfo(title = "あなたと相性が良い日本の侍を、独断と偏見で占います。",
        message = "下のボタンを押してください。")

        #占い結果リスト
        characters = [ "織田信長" , "武田信玄" , "豊臣秀吉" , "上杉謙信" , "土方歳三" , "明智光秀" , "伊達政宗" , "真田幸村" , "沖田総司" , "石田三成" , "黒田官兵衛" ]

        #リストからランダムで選ぶ
        character = r.choice(characters)

        #結果を表示する
        tkinter.messagebox.showinfo( title = "いざ、結果発表に参る！！！！" ,
        message = "あなたと相性がいいお侍さんは\n"+ character +"です。\nもし、タイムスリップした時は、会いに行ってみてくださいね！")

        #終わりの挨拶
        tkinter.messagebox.showinfo( title = "次へ参ろう！" , 
        message = "煮えてなんぼの、おでんに候！！！！")

        #自動的に閉じる