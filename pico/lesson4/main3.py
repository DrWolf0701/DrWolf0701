#green每隔2秒執行乙次，red每隔1秒執行乙次
from machine import Timer, Pin

green_led=Pin("LED",Pin.OUT)

green_count=0
def green_led_mycallback(t:Timer): 

    global green_count 
    green_count+=1
    #print(f"目前mycallback被執行:{green_count}次")
    green_led.toggle() #toggle的意思是原本暗的變亮的，亮的變暗的，總共體亮5次
    print("green_led初執行")
    if green_count >=10: 
        t.deinit() 

green_led_timer = Timer(period=1000,mode=Timer.PERIODIC,callback=green_led_mycallback)

red_led=Pin(15,Pin.OUT)
red_count=0
def red_led_mycallback(t:Timer): 

    global red_count 
    red_count+=1
    #print(f"目前mycallback被執行:{red_count}次")
    red_led.toggle() #toggle的意思是原本暗的變亮的，亮的變暗的，總共體亮5次
    print("red_led初執行")
    if red_count >=10: 
        t.deinit()
red_led_timer = Timer(period=2000,mode=Timer.PERIODIC,callback=red_led_mycallback)
        