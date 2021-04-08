import socket
PORT = 8080
IP = "127.0.0.1"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("The server is configured!")

while True:
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    print("A client has connected to the server!")
    msg_raw = cs.recv(2048)
    msg = msg_raw.decode()
    print(f"Received Message: {msg}")
    try:
        response = int(msg) ** int(msg)
        cs.send(str(response).encode())
    except ValueError:
        cs.send("We need a number".encode())
    cs.close()