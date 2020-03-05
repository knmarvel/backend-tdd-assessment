#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "knmarvel"


import argparse


def create_parser(*args):
    """Defines and provides help for commandline arguments"""
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
    return parser


def main():
    """Implementation of echo"""

    args = create_parser().parse_args()
    text = args.text

    if args.upper:
        text = text.upper()

    if args.lower:
        text = text.lower()

    if args.title:
        text = text.title()

    print(text)


if __name__ == '__main__':
    main()
