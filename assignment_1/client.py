import socket
import random
from math import ceil
from codes import vrc, lrc, crc, checksum
from functools import reduce

def inject_error(message: bytes, swaps: set) -> bytes:
    binary_string: str = reduce(
        lambda final, byte: final + format(byte, '08b'),
        message,
        '')
    swap_string = reduce(lambda final, index: xor(final, '1' + '0' * index), swaps, '0')
    return int(xor(binary_string, swap_string), 2).to_bytes(len(message), 'big')

xor = lambda a, b: format(int(a, 2) ^ int(b, 2), f'0{max((len(a), len(b)))}b')

repetitions = int(input('Enter the number of repetitions: '))
num_swaps = int(input('Enter the number of swaps: '))
print('Enter 1 for VRC\nEnter 2 for LRC\nEnter 3 for Checksum\nEnter 4 for CRC')
choice = int(input('Enter the choice: '))
results = 0
global encoding
key = 0b10011
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 6000))
    if choice == 1:
        encoding = vrc.vrc_generator
        s.sendall(b'FUNCTION: VRC')
    elif choice == 2:
        encoding = lrc.lrc_generator
        s.sendall(b'FUNCTION: LRC')
    elif choice == 3:
        encoding = checksum.checksum_generator
        s.sendall(b'FUNCTION: CHECKSUM')
    elif choice == 4:
        encoding = lambda frame: crc.crc_generator(frame, key)
        s.sendall(b'FUNCTION: CRC')
    else:
        exit(1)
    status = s.recv(1024)
    if status != b'DONE':
        exit(1)
    
    with open('data.txt') as file:
        data = file.read().encode()
        frames = []
        i = 0
        while len(frames) < ceil(len(data)/8):
            frames.append(data[i: min(len(data), (i+8))])
            i += 8
        # print(frames)
        frames = list(map(lambda byte: byte + bytes((8 - len(byte)) * [0]), frames))
        for _ in range(repetitions):
            for frame in frames:
                frame = encoding(frame)
                swaps: set = set()
                while len(swaps) < num_swaps:
                    swaps.add(random.randint(0, 63))
                frame = inject_error(frame, swaps)
                s.sendall(frame)
                received = s.recv(1024)
                if received.decode() == 'False':
                    results += 1
print(f'Score: {results}')

