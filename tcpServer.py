import socket

serverPort = 12345  # Creates server port
bufferSize = 1024  # Sets buffer size >= 1024

tcpServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creates a new TCP server socket

tcpServerSocket.bind(('', serverPort))  # Binds the socket to the host name/IP and port

tcpServerSocket.listen(1)  # Listens for incoming data
print("TCP server is ready.")  # Tells the user that the TCP server is running correctly

while 1:  # Loop that goes forever
    tcpConnectionSocket, addr = tcpServerSocket.accept()  # Accepts incoming requests, creates new socket on return
    message = tcpConnectionSocket.recv(bufferSize)  # Reads the bytes from the socket (not addr like UDP does)
    modifiedMessage = message.upper()  # Takes the received message and turns it into uppercase string
    tcpConnectionSocket.send(modifiedMessage)  # Sends back the modified message
    tcpConnectionSocket.close()  # Closes the socket
