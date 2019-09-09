# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:10:34 2019

@author: Bartek
"""

from socket import *
#arbitrary port for communication
serverPort = 12000
#socket definition with Adress Family & Socket Kind
serverSocket = socket(AF_INET, SOCK_STREAM)
#bind the socket to address, address depends on Socket Kind
#for AF_INET (host, port) format
serverSocket.bind(('',serverPort))
#enable server to accept connection
serverSocket.listen()

print('Server is ready for receiving data')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    #modify lowercase to uppercase
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    #close socekt
    connectionSocket.close()