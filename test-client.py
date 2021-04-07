# main.py
import sys

from socket import *

bufferSize = 2048

if __name__ == "__main__":
	host = sys.argv[1]
	port = int(sys.argv[2])
	path = sys.argv[3]

	message = 'GET ' + path + ' HTTP/1.1'

	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((host, port))

	encodedMessage = message.encode()

	clientSocket.send(encodedMessage)

	receivedMessage = clientSocket.recv(bufferSize)
	clientSocket.close()
	
	print(
		'-------------------------------------\n'
		+
		receivedMessage.decode()
		+
		'\n-------------------------------------'
	)

	