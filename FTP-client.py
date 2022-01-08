import socket
import pickle

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

while True:
    command = str(input('введите комманду '))
    sock.send(pickle.dumps(command))
    if command == 'q':
        break
    data = sock.recv(1024)
    print(pickle.loads(data))

sock.close()
