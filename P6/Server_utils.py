from Seq6 import Seq
import termcolor
import colorama
from pathlib import Path
from jinja2 import Template

HTML_ASSETS = "./HTML/info/"
OPERATION_LIST = ["Info", "Complement", "Reverse"]


def print_colored(message, color):
    colorama.init(strip="False")
    print(termcolor.colored(message, color))


def format_command(command):
    return command.replace("\n", "").replace("\r", "")


def read_template_html_file(filename):
    content = Template(Path(filename).read_text())
    return content


def get(list_sequences, number_seq):
    context = {
        "number": number_seq,
        "sequence": list_sequences[int(number_seq)]
    }
    contents = read_template_html_file(HTML_ASSETS + "get.html").render(context=context)
    return contents


def info(sequence):
    list_bases = ["A", "C", "T", "G"]
    sequence = Seq(sequence.replace('"', ""))
    t_l = Seq.len(sequence)
    count_list = []
    percentage_list = []
    for base in list_bases:
        count_list.append(sequence.count_base_1(base))
    for i in range(0, len(count_list)):
        percentage_list.append(count_list[i] * 100 / t_l)
    result = f"""Total length: {t_l}
        A: {count_list[0]} ({percentage_list[0]}%)
        C: {count_list[1]} ({percentage_list[0]}%)
        G: {count_list[2]} ({percentage_list[0]}%)
        T: {count_list[3]} ({percentage_list[0]}%)"""
    context = {
        "sequence": sequence,
        "result": result,
        "operation": "Info"
    }
    contents = read_template_html_file(HTML_ASSETS + "operation.html").render(context=context)
    return contents


def comp(sequence):
    sequence = Seq(sequence.replace('"', ""))
    comp_seq = str(Seq.seq_complement(sequence))
    context = {
        "sequence": sequence,
        "result": comp_seq,
        "operation": "Comp"
    }
    contents = read_template_html_file(HTML_ASSETS + "operation.html").render(context=context)
    return contents

def rev(sequence):
    argument = Seq(sequence.replace('"', ""))
    rev_seq = str(Seq.seq_reverse(argument))
    context = {
        "sequence": sequence,
        "result": rev_seq,
        "operation": "Rev"
    }
    contents = read_template_html_file(HTML_ASSETS + "operation.html").render(context=context)
    return contents



def gene(gene):
    PATH = "./Sequences/" + gene + ".txt"
    s1 = Seq()
    s1.seq_read_fasta(PATH)
    context = {
        "gene_name": gene,
        "gene_contents": s1.strbases
    }
    contents = read_template_html_file(HTML_ASSETS + "gene.html").render(context=context)
    return contents
