import http.server
import socketserver
import termcolor
import colorama
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from jinja2 import Template

# Define the Server's port
PORT = 8080
HTML = "./HTML/"

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
        colorama.init(strip=False)
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        # Open the form1.html file
        # Read the index from the file
        if self.path == "/" or self.path == "/echo":
            try:
                contents = read_html_file(HTML + "form-1.html")
            except FileNotFoundError:
                contents = read_html_file(HTML + "ERROR.html")
        elif self.path.startswith("/echo?msg"):
            # msg = self.path.split('?msg=')[1]
            msg = parse_qs(urlparse(self.path).query)["msg"][0]
            print("Message:", termcolor.colored(msg, "blue"))
            try:
                # contents = read_html_file(HTML + 'template.html').format(msg)
                contents = read_template_html_file(HTML + 'template_jinja.html').render(msg=msg)
            except FileNotFoundError:
                contents = read_html_file(HTML + "ERROR.html")
        else:
            contents = read_html_file(HTML + "ERROR.html")

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

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