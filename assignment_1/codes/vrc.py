def vrc_check(message: bytes) -> bool:
    xorresult = 0
    for byte in message:
        xorresult ^= byte
    result = 0
    while xorresult > 0:
        result += xorresult & 1
        xorresult >>= 1
    return result % 2 == 0

def vrc_generator(message: bytes) -> bytes:
    xorresult = 0
    for byte in message:
        xorresult ^= byte
    result = 0
    while xorresult > 0:
        result += xorresult & 1
        xorresult >>= 1
    return message + bytes([result % 2])

if __name__ == '__main__':
    a = vrc_generator(b"a")
    print(format(int.from_bytes(a, "big"), 'b'))
    print(vrc_check(a))
