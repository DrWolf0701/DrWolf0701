import machine
import time

adc = machine.ADC(4) #machine裡面有乙個ADC class，用adc控制ADC實體
while True: #無限迴圈讓它永遠做
    temperature_value = adc.read_u16() #內鍵的溫度感測器，連做都不用做
    print(temperature_value)
    time.sleep(3) #SPEC裡面寫說刮弧裡放secnonds，教學才會用sleep，sleep是叫硬體暫時停止