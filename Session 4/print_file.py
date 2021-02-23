from pathlib import Path
#"RNU6_269P.txt"; "FRAT1.txt"; "U5.txt"; "ADA.txt"; "FXN.txt"
try:
    Filename = input("Introduce the name of your file: ")
    file_contents = Path(Filename).read_text()
    print(file_contents)
except FileNotFoundError:
    print("The file you have introduce cannot be found.")