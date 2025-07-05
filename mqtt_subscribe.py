import paho.mqtt.client as mqtt
from paho.mqtt.client import CallbackAPIVersion
import time

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttBroker = "broker.hivemq.com"
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Smartphone")
client.connect(mqttBroker)

client.loop_start()
client.subscribe("TEMPERATURE")
client.on_message = on_message
time.sleep(30)
client.loop_read()
