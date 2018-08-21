#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import json
from sys import argv
import base64

class S(BaseHTTPRequestHandler):

    def logg(self):
        time = self.date_time_string() 
        ip = self.address_string()
        msg = "Connected By [{}] At [{}]".format(ip, time)
        #print(msg)

    def send_pool_info(self):
        self.pool_name = "teste2"
        self.pool_key = "teste"
        return self.pool_key, self.pool_name

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        pool_info = json.dumps(self.send_pool_info())
        self.wfile.write(pool_info)
        self.logg()
        
    def do_POST(self):
        # Gets the size of data
        content_length = int(self.headers['Content-Length']) 
        
        # Gets the data itself
        post_data = self.rfile.read(content_length) 
        post_data = base64.decodestring(post_data)
        
        self.logg()
        print("\nMSG [{}]".format(post_data))
        self._set_headers()
        self.wfile.write("eae men")
        
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting web server...'
    httpd.serve_forever()

if __name__ == "__main__":
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()