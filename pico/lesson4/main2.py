from machine import Timer

#tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
#ONE_SHOT代表執行乙次

#tim.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(2))
#請你建立一個timer，每2秒執行且持續執行
#用timer去做就不用time去寫一個while迴圈
count=0
def mycallback(t:Timer): #會把led_timer傳到t
    #pass #沒做任何事，暫時不寫
    global count #global代表全域，告訴它裡面用的count永遠等於外面的count
    count+=1
    print(f"目前mycallback被執行:{count}次")
    if count >=10: #指定執行次數
        t.deinit() #把Timer消滅

led_timer = Timer(period=1000,mode=Timer.PERIODIC,callback=mycallback)
#period=1000就是1秒, 這邊mycallback是註冊不是function, 用led_timer去接收