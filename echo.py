#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "???"


import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description = "Cause argparse help to run")
    return parser.parse_args()


def main(args):
    """Implementation of echo"""
    args = create_parser()
    print(args)

    pass


if __name__ == '__main__':
    pass
