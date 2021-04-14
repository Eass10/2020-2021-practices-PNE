from Seq3 import Seq
import termcolor
import colorama


def print_colored(message, color):
    colorama.init(strip="False")
    print(termcolor.colored(message, color))


def format_command(command):
    return command.replace("\n", "").replace("\r", "")


def ping(cs):
    print_colored("PING command", "green")
    response = "OK!"
    print(response)
    cs.send(response.encode())


def get(list_sequences, cs, argument):
    print_colored("GET " + str(argument.replace('"', "")), "yellow")
    response = list_sequences[int(argument.replace("'", "").replace('"', ""))]
    print_colored(response, "red")
    print(response)
    cs.send(response.encode())


def info(argument, cs):
    print_colored("INFO", "yellow")
    list_bases = ["A", "C", "T", "G"]
    argument = Seq(argument.replace('"', ""))
    t_l = Seq.len(argument)
    count_list = []
    percentage_list = []
    for base in list_bases:
        count_list.append(argument.count_base_1(base))
    for i in range(0, len(count_list)):
        percentage_list.append(count_list[i] * 100 / t_l)
    response = f"""Sequence: {argument}
    Total length: {t_l}
    A: {count_list[0]} ({percentage_list[0]}%)
    C: {count_list[1]} ({percentage_list[0]}%)
    G: {count_list[2]} ({percentage_list[0]}%)
    T: {count_list[3]} ({percentage_list[0]}%)"""
    cs.send(response.encode())
    print(response)


def comp(argument, cs):
    print_colored("COMP", "yellow")
    argument = Seq(argument.replace('"', ""))
    comp_seq = str(Seq.seq_complement(argument))
    response = f"""Initial sequence: {argument}
    Complement sequence: {comp_seq}"""
    cs.send(response.encode())
    print(response)


def rev(argument, cs):
    print_colored("REV", "yellow")
    argument = Seq(argument.replace('"', ""))
    rev_seq = str(Seq.seq_reverse(argument))
    response = f"""Initial sequence: {argument}
    Reverse sequence: {rev_seq}"""
    cs.send(response.encode())
    print(response)


def gene(argument, cs):
    print_colored("GENE", "yellow")
    sequence = Seq(Seq.seq_read_fasta_2("./Sequences/" + argument.replace('"', "") + ".txt"))
    comp_seq = str(Seq.seq_complement(sequence))
    rev_seq = str(Seq.seq_reverse(sequence))
    colored_response = f"""Initial sequence: {termcolor.colored(sequence, "red")}
    Complement sequence: {termcolor.colored(comp_seq, "green")}
    Reverse sequence: {termcolor.colored(rev_seq, "blue")}"""
    response = f"""Initial sequence: {sequence}
    Complement sequence: {comp_seq}
    Reverse sequence: {rev_seq}"""
    cs.send(response.encode())
    print(response)
