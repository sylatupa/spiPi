import time
import os
import subprocess
import paho.mqtt.client as mqtt
import json


broker_address="192.168.1.55"
'''
mqtt_topic="test"

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-7")))
    print("topic=",message.topic , " ,qos=" , message.qos , " ,retain_flag=",message.retain)   
    obj = json.loads(str(message.payload.decode("utf-8")))    
    val = obj['v']
    print("received ", val  )
'''
global client
def connect_client():
	global client
	client = mqtt.Client("spyPi")
	client.connect(broker_address, 1883)
	#client.on_message=on_message
	client.loop_start()

def publish_data(data):
	client.publish(data["topic"],str(data["m"]) )  #FUDI FORMATTED https://stackoverflow.com/questions/31811448/from-node-red-to-pure-data-with-udp

def publish_data2(topic, data):
	client.publish(topic, data)  #FUDI FORMATTED https://stackoverflow.com/questions/31811448/from-node-red-to-pure-data-with-udp



def test_publish():
	while True:
		print("Top")

		client.publish("up","1.0")
		time.sleep(1)
		client.publish("down","1.0")
		time.sleep(1)
		client.publish("left","1.0")
		time.sleep(1)
		client.publish("test3","3.0")        
		time.sleep(1)
		client.publish("apples", 5.0)

connect_client()

#data = {"topic":"spyPi/direction/right", "m":22 }
#publish_data(data)
#data = {"topic":"spyPi/direction/up", "m":21}
#publish_data(data)
#data = {"topic":"spyPi/direction/down", "m":2 }
#publish_data(data)
##test_publish()
#print(data["topic"] , "    ", data["m"])
