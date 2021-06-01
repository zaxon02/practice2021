import socket
import pickle

HEADERSIZE = 10
PORT = 9090
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', PORT))

    while True:
        full_msg = b''
        new_msg = True
        while True:
            msg = s.recv(1024)
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
                full_msg = b''

                file = open('res.txt', 'w')
                file.write(str(full_msg))
                file.close()

        print(full_msg)

if __name__ == "__main__":
    main()