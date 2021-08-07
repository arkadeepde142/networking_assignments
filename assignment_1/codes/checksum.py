def checksum_generator(message: bytes) -> bytes:
    sum = 0

    for byte in message:
        sum += byte

    while (sum >> 8) > 0:
        sum = (sum >> 8) + (sum & 255)

    return message + bytes([255 - sum])

def checksum_checker(message: bytes) -> bool:
    sum = 0

    for byte in message:
        sum += byte

    while (sum >> 8) > 0:
        sum = (sum >> 8) + (sum & 255)
    return sum == 255 or sum == 0

if __name__ == '__main__':
    message = b"Hi there"
    dataframe = checksum_generator(message)
    print(checksum_checker(dataframe))