import socket

serverName = '127.0.0.1'  # Setting the host name/IP
serverPort = 12345  # Creating a port number
bufferSize = 1024  # Setting buffer size >= 1024

udpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Creating the UDP client socket

messageFromClient = input('Enter a string of lowercase letters: ')  # Creating a variable to store input from user
messageBytes = str.encode(messageFromClient)  # Encoding the input as a string
udpClientSocket.sendto(messageBytes, (serverName, serverPort))  # Attaching the server name and port to message
# Sending message into the socket

newMessage, serverAddress = udpClientSocket.recvfrom(bufferSize)  # Reading the reply from the socket into a string

messageFromServer = newMessage.decode()  # Decoding the received message, attaching to new variable

print(messageFromServer)  # Printing the decoded message
udpClientSocket.close()  # Closing the socket
