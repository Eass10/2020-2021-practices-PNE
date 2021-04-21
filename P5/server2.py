import http.server
import socketserver
import termcolor
import colorama
from pathlib import Path
from jinja2 import Template

# Define the Server's port
PORT = 8080
HTML_ASSETS = "./HTML/info/"
HTML = "./HTML/"
BASES_INFORMATION = {
    "A": {"name": "ADENINE",
          "formula": "C5H5N5",
          "link": "https://en.wikipedia.org/wiki/Adenine",
          "color": "lightgreen"},
    "C": {"name": "CITOSINE",
          "formula": "C4H5N3O",
          "link": "https://en.wikipedia.org/wiki/Citosine",
          "color": "yellow"},
    "G": {"name": "GUANINE",
          "formula": "C5H5N5O",
          "link": "https://en.wikipedia.org/wiki/Guanine",
          "color": "lightblue"},
    "T": {"name": "TIMINE",
          "formula": "C5H5N2O2",
          "link": "https://en.wikipedia.org/wiki/Timine",
          "color": "pink"}
}
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


def read_html_file(filename):
    return Path(filename).read_text()


def read_template_html_file(filename):
    content = Template(Path(filename).read_text())
    return content

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        global contents
        colorama.init(strip="False")
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok
        # Message to send back to the client
        if self.path == "/":
            contents = read_html_file(HTML + "index.html")
        elif "/info/" in self.path:
            base = self.path.split("/")[-1]
            context = BASES_INFORMATION[base]
            context["letter"] = base
            contents = read_template_html_file(HTML_ASSETS + "General.html").render(base_info=context)
        elif self.path.endswith(".html"):
            try:
                contents = read_html_file(HTML + self.path)
            except FileNotFoundError:
                contents = read_html_file(HTML + "ERROR.html")
        else:
            contents = read_html_file(HTML + "ERROR.html")

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