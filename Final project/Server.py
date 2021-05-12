import http.server
import socketserver
import termcolor
import colorama
import Server_utils as su
import Server_utils_2 as su2
from urllib.parse import urlparse, parse_qs
import http.client


# Define the Server's port
PORT = 8080

HTML_ASSETS = "./HTML/info/"
HTML = "./HTML/"

DICT_GENES = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000226906",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

SERVER = "rest.ensembl.org"
PARAMS = "?content-type=application/json"

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        global contents
        colorama.init(strip="False")
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        connection = http.client.HTTPConnection(SERVER)

        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters: ", arguments)
        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok
        # Message to send back to the client
        context = {}
        try:
            if path_name == "/":
                context["genes"] = DICT_GENES.keys()
                contents = su.read_template_html_file(HTML_ASSETS + "index.html").render(context=context)
            elif path_name == "/listSpecies":
                ENDPOINT = "/info/species"
                contents = su2.list_seqs(connection, ENDPOINT, PARAMS, arguments, context)
            elif path_name == "/karyotype":
                ENDPOINT = "info/assembly/"
                contents = su2.karyotype(connection, ENDPOINT, PARAMS, arguments, context)
            elif path_name == "/chromosomeLength":
                ENDPOINT = "info/assembly/"
                contents = su2.chromosome_length(connection, ENDPOINT, PARAMS, arguments, context)
            elif path_name == "/geneSeq":
                ENDPOINT = "/sequence/id/"
                contents = su2.geneSeq(connection, ENDPOINT, PARAMS, arguments, context, DICT_GENES)
            elif path_name == "/geneInfo":
                ENDPOINT = "/sequence/id/"
                contents = su2.geneInfo(connection, ENDPOINT, PARAMS, arguments, context, DICT_GENES)
            elif path_name == "/geneCalc":
                ENDPOINT = "/sequence/id/"
                contents = su2.geneCalc(connection, ENDPOINT, PARAMS, arguments, context, DICT_GENES)
            else:
                contents = su.read_template_html_file(HTML + "ERROR.html").render()
        except KeyError:
            contents = su.read_template_html_file(HTML + "ERROR.html").render()


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!
        length = len(contents.encode())
        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(length))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()