#!/usr/bin/env python3
"""
Drew Patrick
CS231 Advanced Python
Homework 13: Task:
    Use http.server to serve the output of the program date -R on
    an available high port number. Tell the user what the port number
    is so that they can access the service.
"""
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        with os.popen("date -R") as command:
            message = command.read()

        self.wfile.write(bytes(message, "utf8"))


with HTTPServer(('hills.ccsf.edu', 62345), Handler) as server:
    server.serve_forever()
