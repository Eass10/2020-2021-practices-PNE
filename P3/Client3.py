import socket
from termcolor import colored
import colorama


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("OK")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print("Server is up.")
            s.close()
        except ConnectionRefusedError:
            print("Could not connect to the server. Is it running? Have you checked the IP and the port?")

    def __str__(self):
        return "Connection to SERVER at " + self.ip + ", PORT: " + str(self.port)

    def talk(self, msg):
        colorama.init(strip="False")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        print("To server:", end=" ")
        print(colored(msg, "blue"))
        s.send(msg.encode())
        response = s.recv(2048).decode("utf-8")
        print("From server:", end=" ")
        print(colored(response, "yellow"))
        s.close()
        return "From server: " + response
