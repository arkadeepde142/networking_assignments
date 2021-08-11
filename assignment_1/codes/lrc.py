from functools import reduce


def lrc_generator(message: bytes) -> bytes:
    binary_string: str = reduce(
        lambda final, byte: final + format(byte, '08b'),
        message,
        '')
    
    length = len(binary_string)
    lrc_packet = ''
    for i in range(8):
        j = 0
        bit = '0'
        while(i + j * 8 < length):
            bit = xor(bit, binary_string[i + j * 8])
            j += 1
        lrc_packet += bit
    binary_num = int(binary_string + lrc_packet, 2)
    message = int.to_bytes(binary_num, len(message) + 1, byteorder='big')
    return message

def lrc_checker(message: bytes) -> bool:
    binary_string: str = reduce(
        lambda final, byte: final + format(byte, '08b'),
        message,
        '')
    
    length = len(binary_string)
    lrc_packet = ''
    for i in range(8):
        j = 0
        bit = '0'
        while(i + j * 8 < length):
            bit = xor(bit, binary_string[i + j * 8])
            j += 1
        lrc_packet += bit
    return lrc_packet == ('0' * 8)


xor = lambda a, b: format(int(a, 2) ^ int(b, 2), f'0{max((len(a), len(b)))}b')

if __name__ == '__main__':
    print(lrc_checker(b'HelloB'))