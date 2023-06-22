
from getmac import get_mac_address
import serial.tools.list_ports
import yaml


# Change Accordingly  
mintsDefinitions          = yaml.load(open('mintsXU4/mintsDefinitions.yaml'),Loader=yaml.FullLoader)
dataFolder                = mintsDefinitions['dataFolder']
dataFolderReference       = mintsDefinitions['dataFolder'] + "/reference"
dataFolderMQTTReference   = mintsDefinitions['dataFolder'] + "/referenceMqtt"  # The path of your MQTT Reference Data 
dataFolderMQTT            = mintsDefinitions['dataFolder'] + "/rawMqtt"        # The path of your MQTT Raw Data 
tlsCert                   = mintsDefinitions['tlsCert']     # The path of your TLS cert

latestOn                  = False

mqttOn                    = True
credentials              = 'mintsXU4/credentials/credentials.yaml'
sensorIDs                = 'mintsXU4/credentials/sensorIDs.yml'
portIDs                  = 'mintsXU4/credentials/portIDs.yml'

mqttBrokerDC             = "mqtt.circ.utdallas.edu"
mqttBrokerLoRa           = "mqtt.lora.trecis.cloud"

mqttPort                 = 8883  # Secure port
mqttPortLoRa             = 1883  # Secure port



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
