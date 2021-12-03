#使用するクラスをモジュール化
import _3busyou
import _4onepiece1
import _4onepiece2

#簡単な挨拶のチャットボットを作成
bot_dict = {
    'こんにちは': 'コンニチハ',
    'ありがとう': 'ドウイタシマシテ',
    'さようなら': 'サヨウナラ',
    }

while True:
#こんにちは、ありがとう、さようならなら、次の処理。
    command = input('ようこそ、Mr.ぐるまゆの館へ > ')
    response = ''
    for message in bot_dict:
        if message in command:
            response = bot_dict[message]
            break

#空白なら、次の処理。
    if not response:
        response = '何ヲ言ッテルカ、ワカラナイ'
        print(response)

#そのまま占いをしてもらうように誘導。
    e = input("次に進んでくれなんし Yes ▷▷ 0 / No ▷▷ 1 ⇒")

    if e == '0':
        break
    
#一旦休憩。Enterで開始。
input("初めまして、Mr.ぐるまゆと申す。\n早速だが、まずはこのMr.ぐるまゆが、勝手にお主を占おうぞ。")

#順番に占いで遊ぶ
i=0

input("まずは、お主と相性ピッタリなお侍さんを、このMr.ぐるまゆが、独断と偏見でお探し致すぞ？")

#1つ目の占い。
if i == 0:
    #武将をインスタンス化
   game1 = _3busyou.busyou
   game1.start()
   i += 1

input("次に、お主と相性ピッタリなONE PIECEの敵キャラも、Mr.ぐるまゆ様が、独断と偏見でお探し致しちょうぞ？")

#2つ目の占い。
if i == 1:
    #ワンピース１をインスタンス化
    game2 = _4onepiece1.onepiece1
    game2.start()
    i += 1

input('最後に、ここまで遊んでくれたお主に敬意を表して、是非とも読んでほしいONE PIECEを、このMr.ぐるまゆが、独断と偏見でお探し致しよう。')

#3つ目の占い。
if i == 2:
    #ワンピース２をインスタンス化
    game3 = _4onepiece2.onepiece2
    game3.start()
    i += 1

#終わりの挨拶。
print("如何じゃったか？楽しんでいただけたでありんすか？")
print("最後まで遊んでくれて、ありがとうでありんした♪\nカップラーメンも、美味しく召し上がってくれなんし(*'▽')")


