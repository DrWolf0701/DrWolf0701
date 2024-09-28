#import machine
#import time #後來沒用到time
from machine import Timer, ADC, Pin, PWM, RTC
import tools

tools.connect()
#adc = machine.ADC(4) #machine裡面有乙個ADC class，用adc控制ADC實體
adc = ADC(4)
pwm=PWM(Pin(15),freq=2000) #Pin(15)是LED
conversion_factor = 3.3 / (65535) #3.3V轉換, 參考老師的講議pico_W/一般操作/0_5內建溫度感測器(ADC)/
rtc=RTC()

'''
while True: #無限迴圈讓它永遠做
    reading = adc.read_u16() * conversion_factor #內鍵的溫度感測器，連做都不用做
    temperature = 27 - (reading -0.706)/0.001721
    print(temperature)
    time.sleep(2) #SPEC裡面寫說刮弧裡放secnonds，教學才會用sleep，sleep是叫硬體暫時停止
'''

def do_thing(t): #t代表Timer的實體
    reading = adc.read_u16() * conversion_factor #內鍵的溫度感測器，連做都不用做
    temperature = 27 - (reading -0.706)/0.001721
    year,month,day,weekday, hours, minutes, seconds,info = rtc.datetime()
    datetime_str = f"{year}-{month}-{day} {hours}:{minutes}:{seconds}"
    print(datetime_str)
    #print(rtc.datetime()) #tuple是把一組數值暫時包在一起
    print(temperature)

def do_thing1(t):
    #pass
    adc1 = ADC(Pin(26)) #可變電阻，參考 pico_W/一般操作/1_1_3_可變電阻控制LED
    duty = adc1.read_u16() #照說明書
    pwm.duty_u16(duty) #要看SPEC, 這就是ADC+PWM
    
    print(f'可變電阻:{round(duty/65535*10)}') #想抓到0~10的等級

#同時做二件事
t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing) #要看說明書
t2 = Timer(period=500, mode=Timer.PERIODIC, callback=do_thing1) #500代表0.5秒

