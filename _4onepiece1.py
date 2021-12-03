#クラスを作成。
class onepiece1:
    #関数を定義。
    def start():
        #インポート文
        import random as r
        import tkinter,tkinter.messagebox


        def confirm_retry():
            """もう1度行うかどうかを確認"""
            while True:
                n = int(input('もう一度？ Yes ▷▷ 1 / No ▷▷ 0：'))
                if n == 0 or n == 1:
                    return n

        print('ワンピース敵キャラ相性診断開始！')

        #tkinterの初期化
        root = tkinter.Tk()
        root.withdraw()

        #メッセージボックスの表示
        tkinter.messagebox.showinfo(title = "あなたと相性が良いキャラは…！",
        message = "下のボタンを押してください。")

        #占い結果リスト
        characters = [ "シャーロット・クラッカー" , "ドンキホーテ・ドフラミンゴ" , "ビッグマム" , "アーロン" , "赤犬" , "モンキー・D・ガープ" , "マーシャル・D・ティーチ" , "藤虎" ,
        "セニョール・ピンク" , "ヴェルゴ" , "ホーディ・ジョーンズ" , "mミス・バレンタイン" , "モネ" , "シュガー" , "スパンダム" , "戦桃丸" , "ジュラキュール・ミホーク" , "ワポル" , "ジャック" ,
        "黒炭オロチ" , "カイドウ" , "バギー" , "サー・クロコダイル" , "黄猿" , "ブラックマリア" , "うるティ" , "エネル" , "シーザー・クラウン" , "ゲッコー・モリア" , "ハンニャバル" ,
        "モーガン" , "クロ" , "Mr.3" , "ボンクレー" , "ドン・クリーク" , "ベラミー" , "バジル・ホーキンス" , "ブルーノ" , "ロブ・ルッチ" , "オーズ" , "マゼラン" , "バンダー・ゼッケン九世" ]

        #リストからランダムで選ぶ
        character = r.choice(characters)

        #結果を表示する
        tkinter.messagebox.showinfo( title = "いざ、出航だー！！！！" ,
        message = "あなたと相性がいいワンピースの敵キャラは、\n"+ character + "です。\nもうすぐHalloween♪ということで…。\n一緒に悪いことをしてみると、あなたも何かに目覚めてしまうかも\nしれませんね☆")

        #終わりの挨拶
        tkinter.messagebox.showinfo( title = "次へ行ってみよう！" , 
        message = "海賊王に、おれはなる！！！！")

        #自動的に閉じる