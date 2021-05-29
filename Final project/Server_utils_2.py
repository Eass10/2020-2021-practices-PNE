import Server_utils as su
import json
from Seq import Seq


def taking_out_space(specie):
    answer = specie.replace(" ", "_")
    return answer


def list_species(connection, ENDPOINT, PARAMS, arguments, context):
    connection.request("GET", ENDPOINT + PARAMS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        # print(json.dumps(response_dict, indent=4, sort_keys=True))
        if arguments == {}:
            cont_type = 'text/html'
            context["limit"] = "ERROR"
            contents = su.read_template_html_file("./HTML/info/list_species.html").render(context=context)
            return contents, cont_type
        elif len(arguments.keys()) == 1 and "json" in arguments.keys():
            cont_type = 'application/json'
            context["limit"] = "ERROR"
            contents = json.dumps(context, indent=4, sort_keys=True)
            return contents, cont_type
        else:
            species_list = []
            amount_species = len(response_dict["species"])
            context["amount_species"] = amount_species
            limit = int(arguments["limit"][0])
            context["limit"] = limit
            if limit < amount_species:
                for n in range(0, limit):
                    species_list.append(response_dict["species"][n]["common_name"])
                context["names"] = species_list
            else:
                for n in range(0, amount_species):
                    species_list.append(response_dict["species"][n]["common_name"])
                context["names"] = species_list
            if "json" in arguments.keys():
                if arguments["json"][0] == "1":
                    cont_type = 'application/json'
                    contents = json.dumps(context, indent=4, sort_keys=True)
                    return contents, cont_type
            else:
                cont_type = 'text/html'
                contents = su.read_template_html_file("./HTML/info/list_species.html").render(context=context)
                return contents, cont_type


def karyotype(connection, ENDPOINT, PARAMS, arguments, context):
    try:
        specie = taking_out_space(arguments["species"][0])
    except KeyError:
        if len(arguments.keys()) == 0:
            cont_type = 'text/html'
            context["karyotype"] = "ERROR"
            contents = su.read_template_html_file("./HTML/info/karyotype.html").render(context=context)
            return contents, cont_type
        elif len(arguments.keys()) == 1:
            cont_type = 'application/json'
            context["karyotype"] = "ERROR"
            contents = json.dumps(context, indent=4, sort_keys=True)
            return contents, cont_type
    connection.request("GET", ENDPOINT + specie + PARAMS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        # print(json.dumps(response_dict, indent=4, sort_keys=True))
        karyotype = response_dict["karyotype"]
        # print(karyotype)
        context["species"] = arguments["species"][0]
        context["karyotype"] = karyotype
        if "json" in arguments.keys():
            if arguments["json"][0] == "1":
                cont_type = 'application/json'
                contents = json.dumps(context, indent=4, sort_keys=True)
                return contents, cont_type
        else:
            cont_type = 'text/html'
            contents = su.read_template_html_file("./HTML/info/karyotype.html").render(context=context)
            return contents, cont_type


def chromosome_length(connection, ENDPOINT, PARAMS, arguments, context):
    try:
        specie = taking_out_space(arguments["species"][0])
    except KeyError:
        if len(arguments.keys()) == 0:
            cont_type = 'text/html'
            context["length"] = "ERROR"
            contents = su.read_template_html_file("./HTML/info/chromosome_length.html").render(context=context)
            return contents, cont_type
        elif len(arguments.keys()) == 1:
            if "chromosome" in arguments.keys():
                cont_type = 'text/html'
                context["length"] = "ERROR 2"
                contents = su.read_template_html_file("./HTML/info/chromosome_length.html").render(context=context)
                return contents, cont_type
            if "json" in arguments.keys():
                cont_type = 'application/json'
                context["length"] = "ERROR"
                contents = json.dumps(context, indent=4, sort_keys=True)
                return contents, cont_type
        elif len(arguments.keys()) == 2:
            cont_type = 'application/json'
            context["length"] = "ERROR 2"
            contents = json.dumps(context, indent=4, sort_keys=True)
            return contents, cont_type
    connection.request("GET", ENDPOINT + specie + PARAMS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        try:
            chromosome = arguments["chromosome"][0]
            # print(json.dumps(response_dict, indent=4, sort_keys=True))
        except KeyError:
            if len(arguments.keys()) == 1:
                if "species" in arguments.keys():
                    cont_type = 'text/html'
                    context["length"] = "ERROR 1"
                    contents = su.read_template_html_file("./HTML/info/chromosome_length.html").render(context=context)
                    return contents, cont_type
                if "json" in arguments.keys():
                    cont_type = 'application/json'
                    context["length"] = "ERROR"
                    contents = json.dumps(context, indent=4, sort_keys=True)
                    return contents, cont_type
            elif len(arguments.keys()) == 2:
                cont_type = 'application/json'
                context["length"] = "ERROR 1"
                contents = json.dumps(context, indent=4, sort_keys=True)
                return contents, cont_type
        for n in range(0, len(response_dict["top_level_region"])):
            if chromosome == response_dict["top_level_region"][n]["name"]:
                length = response_dict["top_level_region"][n]["length"]
        # print(length)
        context["species"] = arguments["species"][0]
        context["chromosome"] = chromosome
        context["length"] = length
        if "json" in arguments.keys():
            if arguments["json"][0] == "1":
                cont_type = 'application/json'
                contents = json.dumps(context, indent=4, sort_keys=True)
                return contents, cont_type
        else:
            cont_type = 'text/html'
            contents = su.read_template_html_file("./HTML/info/chromosome_length.html").render(context=context)
            return contents, cont_type


def geneSeq(connection, ENDPOINT, PARAMS, arguments, context, DICT_GENES):
    try:
        gene = arguments["gene"][0]
    except KeyError:
        if len(arguments.keys()) == 0:
            cont_type = 'text/html'
            context["seq"] = "ERROR"
            contents = su.read_template_html_file("./HTML/info/geneSeq.html").render(context=context)
            return contents, cont_type
        elif len(arguments.keys()) == 1:
            cont_type = 'application/json'
            context["seq"] = "ERROR"
            contents = json.dumps(context, indent=4, sort_keys=True)
            return contents, cont_type
    id = DICT_GENES[gene]
    connection.request("GET", ENDPOINT + id + PARAMS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        # print(json.dumps(response_dict, indent=4, sort_keys=True))
        context["gene"] = arguments["gene"][0]
        context["seq"] = response_dict["seq"]
        if "json" in arguments.keys():
            if arguments["json"][0] == "1":
                cont_type = 'application/json'
                contents = json.dumps(context, indent=4, sort_keys=True)
                return contents, cont_type
        else:
            cont_type = 'text/html'
            contents = su.read_template_html_file("./HTML/info/geneSeq.html").render(context=context)
            return contents, cont_type


def geneInfo(connection, ENDPOINT, PARAMS, arguments, context, DICT_GENES):
    try:
        gene = arguments["gene"][0]
    except KeyError:
        if len(arguments.keys()) == 0:
            cont_type = 'text/html'
            context["dict_info"] = "ERROR"
            contents = su.read_template_html_file("./HTML/info/geneInfo.html").render(context=context)
            return contents, cont_type
        elif len(arguments.keys()) == 1:
            cont_type = 'application/json'
            context["dict_info"] = "ERROR"
            contents = json.dumps(context, indent=4, sort_keys=True)
            return contents, cont_type
    id = DICT_GENES[gene]
    connection.request("GET", ENDPOINT + id + PARAMS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        # print(json.dumps(response_dict, indent=4, sort_keys=True))
        info = response_dict["desc"].split(":")
        context["gene"] = gene
        context["dict_info"] = {
            "Name": info[2],
            "ID": id,
            "Start": info[3],
            "End": info[4],
            "Length": (int(info[4]) - int(info[3]) + 1)
        }
        if "json" in arguments.keys():
            if arguments["json"][0] == "1":
                cont_type = 'application/json'
                contents = json.dumps(context, indent=4, sort_keys=True)
                return contents, cont_type
        else:
            cont_type = 'text/html'
            contents = su.read_template_html_file("./HTML/info/geneInfo.html").render(context=context)
            return contents, cont_type


def geneCalc(connection, ENDPOINT, PARAMS, arguments, context, DICT_GENES):
    try:
        gene = arguments["gene"][0]
    except KeyError:
        if len(arguments.keys()) == 0:
            cont_type = 'text/html'
            context["bases"] = "ERROR"
            contents = su.read_template_html_file("./HTML/info/geneCalc.html").render(context=context)
            return contents, cont_type
        elif len(arguments.keys()) == 1:
            cont_type = 'application/json'
            context["bases"] = "ERROR"
            contents = json.dumps(context, indent=4, sort_keys=True)
            return contents, cont_type
    id = DICT_GENES[gene]
    connection.request("GET", ENDPOINT + id + PARAMS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        # print(json.dumps(response_dict, indent=4, sort_keys=True))
        sequence = Seq(response_dict["seq"])
        dict_bases, percentage_list = Seq.count_base_2(sequence)
        context["gene"] = gene
        context["length"] = Seq.len(sequence)
        context["bases"] = {
            "A": str(dict_bases["A"]) + " (" + str(percentage_list[0]) + "%)",
            "C": str(dict_bases["C"]) + " (" + str(percentage_list[1]) + "%)",
            "T": str(dict_bases["T"]) + " (" + str(percentage_list[2]) + "%)",
            "G": str(dict_bases["G"]) + " (" + str(percentage_list[3]) + "%)"
        }
        if "json" in arguments.keys():
            if arguments["json"][0] == "1":
                cont_type = 'application/json'
                contents = json.dumps(context, indent=4, sort_keys=True)
                return contents, cont_type
        else:
            cont_type = 'text/html'
            contents = su.read_template_html_file("./HTML/info/geneCalc.html").render(context=context)
            return contents, cont_type