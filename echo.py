#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "knmarvel"


import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument("text",
                        type=str,
                        help="text to be manipulated")
    parser.add_argument('-u',
                        '--upper',
                        action='store_const',
                        const=bool,
                        help="convert text to uppercase")
    parser.add_argument("-l",
                        "--lower",
                        action='store_const',
                        const=bool,
                        help="convert text to lowercase")
    parser.add_argument("-t",
                        "--title",
                        action='store_const',
                        const=bool,
                        help="convert text to titlecase")
    return parser.parse_args()


def main():
    """Implementation of echo"""

    args = create_parser()

    if args.upper:
        if sys.argv[1] == "-u" or sys.argv[1] == "--upper":
            print(args.text.upper())

    if args.lower:
        if sys.argv[1] == "-l" or sys.argv[1] == "--lower":
            print(args.text.lower())

    if args.title:
        if sys.argv[1] == "-t" or sys.argv[1] == "--title":
            print(args.text.title())

    else:
        print(args.text)


if __name__ == '__main__':
    main()
