import Server_utils as su
import json
from Seq import Seq


def taking_out_space(specie):
    answer = specie.replace(" ", "_")
    return answer


def list_seqs(connection, ENDPOINT, PARAMS, arguments, context):
    connection.request("GET", ENDPOINT + PARAMS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        species_list = []
        amount_species = len(response_dict["species"])
        context["amount_species"] = amount_species
        # print(json.dumps(response_dict, indent=4, sort_keys=True))
        if arguments == {}:
            contents = su.read_template_html_file("./HTML/ERROR.html").render(context=context)
            return contents
        else:
            limit = int(arguments["limit"][0])
            context["limit"] = limit
            if limit <= amount_species or limit == amount_species:
                for n in range(0, limit):
                    species_list.append(response_dict["species"][n]["common_name"])
                context["names"] = species_list
            else:
                for n in range(0, amount_species):
                    species_list.append(response_dict["species"][n]["common_name"])
                context["names"] = species_list
            if "json" in arguments.keys():
                if arguments["json"][0] == "1":
                    # return str(context)
                    with open("context.json", "w") as file:
                        json.dump(context, file, indent=4)
                    return file
            else:
                contents = su.read_template_html_file("./HTML/info/list_species.html").render(context=context)
                return contents


def karyotype(connection, ENDPOINT, PARAMS, arguments, context):
    specie = taking_out_space(arguments["species"][0])
    connection.request("GET", ENDPOINT + specie + PARAMS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        # print(json.dumps(response_dict, indent=4, sort_keys=True))
        karyotype = response_dict["karyotype"]
        # print(karyotype)
        context["species"] = arguments["species"][0]
        context["karyotype"] = karyotype
        contents = su.read_template_html_file("./HTML/info/karyotype.html").render(context=context)
        return contents


def chromosome_length(connection, ENDPOINT, PARAMS, arguments, context):
    specie = taking_out_space(arguments["species"][0])
    connection.request("GET", ENDPOINT + specie + PARAMS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        chromosome = arguments["chromosome"][0]
        # print(json.dumps(response_dict, indent=4, sort_keys=True))
        for n in range(0, len(response_dict["top_level_region"])):
            if chromosome == response_dict["top_level_region"][n]["name"]:
                length = response_dict["top_level_region"][n]["length"]
        # print(length)
        context["species"] = arguments["species"][0]
        context["chromosome"] = chromosome
        context["length"] = length
        contents = su.read_template_html_file("./HTML/info/chromosome_length.html").render(context=context)
        return contents


def geneSeq(connection, ENDPOINT, PARAMS, arguments, context, DICT_GENES):
    gene = arguments["gene"][0]
    id = DICT_GENES[gene]
    connection.request("GET", ENDPOINT + id + PARAMS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        print(json.dumps(response_dict, indent=4, sort_keys=True))
        context["gene"] = arguments["gene"][0]
        context["seq"] = response_dict["seq"]
        contents = su.read_template_html_file("HTML/Info/geneSeq.html").render(context=context)
        return contents


def geneInfo(connection, ENDPOINT, PARAMS, arguments, context, DICT_GENES):
    gene = arguments["gene"][0]
    id = DICT_GENES[gene]
    connection.request("GET", ENDPOINT + id + PARAMS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        print(json.dumps(response_dict, indent=4, sort_keys=True))
        info = response_dict["desc"].split(":")
        context["gene"] = gene
        context["dict_info"] = {
            "Name": info[1],
            "ID": id,
            "Start": info[3],
            "End": info[4],
            "Length": (int(info[4]) - int(info[3]) + 1)
        }
        contents = su.read_template_html_file("HTML/Info/geneInfo.html").render(context=context)
        return contents


def geneCalc(connection, ENDPOINT, PARAMS, arguments, context, DICT_GENES):
    gene = arguments["gene"][0]
    id = DICT_GENES[gene]
    connection.request("GET", ENDPOINT + id + PARAMS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        print(json.dumps(response_dict, indent=4, sort_keys=True))
        sequence = Seq(response_dict["seq"])
        dict_bases, percentage_list = Seq.count_base_2(sequence)
        context["length"] = Seq.len(sequence)
        context["bases"] = {
            "A": str(dict_bases["A"]) + " (" + str(percentage_list[0]) + "%)",
            "C": str(dict_bases["C"]) + " (" + str(percentage_list[1]) + "%)",
            "T": str(dict_bases["T"]) + " (" + str(percentage_list[2]) + "%)",
            "G": str(dict_bases["G"]) + " (" + str(percentage_list[3]) + "%)"
        }
        contents = su.read_template_html_file("HTML/Info/geneCalc.html").render(context=context)
        return contents