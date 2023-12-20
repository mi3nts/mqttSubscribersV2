# mqttSubscribersV2
Contains firmware on obtaining live data from mints MQTT data pipelines

# Implimentation
Before running this in your system, please request credentials files from a MINTS team member and place it @
`mqttSubscribersV2/firmware/mintsXU4/credentials`.  
Afterwards run `./runDataReaders.sh` @ `mqttSubscribersV2/firmware/`
To stop the implimentation run  `./stopDataReaders.sh` @ `mqttSubscribersV2/firmware/`

## Main Goals 
- Record data only visible on node ID look up CSV
- Check for LoRaWAN port IDs from LoRaWAN Support CSV
- Raw LoRaWAN data must be saved just as we did before
- Should Contain two seperate codes for data saving

 ## TO DO 
 - Custom Sensor ID and Node ID reads
