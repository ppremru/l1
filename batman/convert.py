""" MVP """

import sys
import argparse
import csv


from .batman import Batman
from .miro import Miro
from .tackle import Tackle


def convert(bat_file, tackle_file):
    """start here"""
    bat = None
    try:
        bat = Batman(bat_file, tackle_file)
    except ValueError as ex:
        print("cause:", ex.__cause__)
        print("exception:", ex)
        SystemExit(9)

    if bat:
        bat.convert()


# ENTRY POINT
def main() -> int:
    parser = argparse.ArgumentParser(
        description="MVP to parse csv from BAT to csv for Tackle"
    )
    parser.add_argument(
        "--i",
        default=Miro.FILENAME,
        type=str,
        help="Optional name of the input BAT csv file",
    )
    parser.add_argument(
        "--o",
        default=Tackle.FILENAME,
        type=str,
        help="Optional name of the output Tackle csv file",
    )
    args = parser.parse_args()
    convert(args.i, args.o)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
