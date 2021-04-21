import http.server
import socketserver
import termcolor
import colorama
from pathlib import Path

# Define the Server's port
PORT = 8080
HTML_ASSETS = "./HTML/info/"
HTML = "./HTML/"
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


def read_html_file(filename):
    return Path(filename).read_text()

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
        path_name = self.path.split(".")[0]
        if path_name == "/" or path_name == "/index":
            contents = read_html_file(HTML + "index.html")
        elif "/info/" in path_name:
            try:
                contents = read_html_file(HTML_ASSETS + str(path_name[-1]) + ".html")
            except FileNotFoundError:
                contents = read_html_file(HTML + "ERROR.html")

        """if self.path == "/info/A" or self.path == "/info/A.html":
            contents = read_html_file(HTML_ASSETS + "A.html")
        elif self.path == "/info/C" or self.path == "/info/C.html":
            contents = read_html_file(HTML_ASSETS + "C.html")
        elif self.path == "/info/T" or self.path == "/info/T.html":
            contents = read_html_file(HTML_ASSETS + "T.html")
        elif self.path == "/info/G" or self.path == "/info/G.html":
            contents = read_html_file(HTML_ASSETS + "G.html")
        else:
            contents = read_html_file(HTML + "ERROR.html")"""

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
