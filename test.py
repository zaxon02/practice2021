import socket
import pickle
from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime

ip = ['222.222.0.222', '111.111.0.111']

HEADERSIZE = 10
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER, PORT)
print(SERVER)


class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        device_url = self.path.split('/')
        print(str(device_url[-1]))
        for i in ip:
            if i == device_url[-1]:
                print("your i is", i)

        for i in ip:
            if self.path.endswith('/time/' + i):
                output = "OK" + ' ' + str(datetime.datetime.now().time())
                self.wfile.write(output.encode())
                response = open('res.txt', 'w')
                response.write(output)
                response.close()

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind(ADDR)
                print("HOSTNAME IS --------> ", socket.gethostname())
                s.listen(5)

                while True:
                    clientsocket, adress = s.accept()
                    print(f"Connection from {adress} has been established!")
                    print(clientsocket, " ", adress)

                    d = output
                    msg = pickle.dumps(d)

                    msg = bytes(f"{len(msg):<{HEADERSIZE}}", "utf-8") + msg

                    clientsocket.send(msg)

        if self.path.endswith('/time'):
            output = ''
            output += '<html><body>'
            output = str(datetime.datetime.now().time())
            output += '</body></html>'
            self.wfile.write(output.encode())
            response = open('request.txt', 'w')
            response.write(output)
            response.close()

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

