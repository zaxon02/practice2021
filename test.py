import socket
import pickle
from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime

CLIENTS = {'user1': '111.000.0.000', 'user2': '111.111.0.111'}

HEADERSIZE = 10
PORT = 9090
#ADDR = (SERVER, PORT)


class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        device_url = self.path.split('/')
        print(str(device_url[-1]))


        if self.path.endswith('/time'):
            output = "OK" + ' ' + str(datetime.datetime.now().time())
            self.wfile.write(output.encode())
            response = open('res.txt', 'w')
            response.write(output)
            response.close()

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print("Server is running")

            d = output
            msg = pickle.dumps(d)

            msg = bytes(f"{len(msg):<{HEADERSIZE}}", "utf-8") + msg

            x = s.sendto(msg, (CLIENTS['user1'], PORT))
            s.close()

        #if self.path.endswith('/time'):
           # output = ''
           # output += '<html><body>'
           # output = str(datetime.datetime.now().time())
           # output += '</body></html>'
           # self.wfile.write(output.encode())
           # response = open('request.txt', 'w')
           # response.write(output)
            #response.close()

        if self.path.endswith('/date'):
            output = ''
            output += '<html><body>'
            output = str(datetime.datetime.now().date())
            output += '</body></html>'
            self.wfile.write(output.encode())
            response = open('request.txt', 'w')
            response.write(output)
            response.close()


def main():
    PORT = 8000
    server = HTTPServer(('', PORT), requestHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()

if __name__ == "__main__":
    main()

