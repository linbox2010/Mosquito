import paho.mqtt.client as mqtt
import time

HOST = "localhost"
PORT = 1883
MQTT_USER = "user"
MQTT_PASS = "password"

Client = mqtt.Client('client1')
Client.username_pw_set(MQTT_USER,MQTT_PASS)
Client.connect(HOST,PORT)
Client.loop_start()

while(1):
    mess_1 = "test publish"
    str1 = "dev/test"

    for i in range(10):
        topic = ' '.join([str1,str(i)])
        mess = ' '.join([mess_1,str(i)])
        Client.publish(topic,mess)
        print(f"Sedning message '{mess}' to {topic}")
    time.sleep(1)