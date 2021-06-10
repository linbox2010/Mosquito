import paho.mqtt.client as mqtt
import time

HOST = "localhost"
PORT = 1883
MQTT_USER = "user"
MQTT_PASS = "password"

def on_connect(client,userdata,flags,rc):
    print("Connected!",str(rc))
    for i in range(10):
        client.subscribe("dev/test" + str(i))

def on_message(client,userdata,message):
    topic = str(message.topic)
    message = str(message.payload.decode("utf-8"))
    print(f"Received message from {topic}: {message}")

Client = mqtt.Client('client2')

Client.username_pw_set(MQTT_USER,MQTT_PASS)
Client.on_connect = on_connect
Client.on_message = on_message
Client.connect(HOST,PORT)
Client.loop_forever()
Client.disconnect()