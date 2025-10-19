import argparse

from tciph import __version__
from tciph.core import cipher, cipher_file, decipher, decipher_file, gen_key


def main():
    parser = argparse.ArgumentParser(prog="tciph")

    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=__version__,
    )
    parser.add_argument(
        "-k",
        "--key",
        action="store_true",
        help="generate a key",
    )
    parser.add_argument(
        "-c",
        "--cipher",
        action="store_true",
        help="cipher plaintext",
    )
    parser.add_argument(
        "-d",
        "--decipher",
        action="store_true",
        help="decipher plaintext",
    )
    parser.add_argument(
        "--cipher-file",
        action="store_true",
        help="cipher plaintext from a file",
    )
    parser.add_argument(
        "--decipher-file",
        action="store_true",
        help="decipher plaintext from a file",
    )

    args = parser.parse_args()

    if args.key:
        gen_key()

    elif args.cipher:
        cipher()

    elif args.decipher:
        decipher()

    elif args.cipher_file:
        cipher_file()

    elif args.decipher_file:
        decipher_file()

    else:
        parser.print_help()
