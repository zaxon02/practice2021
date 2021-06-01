import socket
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
print("HOSTNAME IS --------> ", socket.gethostname())
s.listen(5)

while True:
    clientsocket, adress = s.accept()
    print(f"Connection from {adress} has been established!")
    print(clientsocket, " ", adress)

    d ="resssss.txt"
    msg = pickle.dumps(d)
    #print(msg)

    #msg = 'Welcome to the server!'
    #msg = check
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", "utf-8") + msg

    clientsocket.send(msg)
