from socket import *
import time
serverPort = 5566
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', serverPort))
try:
    count = 0
    start_time = time.time()
    while True:
        message, address = server_socket.recvfrom(16)
        message = message.decode('utf-8')
        count += 1
        if count == 1:
            start_time = time.time()
        print("Messages Count: {}, Last Message: {}, Elapsed time: {:.2f}".format(count, message, time.time() - start_time))
except KeyboardInterrupt:
    print("Keyboard interrupt received. Shutting down server.")
finally:
    server_socket.close()
