from socket import *
serverPort = 8080
server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('', serverPort))
server_socket.listen()
print("Server is listening on port {}".format(serverPort))
try:
    while True:
        print("Waiting for requests...")
        connection, address = server_socket.accept()
        message = connection.recv(1024).decode('utf-8')
        if not message:
            break
        request_method = message.split(" ")[0]
        request_url = message.split(" ")[1]
        print(request_method, request_url)
        if request_method == "GET" and (request_url == "/" or request_url == "/en"):
            connection.send("HTTP/1.1 200 OK\r\n".encode('utf-8'))
            connection.send("Content-Type: text/html\r\n".encode('utf-8'))
            connection.send("\r\n".encode('utf-8'))
            with open("index.html", "r") as f:
                connection.send(f.read().encode('utf-8'))
                print("Sent index.html")
        elif request_method == "GET" and request_url == "/ar":
            connection.send("HTTP/1.1 200 OK\r\n".encode('utf-8'))
            connection.send("Content-Type: text/html\r\n".encode('utf-8'))
            connection.send("\r\n".encode('utf-8'))
            with open("index.html", "r") as f:
                connection.send(f.read().encode('utf-8'))
                print("Sent index.html")
        elif request_method == "GET" and request_url == "/style.css":
            connection.send("HTTP/1.1 200 OK\r\n".encode('utf-8'))
            connection.send("Content-Type: text/css\r\n".encode('utf-8'))
            connection.send("\r\n".encode('utf-8'))
            with open("style.css", "r") as f:
                connection.send(f.read().encode('utf-8'))
                print("Sent styles.css")
        elif request_method == "GET" and request_url == "/favicon.ico":
            connection.send("HTTP/1.1 200 OK\r\n".encode('utf-8'))
            connection.send("Content-Type: image/x-icon\r\n".encode('utf-8'))
            connection.send("\r\n".encode('utf-8'))
            with open("favicon.ico", "rb") as f:
                connection.send(f.read())
                print("Sent favicon.ico")
        elif request_method == "GET" and request_url == "/images/first_logo.jpg":
            connection.send("HTTP/1.1 200 OK\r\n".encode('utf-8'))
            connection.send("Content-Type: image/jpg\r\n".encode('utf-8'))
            connection.send("\r\n".encode('utf-8'))
            with open("images/first_logo.jpg", "rb") as f:
                connection.send(f.read())
                print("Sent first_logo.jpg")
        elif request_method == "GET" and request_url == "/images/gh.png":
            connection.send("HTTP/1.1 200 OK\r\n".encode('utf-8'))
            connection.send("Content-Type: image/jpg\r\n".encode('utf-8'))
            connection.send("\r\n".encode('utf-8'))
            with open("images/gh.png", "rb") as f:
                connection.send(f.read())
                print("Sent first_logo.jpg")
        connection.close()
except KeyboardInterrupt:
    print("Keyboard interrupt received. Shutting down server.")
finally:
    server_socket.close()
