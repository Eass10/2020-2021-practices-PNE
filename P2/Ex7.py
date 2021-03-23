from Client0 import Client
from pathlib import Path
from Seq2 import Seq
import colorama
from termcolor import colored
print("---|PRACTICE 2: EXERCISE 6|---")

IP = "127.0.0.1"
PORT = 12000
PORT_2 = 12300
c = Client(IP, PORT)
c_2 = Client(IP, PORT_2)

s = Seq()
s.seq_read_fasta("./Sequences/FRAT1.txt")
count = 0
i = 0
while i < len(s.strbases) and count < 10:
    colorama.init(strip = "False")
    fragment = s.strbases[i:i+10]
    count += 1
    i += 10
    print("Fragment", count, ":", fragment)
    if count % 2 == 0:
        c_2.debug_talk("Fragment " + str(count) + ": " + fragment)
    else:
        c.debug_talk("Fragment " + str(count) + ": " + fragment)