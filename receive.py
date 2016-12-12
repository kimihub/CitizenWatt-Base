#!/usr/bin/env python3

from RF24 import *


# file storing data
filename = '/tmp/sensor.log'

# TODO : read from config file 
pipes = [0xE7E7E7E7E7, 0xE056D446D0]

radio = RF24(22, 0)
radio.begin()
radio.setRetries(15, 15)
radio.setDataRate(RF24_250KBPS)
radio.setAutoAck(1)
radio.setPALevel(RF24_PA_MIN)
radio.setCRCLength(RF24_CRC_8)
radio.openReadingPipe(1, pipes[1])

# for debug
# radio.printDetails()

while True:
    radio.startListening()
    pipe = [0]
    while not radio.available():
        continue
    size = radio.getDynamicPayloadSize()
    receive_payload = radio.read(size)
    
    # for debug
    # print(size, ''.join('{:02x}'.format(x) for x in receive_payload))
    # print(receive_payload)
    # print('')
    FileTemp = open(filename, 'wb')
    FileTemp.write(receive_payload)
    FileTemp.close()
