import socket
from termcolor import colored
import colorama
PORT = 8080
IP = "127.0.0.1"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
count_connections = 0
ls.listen()
print("The server is configured!")
client_addres_list = []
while True:
    colorama.init(strip="False")
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        count_connections += 1
        client_addres_list.append(client_ip_port)
        print("CONNECTION " + str(count_connections) + ". Client IP, PORT: " + str(client_ip_port))
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    print("A client has connected to the server!")
    msg_raw = cs.recv(2048)
    msg = msg_raw.decode()
    print("Received Message: " + colored(msg, "yellow"))
    response = "ECHO: " + msg
    cs.send(response.encode())
    cs.close()
    if count_connections == 5:
        for i in range(0, len(client_addres_list)):
            print("Client " + str(i) + ". Client IP, PORT: " + str(client_addres_list[i]))
        exit(0)
