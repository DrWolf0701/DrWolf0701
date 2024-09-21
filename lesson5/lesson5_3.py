
#方法一:module
# import tools #要import才能用裡面的function，呼叫裡面的function要加上module名稱
               #tools.get_status(BMI)
               #專案中可提供自訂的module給它，就是py檔

#方法二:package
import widget #呼叫裡面的function要加上module名稱 ex : widget.get_status(BMI)

#主程式
while True:
    kg=0  #清除變數
    cm=0  #清除變數
    
    cm, kg = widget.input_data() #呼叫function, 且必須接收function傳出的東西(二邊的cm, kg是在不一樣的記憶體中)
                                
    print(f'身高={cm},體重={kg}')

    BMI = widget.calculate_bmi(kg=kg,cm=cm) #呼叫function, 此處的BMI與function裡的BMI一點關係也沒有
                                     #引數值的呼叫，引數名稱的呼叫就是參數名稱，可不依照順序 ex : kg=kg,cm=cm
    print(f'BMI={BMI}')
    
    print(widget.get_status(BMI)) #呼叫function，大寫的BMI傳到function裡copy為bmi去比較
                              
    play_again = input("還要繼續嗎?(y,n)")
    if play_again == "n":
        break
print('程式結束')