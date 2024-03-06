
from getmac import get_mac_address
import serial.tools.list_ports
import yaml
import pandas as pd
# Change Accordingly  
mintsDefinitions          = yaml.load(open('mintsXU4/credentials/mintsDefinitions.yaml'),Loader=yaml.FullLoader)
dataFolder                = mintsDefinitions['dataFolder']
dataFolderReference       = mintsDefinitions['dataFolder'] + "/reference"
dataFolderMQTTReference   = mintsDefinitions['dataFolder'] + "/referenceMqtt"  # The path of your MQTT Reference Data 
dataFolderMQTT            = mintsDefinitions['dataFolder'] + "/rawMqtt"        # The path of your MQTT Raw Data 
tlsCert                   = mintsDefinitions['tlsCert']     # The path of your TLS cert

latestOn                  = False

mqttOn                    = True
credentialsFile           = 'mintsXU4/credentials/credentials.yaml'
credentials               = yaml.load(open(credentialsFile))

sensorInfo                = pd.read_csv('https://raw.githubusercontent.com/mi3nts/mqttSubscribersV2/main/lists/sensorIDs.csv')
portInfo                  = pd.read_csv('https://raw.githubusercontent.com/mi3nts/mqttSubscribersV2/main/lists/portIDs.csv')

nodeInfo                  = pd.read_csv('https://raw.githubusercontent.com/mi3nts/AirQualityAnalysisWorkflows/main/influxdb/nodered-docker/id_lookup.csv')

mqttBrokerDC              = "mqtt.circ.utdallas.edu"
mqttBrokerLoRa            = "mqtt.lora.trecis.cloud"

mqttPort                  = 8883  # Secure port
mqttPortLoRa              = 1883  # Secure port

# IQ Sensors 
nodeInfoIQ                = pd.read_csv('https://raw.githubusercontent.com/mi3nts/AirQualityAnalysisWorkflows/main/influxdb/nodered-docker/id_lookup_iq.csv')

# ATMO : 0xA3 SENSE : 0xA4 AERO : 0xA5 PMI : 0xA6 AERO CO2 : 0xA7
IQDeviceIDs               = {
                                "a3": "D739FATMO",
                                "a4": "D739SENSE",
                                "a5": "D739FAERO",
                                "a6": "D739PMI",
                                "a7": "D739AEROCO2"
                                }

IQSensorIDs               = {
                                "11": "RTD1",
                                "12": "RTD2",
                                "13": "RTD3",
                                "21": "PS1",
                                "22": "PS2",
                                "31": "PC1",
                                "04": "TM1",
                            }

def findMacAddress():
    macAddress= get_mac_address(interface="eth0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    macAddress= get_mac_address(interface="docker0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    macAddress= get_mac_address(interface="enp1s0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    return "xxxxxxxx"

macAddress                = findMacAddress()

print()
print("----- MQTT Subscriber V2 -----")
print(" ")
print("Node Info:")
print(nodeInfo)
print(" ")
print("Sensor Info:")
print(sensorInfo)
print(" ")
print("Port Info:")
print(portInfo)
print(" ")
print(" IQ Devices")
print(" ")
print("Node Info IQ:")
print(nodeInfoIQ)
print(" ")
print("IQ Device IDs:")
print(IQDeviceIDs)
print(" ")
print("IQ Sensor IDs:")
print(IQSensorIDs)
print(" ")