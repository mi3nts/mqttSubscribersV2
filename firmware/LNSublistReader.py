# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
import base64
from pickle import TRUE
import paho.mqtt.client as mqtt
import datetime
import yaml
import collections
import json

from mintsXU4 import mintsSensorReader as mSR
from mintsXU4 import mintsDefinitions as mD
from mintsXU4 import mintsLatest as mL
from mintsXU4 import mintsLoRaReader as mLR
from collections import OrderedDict
import struct


mqttPort              = mD.mqttPortLoRa
mqttBroker            = mD.mqttBrokerLoRa
mqttCredentialsFile   = mD.credentials
tlsCert               = mD.tlsCert
nodeInfo              = mD.nodeInfo
sensorInfo            = mD.sensorInfo
portInfo              = mD.portInfo
credentials           = mD.credentials

connected             = False  # Stores the connection status
broker                = mqttBroker  
port                  = mqttPort  # Secure port
mqttUN                = credentials['LoRaMqtt']['username'] 
mqttPW                = credentials['LoRaMqtt']['password'] 

nodeIDs               = nodeInfo['mac_address'].tolist()
print(nodeIDs)
sensorIDs             = sensorInfo['sensorID']
portIDs               = portInfo['portID']

decoder = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)


deiuList = [
    '70b3d540f40ce423',
    '70b3d540f40ce429',
    '70b3d540f40ce435',
    '70b3d540f40ce430',
    '70b3d540f40ce41f',
    '70b3d540f40ce43c',
    '70b3d540f40ce420',
    '70b3d540f40ce425',
    '70b3d540f40ce438',
    '70b3d540f40ce436',
    '70b3d540f40ce433',
    '70b3d540f40ce43a',
    '70b3d540f40ce422',
    '70b3d540f40ce421',
    '70b3d540f40ce427',
    '70b3d540f40ce426',
    '70b3d540f40ce42f',
    '70b3d540f40ce434',
    '70b3d540f40ce424',
    '70b3d540f40ce42d',
    'a8610a343246750e'
]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    topic = "utd/lora/app/2/device/+/event/up"
    client.subscribe(topic)
    print("Subscrbing to Topic: "+ topic)

def on_message(client, userdata, msg):
    try:
        print("==================================================================")
        print(" - - - MINTS DATA RECEIVED - - - ")
        # print(msg.payload)
        dateTime,gatewayID,nodeID,sensorID,framePort,base16Data = \
            mLR.loRaSummaryWrite(msg,portInfo)
        print("Node ID         : " + nodeID)
        if nodeID in deiuList:
            print("Node ID         : " + nodeID)
            print("Sensor ID       : " + sensorID)
            print("Date Time       : " + str(dateTime))
            print("Port ID         : " + str(framePort))
            print("Base 16 Data    : " + base16Data)
            # if nodeID in nodeIDs:
            #     print("Date Time       : " + str(dateTime))
            #     print("Port ID         : " + str(framePort))
            #     print("Base 16 Data    : " + base16Data)
                # mLR.sensorSendLoRa(dateTime,nodeID,sensorID,framePort,base16Data)
        
    
    except Exception as e:
        print("[ERROR] Could not publish data, error: {}".format(e))


# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(mqttUN,mqttPW)
client.connect(broker, port, 60)
client.loop_forever()

