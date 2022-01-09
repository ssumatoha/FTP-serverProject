import socket
from FileManagerInterface import start, process
from FileManagerClass import FileManager
import pickle

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)

conn, addr = sock.accept()

p = FileManager()
start(p)

while True:
    data = conn.recv(1024)
    if not data:
        break
    data_out = process(p, pickle.loads(data))
    conn.send(pickle.dumps(data_out))

conn.close()
