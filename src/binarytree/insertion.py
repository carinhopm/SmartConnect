#!/usr/bin/python

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

"""
Run HTTP Server
"""
def runHttpServer(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()
    return httpd

"""
Stop HTTP Server
"""
def stopHttpServer(httpd):
    httpd.server_close()
    print('Stopping httpd...')

"""
Insertion function
"""
def insert(root, key, value):
    if root==None:
        root = Node(key, value)
    elif key==root.key:
        root.value = value
    elif key<root.key:
        root.left = insert(root.left, key, value)
    else:
        root.right = insert(root.right, key, value)
    return root

"""
Node object
"""
class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.element = value
        self.left = None
        self.right = None

"""
HTTP Handler
"""
class S(BaseHTTPRequestHandler):
    def _set_response(self, root):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length)#.decode('utf-8') # <--- Gets the data itself
        printf("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data)
        try:
            message = json.loads(post_data)
            tree = message['tree']
            value = message['value']
            response = updateTree(tree, value)
            self._set_response()
            self.wfile.write(json.dumps(message))
        except:
            self.send_response(402)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": 402, "message": "Wrong request" }))
    
    def updateTree(tree, value):
        newTree = {"message": "default response"}
        return newTree
