import socket
import codes.checksum

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 6000))
s.sendall(codes.checksum.checksum_generator(b'Hello,- World'))
data = s.recv(1024)
s.close()
print('Received', bool(data))