from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime


class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        if self.path.endswith('/time'):
            output = ''
            output += '<html><body>'
            output = str(datetime.datetime.now().time())      #check user if in url
            output += '</body></html>'
            self.wfile.write(output.encode())
            response = open('resssss.txt', 'w')
            response.write(output)
            response.close()

        if self.path.endswith('/date'):
            output = ''                                         #check user if in url
            output += '<html><body>'
            output = str(datetime.datetime.now().date())
            output += '</body></html>'
            self.wfile.write(output.encode())
            # write file

def main():
    PORT = 9000
    server = HTTPServer(('', PORT), requestHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()



if __name__ == "__main__":
    main()
