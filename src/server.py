#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
#Write your code here

PORT = 3000
BUFFER_SIZE = 2048

serverSocket.bind(('', PORT))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(BUFFER_SIZE).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()
        f.close()
        #Send one HTTP header line into socket
        #Write your code here
        successMessage = 'HTTP/1.1 200 OK\n\n'
        connectionSocket.send(successMessage.encode())
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
        print("OK!")
    except IOError:
        #Send response message for file not found
        #Write your code here
        successMessage = 'HTTP/1.1 404\n\n'
        connectionSocket.send(successMessage.encode())
        #Close client socket
        #Write your code here
        connectionSocket.close()
        pass

serverSocket.close()
