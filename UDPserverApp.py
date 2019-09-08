# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 19:59:56 2019

@author: Bartek
"""
from socket import *
serverPort = 1200
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("Server is ready for receiving data")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)