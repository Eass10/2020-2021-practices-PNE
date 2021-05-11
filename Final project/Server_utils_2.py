import http.server
import socketserver
import termcolor
import colorama
import Server_utils as su
from urllib.parse import urlparse, parse_qs
import http.client
import json


def list_seqs (connection, ENDPOINT, PARAMS, arguments, context):
    connection.request("GET", ENDPOINT + PARAMS)
    response = connection.getresponse()
    if response.status == 200:
        response_dict = json.loads(response.read().decode())
        species_list = []
        amount_species = len(response_dict["species"])
        limit = int(arguments["limit"][0])
        # print(json.dumps(response_dict, indent=4, sort_keys=True))
        if limit <= amount_species or limit == amount_species:
            for n in range(0, limit):
                species_list.append(response_dict["species"][n]["common_name"])
            context["names"] = species_list

        else:
            for n in range(0, amount_species):
                species_list.append(response_dict["species"][n]["common_name"])
            context["names"] = species_list
        context["amount_species"] = amount_species
        context["limit"] = limit
        contents = su.read_template_html_file("./HTML/info/list_species.html").render(context=context)
        return contents


def karyotype(connection, ENDPOINT, PARAMS, arguments, context):
    connection.request("GET", ENDPOINT + arguments["species"][0] + PARAMS)
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
    connection.request("GET", ENDPOINT + arguments["species"][0] + PARAMS)
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
