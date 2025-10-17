from base64 import b64decode, b64encode


def compress(char):
    return b64encode(char.encode()).decode()


def decompress(char):
    return b64decode(char.encode()).decode()
