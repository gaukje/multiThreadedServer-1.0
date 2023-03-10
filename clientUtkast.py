"""
One side must be the active one
☞ take the initiative in creating the connection
☞ this side is called the client
"""
"""

from socket import *
import sys
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)  #This line creates a new socket using the AF_INET address family and the SOCK_STREAM socket type. The AF_INET address family specifies that the socket is using the IPv4 protocol, and the SOCK_STREAM socket type indicates that the socket is using the TCP protocol.

try: 
    clientSocket.connect((serverName, serverPort))

except:
    print("ConnectionError")
    sys.exit()

#username = input("Enter your username: ")
#clientSocket.send(username.encode())

while True:
    username = input("Enter a username: ")
    sentence = input('What would you like to send to the server? ')
    message = f"{username}: {sentence}"
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    
    print('From Server : ', modifiedSentence.decode())
    
        # check if the received message is the broadcast message
    if modifiedSentence.decode().startswith("A new client has joined"):
        print("A new client has joined the chat room")

    if(sentence == "exit"):
        break

clientSocket.close()
"""