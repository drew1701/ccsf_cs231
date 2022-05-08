#!/usr/bin/env python3
"""
Homework 13:
    Use http.server to serve the output of the program date -R on
    an available high port number. Tell the user what the port number
    is so that they can access the service.
"""
import signal
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import os


# Define function to handle control-c exit gracefully.
def er_handler(signum, frame):
    print('\nHTTP Server Stopped Successfully')
    sys.exit(0)


# Create custom GET handler to display output of 'date -R' command.
class WebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Runs linux shell command and saves output as message.
        with os.popen("date -R") as command:
            message = command.read()

        self.wfile.write(bytes(message, "utf8"))


# Use signal to capture control-c (SIGINT).
signal.signal(signal.SIGINT, er_handler)

# Show user how to connect to service and exit server.
print("The python webserver is running on port: 62345\n")
print("Please use a separate terminal window and enter")
print("'curl http://localhost:62345' to test the server.\n")
print("To stop the server use CTRL-C or close the terminal window.\n")

# Start server on localhost at port 62345 using our custom handler.
with HTTPServer(('', 62345), WebHandler) as server:
    server.serve_forever()
