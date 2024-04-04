
import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 8888        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(b'Hello, world')
        data = s.recv(64)
        print('Received', repr(data))

