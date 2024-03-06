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

sensorInfo            = mD.sensorInfo
portInfo              = mD.portInfo
credentials           = mD.credentials

nodeInfo              = mD.nodeInfoIQ

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

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    topic = "utd/lora/app/3/device/+/event/up"
    client.subscribe(topic)
    print("Subscrbing to Topic: "+ topic)


def on_message(client, userdata, msg):
    try:
        print("==================================================================")
        print(" - - - MINTS DATA RECEIVED - - - ")
        print()
        dateTime,gatewayID,nodeID,sensorID,\
            framePort,base16Data,binaryBits = \
                mLR.loRaSummaryWriteIQ(msg)

        print("Node ID      :" + nodeID)
        print("Sensor ID    :" + sensorID)
        print("FramePort    :" + str(framePort))

        if nodeID in nodeIDs:
            print("Date Time    :" + str(dateTime))
            print("Base 16 Data :" + str(base16Data))
            print("Binary Data  :" + str(binaryBits))
            print(len(binaryBits))
            mLR.sensorSendLoRaIQ(dateTime,nodeID,sensorID,framePort,base16Data,binaryBits)

    except Exception as e:
        print("[ERROR] Could not publish data, error: {}".format(e))


# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(mqttUN,mqttPW)
client.connect(broker, port, 60)
client.loop_forever()

