#function
def input_data()->tuple[int,int]: #產生記憶體區塊，執行完就消失(結束前要傳回主程式，不然會被消滅)
    # pass #每一個程式區塊一定要有一行
    while True:
        try:    
            cm = int(input("請輸入身高(公分):"))
            if cm > 300:
                    raise Exception("超過300公分")
            break
        except ValueError:
            print('輸入格式錯誤')
            continue
        except Exception as e:
            print(f'輸入錯誤{cm}')
            continue

    while True:
        try:    
            kg = int(input("請輸入體重(公斤):"))
            if kg > 300:
                raise Exception("超過300公分")
            break
        except ValueError:
            print('輸入格式錯誤')
            continue
        except Exception as e:
            print(f'輸入錯誤{kg}')
            continue
    return cm,kg #return在function裡面代表會傳出東西, tuple可省略刮號

def get_status(bmi:float)->str: #3/10版以後要這樣寫，bmi要傳入一個float參數，最後會傳出字串 
    # pass #每一個程式區塊一定要有一行
    #因為print不會寫在function裡面，多項區塊只會傳出一個字串

    if bmi >=35:
        return "重度肥胖：BMI≧35"
    elif bmi >=30:
        return "中度肥胖：30≦BMI"
    elif bmi >=27:
        return "輕度肥胖：27≦BMI"
    elif bmi >=24:
        return "過重"
    elif bmi >=18.5:
        return "正常範圍"
    else:
        return "體重過輕"
    
def calculate_bmi(kg:int,cm:int)->float: #如果這樣寫()沒有參數會有cm, kg的參數(變數)嗎? 不會 
                                  #:int代表型別提示，傳出的BMI為float  
    cm=(cm/100)*(cm/100)
    BMI=kg/cm
    return BMI  #此處的BMI屬於區域變數，老師故意用一樣的名字
