# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:38:25 2019

@author: Bartek
"""

from socket import *
serverName = 'hostname'
serverPort = 1200
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Zdanie wejsciowe zapisane malymi literami')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
