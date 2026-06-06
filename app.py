#!/usr/bin/env python3
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # If requesting root or directory, serve index.html or one.html
        if self.path == '/' or self.path == '':
            self.path = '/one.html'
        return SimpleHTTPRequestHandler.do_GET(self)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super().end_headers()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print(f'Server running on port {port}')
    httpd.serve_forever()
