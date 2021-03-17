from Client0 import Client
print("---|PRACTICE 2: EXERCISE 3|---")

IP = "127.0.0.1"
PORT = 12000
c = Client(IP, PORT)
msg = c.talk("Avengers Endgame is the best film of all time")
print("Response: ", msg)