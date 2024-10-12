import paho.mqtt.client as mqtt
from datetime import datetime
import os, csv

def record(r):
    root_dir = os.getcwd()
    data_dir = os.path.join(root_dir, 'data')
    if not os.path.isdir(data_dir):    
            os.mkdir('data')
    
    today = datetime.today()
    filename = today.strftime("%Y-%m-%d") + ".csv"
    #get_file_abspath
    full_path = os.path.join(data_dir,filename)
    if not os.path.exists(full_path):
        #沒有這個檔,建立檔案
        print('沒有這個檔')
        with open(full_path,mode='w',encoding='utf-8',newline='') as file:
            file.write('時間,設備,值\n')
    
    with open(full_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(r)

def on_connect(client, userdata, flags, reason_code, properties):
    # print(f"Connected with result code {reason_code}")
    # 在连接成功后订阅主题
    client.subscribe("SA-35/#")  # 替换为您想要订阅的主题

# 定义消息接收回调函数
def on_message(client, userdata, msg):
    #payload代表value ; msg代表topic
    global led_origin_value #(重要)宣告function裡面的是全域變數
    topic = msg.topic #一定是字串
    value = msg.payload.decode() #不確性是什麼, 可print(type(value))
    #led_origin_value = 0 #function裡面建立的叫區域變數，執行完就被消滅了，所以不在這裡建立
    if topic == 'SA-35/LED_LEVEL':
        led_value = int(value) #已知傳回來會是整數，所以轉為整數
        
        if led_value != led_origin_value: #不等於時保留(記錄)
            led_origin_value = led_value #(重要)如果沒global就會變區域變數
            print(f'led_value:{(led_value)}')
            today = datetime.today()
            now_str = today.strftime('%Y-%m-%d %H:%M%S')
            save_data = [now_str,"SA-35/LED_LEVEL",led_origin_value] #有改變的時候希望傳出來的是一個list
            record(save_data)   
    # print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")

def main():
    # 创建MQTT客户端实例
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    # 设置用户ID和密码
    username = "pi"  # 替换为您的用户名
    password = "raspberry"  # 替换为您的密码
    client.username_pw_set(username, password)
    # 绑定回调函数
    client.on_connect = on_connect #有刮號代表執行，沒刮號代表註冊
    client.on_message = on_message
    client.connect("192.168.0.252", 1883,60)
    client.loop_forever()


if __name__ ==  "__main__":
    led_origin_value = 0 #全域變數
    main()