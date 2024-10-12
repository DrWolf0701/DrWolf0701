import paho.mqtt.client as mqtt

def record(): #有改變的時候才記錄，先做一個LED
    pass

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
        
        if led_value != led_origin_value: #不等於時保留
            led_origin_value = led_value #(重要)如果沒global就會變區域變數
            print(f'led_value:{(led_value)}')
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