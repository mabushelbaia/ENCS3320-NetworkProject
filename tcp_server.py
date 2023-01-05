from socket import *
import time
serverPort = 5566
server_socket = socket(AF_INET,SOCK_STREAM)
messages_received = 0
server_socket.bind(('', serverPort))
server_socket.listen()
try:
    while True:
        print("Waiting for connection...")
        connection, address = server_socket.accept()
        try:
            print("Connection from {}".format(address))
            start_time = time.time()
            while True:
                message = connection.recv(16).decode('utf-8')
                if not message:
                    break
                print(int(message))
                messages_received += 1
        finally:
            end_time = time.time()
            connection.close()
            print("Messages received: {}".format(messages_received))
            print("Time required to receive the packets: {:.2f}s".format(end_time - start_time))
            messages_received = 0
except KeyboardInterrupt:
    print("Keyboard interrupt received. Shutting down server.")
finally:
    server_socket.close()
