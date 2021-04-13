from Seq3 import Seq

def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")
    print(termcolor.colored(message, color))

def format_command(command):
    return command .replace("\n", "").replace("\r", "")

def ping(cs):
    print_colored("PING command", "green")
    response = "OK!"
    cs.send(response.encode())

def Get(list_sequences, cs, argument):
    print_colored("GET " + str(argument.replace('"', "")), "yellow")
    response = list_sequences[int(argument.replace("'", "").replace('"', ""))]
    print_colored(response, "red")
    cs.send(response.encode())

def info(argument, cs):
    print_colored("INFO", "yellow")
    list_bases = ["A", "C", "T", "G"]
    argument = Seq(argument.replace('"', ""))
    response1 = "Sequence: " + str(argument) + "\n"
    print_colored(response1, "red")
    response2 = "Total length: " + str(Seq.len(argument)) + "\n"
    print_colored(response2, "blue")
    cs.send((response1 + response2).encode())
    seq_info = Seq.count_base(argument)
    for base in list_bases:
        response = base + ": " + str(seq_info[0][base]) + " (" + str(seq_info[1][list_bases.index(base)]) + "%)" + "\n"
        # cs.send(str(response).encode())
        print(response)

def comp(argument, cs):
    print_colored("COMP", "yellow")
    argument = Seq(argument.replace('"', ""))
    # Initial sequence:
    response = "Initial sequence: " + str(argument) + "\n"
    # cs.send(response.encode())
    print_colored(response, "red")
    # Complement sequence:
    response = "Complement sequence: " + str(Seq.seq_complement(argument))
    cs.send(response.encode())
    print_colored(response, "blue")

def rev(argument, cs):
    print_colored("REV", "yellow")
    argument = Seq(argument.replace('"', ""))
    # Initial sequence:
    response = "Initial sequence: " + str(argument) + "\n"
    # cs.send(response.encode())
    print_colored(response, "red")
    # Reverse sequence:
    response = "Reverse sequence: " + str(Seq.seq_reverse(argument))
    cs.send(response.encode())
    print_colored(response, "green")

def gene(argument, cs):
    sequence = Seq(Seq.seq_read_fasta_2("./Sequences/" + argument.replace('"', "") + ".txt"))
    # Initial sequence:
    response1 = "Initial sequence: " + str(sequence) + "\n"
    # cs.send(response.encode())
    print_colored(response1, "red")
    # Complement sequence:
    response2 = "Complement sequence: " + str(Seq.seq_complement(sequence)) + "\n"
    # cs.send(response.encode())
    print_colored(response2, "blue")
    # Reverse sequence:
    response3 = "Reverse sequence: " + str(Seq.seq_reverse(sequence))
    print_colored(response3, "green")
    response = response1 + "\n" + response2 + "\n" + response3
    cs.send(response.encode())
