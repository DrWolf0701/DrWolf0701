#button是input, led是output
from machine import Pin
import time
#GPIO14是 按鈕


red_led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN) #PULL_DOWN下拉電阻

while True:
    if button.value(): #如果數值是0代表false, 有值代表true
        red_led.toggle()
        time.sleep(0.5) #代表按下時有0.5秒是停的