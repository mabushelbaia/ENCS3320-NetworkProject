from socket import *
import os
serverPort = 7781
server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('', serverPort))
server_socket.listen()
print("Server is listening on port {}".format(serverPort))
def handle_requests(connection, request_method, request_url):
        if request_method == "GET" and request_url in ["/", "/en", "/index.html", "/main_en.html"]:
            connection.send("HTTP/1.1 200 OK\r\n".encode('utf-8'))
            connection.send("Content-Type: text/html\r\n".encode('utf-8'))
            connection.send("\r\n".encode('utf-8'))
            with open("static/main_en.html", "r") as f:
                connection.send(f.read().encode('utf-8'))
                print("Sent main_en.html")
        elif request_method == "GET" and request_url in ["ar", "/ar", "/index_ar.html", "/main_ar.html"]:
            connection.send("HTTP/1.1 200 OK\r\n".encode('utf-8'))
            connection.send("Content-Type: text/html\r\n".encode('utf-8'))
            connection.send("\r\n".encode('utf-8'))
            with open("static/main_ar.html", "r", encoding="utf-8") as f:
                connection.send(f.read().encode('utf-8'))
                print("Sent main_ar.html")
        elif request_method == "GET" and request_url == "/style.css":
            connection.send("HTTP/1.1 200 OK\r\n".encode('utf-8'))
            connection.send("Content-Type: text/css\r\n".encode('utf-8'))
            connection.send("\r\n".encode('utf-8'))
            with open("styles/style.css", "r") as f:
                connection.send(f.read().encode('utf-8'))
                print("Sent styles.css")
        elif request_method == "GET" and request_url == "/favicon.ico":
            connection.send("HTTP/1.1 200 OK\r\n".encode('utf-8'))
            connection.send("Content-Type: image/x-icon\r\n".encode('utf-8'))
            connection.send("\r\n".encode('utf-8'))
            with open("favicon.ico", "rb") as f:
                connection.send(f.read())
                print("Sent favicon.ico")
        # Images
        elif request_method == "GET" and request_url[8:] in os.listdir("images"):
            connection.send("HTTP/1.1 200 OK\r\n".encode('utf-8'))
            connection.send(f"Content-Type: image/{request_url[-3:]}\r\n".encode('utf-8'))
            connection.send("\r\n".encode('utf-8'))
            with open(request_url[1:], "rb") as f:
                connection.send(f.read())
                print("Sent {}".format(request_url[8:]))
        elif request_method == "GET" and request_url in ["/go", "/so", "/bzu"]:
            link = {"/go": "Location: https://www.google.com", "/so": "Location: https://www.stackoverflow.com", "/bzu": "Location: https://www.birzeit.edu"}
            connection.send("HTTP/1.1 307 Temporary Redirect\r\n".encode('utf-8'))
            connection.send(f"{link[request_url]}\r\n".encode('utf-8'))
        elif request_method == "GET" and request_url == "/ahmadosh_en":
            connection.send("HTTP/1.1 200 OK\r\n".encode('utf-8'))
            connection.send("Content-Type: text/html\r\n".encode('utf-8'))
            connection.send("\r\n".encode('utf-8'))
            with open("static/project.html", "r", encoding="utf-8") as f:
                connection.send(f.read().encode('utf-8'))
                print("Sent project.html.html")
        elif request_method == "GET" and request_url == "/ahmadosh_ar":
            connection.send("HTTP/1.1 200 OK\r\n".encode('utf-8'))
            connection.send("Content-Type: text/html\r\n".encode('utf-8'))
            connection.send("\r\n".encode('utf-8'))
            with open("static/project_ar.html", "r", encoding="utf-8") as f:
                connection.send(f.read().encode('utf-8'))
                print("Sent project_ar.html")
        elif request_method == "GET" and request_url == "/project.css":
            connection.send("HTTP/1.1 200 OK\r\n".encode('utf-8'))
            connection.send("Content-Type: text/css\r\n".encode('utf-8'))
            connection.send("\r\n".encode('utf-8'))
            with open("styles/project.css", "r", encoding="utf-8") as f:
                connection.send(f.read().encode('utf-8'))
                print("Sent project.css")
        elif request_method == "GET" and request_url == "/project.js":
            connection.send("HTTP/1.1 200 OK\r\n".encode('utf-8'))
            connection.send("Content-Type: text/javascript\r\n".encode('utf-8'))
            connection.send("\r\n".encode('utf-8'))
            with open("styles/project.js", "r", encoding="utf-8") as f:
                connection.send(f.read().encode('utf-8'))
                print("Sent project.js")
            
        else:
            connection.send("HTTP/1.1 404 Not Found\r\n".encode('utf-8'))
            connection.send("Content-Type: text/html\r\n".encode('utf-8'))
            connection.send("\r\n".encode('utf-8'))
            with open("static/not_found.html", "r") as f:
                text = f.read()
                text = text.format(ip=address[0], port=address[1])
                connection.send(text.encode('utf-8'))
            print("Sent 404 Not Found")
try:
    while True:
        connection, address = server_socket.accept()
        message = connection.recv(1024).decode('utf-8')
        print(message)
        if not message:
            break
        request_method = message.split(" ")[0]
        request_url = message.split(" ")[1]
        handle_requests(connection, request_method, request_url)
        connection.close()
except KeyboardInterrupt:
    print("Keyboard interrupt received. Shutting down server.")
finally:
    server_socket.close()
