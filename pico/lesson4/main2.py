from machine import Timer

tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
tim.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(2))
#請你建立一個timer，每2秒執行且持續執行
#用timer去做就不用time去寫一個while迴圈