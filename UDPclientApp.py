# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:38:25 2019

@author: Bartek
"""
from socket import *
serverName = 'localhost'
serverPort = 1200
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase word:\n')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
