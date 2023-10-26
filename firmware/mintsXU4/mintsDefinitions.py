
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

# sensorInfoFile            = 'mintsXU4/credentials/sensorIDs.yml'
# sensorInfo                = yaml.load(open(sensorInfoFile),Loader=yaml.FullLoader)
sensorInfo                = pd.read_csv('https://raw.githubusercontent.com/mi3nts/AirQualityAnalysisWorkflows/main/influxdb/nodered-docker/sensorIDs.csv')
# portInfoFile              = 'mintsXU4/credentials/portIDs.yml'
# portInfo                  = yaml.load(open(portInfoFile),Loader=yaml.FullLoader)
portInfo                  = pd.read_csv('https://raw.githubusercontent.com/mi3nts/AirQualityAnalysisWorkflows/main/influxdb/nodered-docker/portIDs.csv')

nodeInfo                  = pd.read_csv('https://raw.githubusercontent.com/mi3nts/AirQualityAnalysisWorkflows/main/influxdb/nodered-docker/id_lookup.csv')

mqttBrokerDC              = "mqtt.circ.utdallas.edu"
mqttBrokerLoRa            = "mqtt.lora.trecis.cloud"

mqttPort                  = 8883  # Secure port
mqttPortLoRa              = 1883  # Secure port

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