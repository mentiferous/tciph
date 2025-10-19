from base64 import b85decode, b85encode


def encode(char):
    return b85encode(char.encode()).decode()


def decode(char):
    return b85decode(char.encode()).decode()
