import socket, pickle, sys

HOST = 'mxrydev.com'
PORT = 12354

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

if __name__ == "__main__":
    while True:
        data = s.recv(1024)
        data = pickle.loads(data)
        print (data)