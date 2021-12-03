from time import sleep

input = ("カップラーメンができるまで、Mr.ぐるまゆとお話ししましょう。")
#変数に目標時間を設定。
target_time = 300

#関数を実行。
def up_timer(secs):
    for i in range(0,secs):
        print(i)
        
        #時間の制御はsleep()
        sleep(1)
    
    #終わりの合図。
    print("あちきの...じゃなくて、\nお主のカップラーメンが出来上がったでありんす。")

