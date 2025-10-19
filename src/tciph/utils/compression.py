from base64 import b85decode, b85encode


def compress(char):
    return b85encode(char.encode()).decode()


def decompress(char):
    return b85decode(char.encode()).decode()
