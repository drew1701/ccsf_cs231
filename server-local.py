# hw13 http.server test, code from:
# https://flaviocopes.com/python-http-server/

from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = "Hello, World!"
        self.wfile.write(bytes(message, "utf8"))


with HTTPServer(('', 62345), Handler) as server:
    server.serve_forever()
