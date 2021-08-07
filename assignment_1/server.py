import socket
from codes import checksum

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 6000))
s.listen(1)

with s:
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                len(data)
                data_as_int = int.from_bytes(data, byteorder='big')
                data = int.to_bytes(int.from_bytes(data, byteorder='big') ^ 1, len(data) + 1, byteorder='big')
                if not data:
                    break
                conn.sendall(str(checksum.checksum_checker(data)).encode('utf'))

