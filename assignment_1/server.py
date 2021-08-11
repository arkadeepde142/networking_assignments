import socket
import math
from codes import vrc, lrc, checksum, crc

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 6000))
s.listen(1)
global checker
key = 0b10011
with s:
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                if data == b'FUNCTION: LRC':
                    checker = lrc.lrc_checker
                    conn.sendall(b'DONE')
                elif data == b'FUNCTION: VRC':
                    checker = vrc.vrc_checker
                    conn.sendall(b'DONE')
                elif data == b'FUNCTION: CHECKSUM':
                    checker = checksum.checksum_checker
                    conn.sendall(b'DONE')
                elif data == b'FUNCTION: CRC':
                    checker = lambda frame: crc.crc_checker(frame, key)
                    conn.sendall(b'DONE')
                else:
                    conn.sendall(str(checker(data)).encode())

