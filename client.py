import socket
import pickle

HEADERSIZE = 10
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.103"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = client.recv(16)
        if new_msg:
            print(f'new message length: {msg[:HEADERSIZE]}')
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg) - HEADERSIZE == msglen:
            print('full msg recvd')
            print(full_msg[HEADERSIZE:])

            bfolder = pickle.loads(full_msg[HEADERSIZE:])
            print(bfolder)


            new_msg = True
            full_msg = ''

    print(full_msg)