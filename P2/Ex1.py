from Client0 import Client
print("---|PRACTICE 2: EXERCISE 1|---")

IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)
c.advanced_ping()
c.ping()
print(f"IP: {c.ip}, {c.port}")