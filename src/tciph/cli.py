import argparse

from tciph import __version__
from tciph.core import cipher, decipher, gen_key


def main():
    parser = argparse.ArgumentParser(
        prog="tciph",
        description="",
    )

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

    args = parser.parse_args()

    if args.key:
        gen_key()

    elif args.cipher:
        cipher()

    elif args.decipher:
        decipher()

    else:
        parser.print_help()
