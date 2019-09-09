# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:09:47 2019

@author: Bartek
"""

from socket import *
serverName = 'localhost'
serverPort = 'serverPort'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Lowercase input word\n')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
#print modified sentence from server
print('Modified sentence from server: ', modifiedSentence.decode())
clientSocket.close()


