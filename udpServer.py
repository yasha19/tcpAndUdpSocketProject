import socket

serverPort = 12345  # Creating the server port
bufferSize = 1024  # Setting the buffer size >= 1024

udpServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Creating the server socket
udpServerSocket.bind(('', serverPort))  # Binding the host/IP and port to the server socket

print("UDP server is ready.")  # Message to show that the server is running correctly

while 1:  # Loop that runs forever
    message, udpClientAddress = udpServerSocket.recvfrom(bufferSize)  # Reading from server socket into message
    #  Obtaining the client's hostname/IP and port number

    modifiedMessage = message.upper()  # Creating new variable to store the uppercase string that was received
    udpServerSocket.sendto(modifiedMessage, udpClientAddress)  # Sending the new message back to the client
