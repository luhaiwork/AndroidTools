import http.server
import socketserver
class httpServHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'html')
        self.end_headers()
        self.wfile.write(bytes("<html> <head><title> Hello World </title> </head> <body>sss</body>", 'UTF-8'))
PORT = 8888
Handler = httpServHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
