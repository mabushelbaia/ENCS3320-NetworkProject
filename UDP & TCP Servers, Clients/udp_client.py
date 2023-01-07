from socket import *
from time import time
serverName = 'localhost'
serverPort = 5566   
client_socket = socket(AF_INET, SOCK_DGRAM)
try:
    start_time = time()
    for message in range(1, 10**6+ 1):
        client_socket.sendto(str(message).encode('utf-8'),(serverName, serverPort))
finally:
    client_socket.close()
    end_time = time()
    print("Messages sent: {}".format(message))
    print("Time required to send the packets: {:.7f}s".format(end_time - start_time))
