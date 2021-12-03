#クラスを作成。
class onepiece2:
    #関数を定義。
    def start():
        #インポート文
        import random as r
        import tkinter,tkinter.messagebox

        #tkinterの初期化
        root = tkinter.Tk()
        root.withdraw()

        #メッセージボックスの表示
        tkinter.messagebox.showinfo(title = "おすすめのONE PIECEは…！",
        message = "下のボタンを押してください。")

        #占い結果リスト
        characters = [ "1－3巻（東の海／オレンジの町編）" , "5-8巻（バラティエ編）" , "8-11巻（アーロンパーク編）" , "15-17巻（ドラム王国編）" ,
        "17-23巻（アラバスタ編）" , "32-46巻（ウォーターセブン／エニエス・ロビー編）" , "56-61巻（頂上戦争／マリンフォード編）" , 
        "70-80巻（ドレスローザ編）" , "82-90巻（ホールケーキアイランド編）" , "90-X巻（ワノ国編）" , "46-50巻（スリラーバーク編）" ,
        "66-70巻（パンクハザード編）" , "54-56巻（インペルダウン編）" , "61-66巻（魚人島編）" , "24-32巻（空島編）" ]

        #リストからランダムで選ぶ
        character = r.choice(characters)

        #結果を表示する
        tkinter.messagebox.showinfo( title = "いざ、出航だー！！！！" ,
        message = "あなたに読んでほしい、とーーーーーーってもおススメのONE PIECEは、\n" + character + "です！\nONE PIECEは、大人になってから読むと、視点が変わって、面白さが\n一段と上がります♡\nぜひぜひ、この機会に、読んでみてくださいね♪")

        #終わりの挨拶
        tkinter.messagebox.showinfo( title = "それでは、また来てくださいね！" , 
        message = "人は”心”だろうが！！！！")

        #自動的に閉じる
