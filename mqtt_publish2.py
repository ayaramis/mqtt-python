import paho.mqtt.client as mqtt
from paho.mqtt.client import CallbackAPIVersion
from random import randrange, uniform
import time

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "Temperature_Inside")
client.connect("broker.hivemq.com", 1883, 60)

while True:
    randNumber = randrange(10)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(1)
