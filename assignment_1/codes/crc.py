import math

def crc_generator(message: bytes, key: int) -> bytes:
    key_length = math.ceil(math.log(key, 2))
    num = int.from_bytes(message, 'big')
    remainder = num << (key_length-1)
    while remainder > 0 and math.ceil(math.log(remainder, 2)) >= key_length:
        length = math.ceil(math.log(remainder, 2)) - key_length
        remainder ^= (key << length)
        # print(format(remainder, f'0{math.ceil(math.log(num, 2)) + key_length - 1}b'))
    # print(remainder)
    encoded = ((num << (key_length-1)) + remainder)
    return encoded.to_bytes(1 + math.ceil(math.log(encoded, 2)), 'big')

def crc_checker(message: bytes, key: int) -> bool:
    key_length = math.ceil(math.log(key, 2))
    num = int.from_bytes(message, 'big')
    remainder = num
    while remainder > 0 and math.ceil(math.log(remainder, 2)) >= key_length:
        length = math.ceil(math.log(remainder, 2)) - key_length
        remainder ^= (key << length)
        # print(format(remainder, f'0{math.ceil(math.log(num, 2))}b'))
    return remainder == 0

if __name__ == '__main__':
    print(format(int.from_bytes(b'Hi,there', 'big'), 'b'))
    value = format(int.from_bytes(crc_generator(b'Hi,there', 0xD31), 'big'), 'b')
    print(value)
    num = int(value, 2)
    error = num ^ ((1<<40)+ (1<<43))
    print(format(error, 'b'))
    print(crc_checker(error.to_bytes(10, 'big'), 11))
    