# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:09:47 2019

@author: Bartek
"""

from socket import *
serverName = 'serverName'
serverPort = 'serverPort'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('lowercase input word\n')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('Z servera: ', modifiedSentence.decode())
clientSocket.close()


