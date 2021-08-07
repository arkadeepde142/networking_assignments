import math

def crc_generate(message: bytes, key: int):
    key_length = math.ceil(math.log(key, 2))
    num = int.from_bytes(message, 'big')
    remainder = num
    while math.ceil(math.log(remainder, 2)) > key_length:
        length = math.ceil(math.log(remainder, 2)) - key_length
        remainder ^= (key << length)
    encoded = ((num << (key_length-1)) + remainder)
    return encoded.to_bytes(1 + math.ceil(math.log(encoded, 2)), 'big')

if __name__ == 'main':
    print(bin(int.from_bytes(crc_generate(b'abc', 5), 'big')))