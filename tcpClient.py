import socket

serverName = '127.0.0.1'  # Creating server name
serverPort = 12345  # Creating server port
bufferSize = 1024  # Setting buffer size >= 1024

tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating a TCP client socket
tcpClientSocket.connect((serverName, serverPort))  # Attaches socket to the remote server name/IP and port

tcpClientMessage = input('Enter a string of lowercase letters: ')  # Stores input from client after prompt is shown

messageBytes = str.encode(tcpClientMessage)  # Encodes the user message as a string

tcpClientSocket.send(messageBytes)  # Sends the message out

newMessage = tcpClientSocket.recv(bufferSize)  # Variable for the new message to be received

messageFromServer = newMessage.decode()  # Decodes the message upon arrival and stores it into new variable

print(messageFromServer)  # Prints the newly received message
tcpClientSocket.close()  # Closes the socket
