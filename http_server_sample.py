__author__ = 'izeye'

import BaseHTTPServer

HOST_NAME = 'localhost'
PORT_NUMBER = 28080

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        print "Hello, world!"
        self.send_response(200)

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    httpd.serve_forever()
