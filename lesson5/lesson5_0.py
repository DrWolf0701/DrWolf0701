try:  
    weight = int(input("請輸入體重（公斤）："))
    height = int(input("請輸入身高（公分）："))

    bmi = weight / ((height/100) ** 2)

    print(f"BMI是：{bmi:.2f}")

    if bmi < 18.5:
        print("體重過輕")
    elif 18.5 <= bmi < 24:
        print("正常範圍")
    elif 24 <= bmi < 27:
        print("過重")
    elif 27 <= bmi < 30:
        print("輕度肥胖")
    elif 30 <= bmi < 35:
        print("中度肥胖")
    else:
        print("重度肥胖")


except ValueError:
    print("輸入格式有錯")

except Exception as e:
    print(f'錯誤訊息:{e}')

print("應用程式結束")