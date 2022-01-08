import socket


HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)

conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data)

conn.close()
