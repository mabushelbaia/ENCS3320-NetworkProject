from socket import *
import time
serverName = '172.22.9.191'
serverPort = 5566
# start a timer
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((serverName,serverPort))
try:
    start_time = time.time()    
    for i in range(1, 10**6 + 1):
        message = str(i).zfill(16).encode('utf-8')
        client_socket.send(message)
except ConnectionResetError:
    print("Connection reset by peer.")
except KeyboardInterrupt:
    print("Keyboard interrupt received. Shutting down client.")
finally:
    client_socket.close()
    end_time = time.time()
    print("Messages sent: {}".format(i))
    print("Time required to send the packets: {:.2f}s".format(end_time - start_time))