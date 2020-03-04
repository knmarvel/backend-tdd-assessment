#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess


# Your test case class goes here
class TestEcho(unittest.TestCase):
    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper(self):
        """Running the program with -u or --upper as arguments should result with "upper" stored in namespace returned from
         parser.parse_args and that "hello" will return to "HELLO" when the program is run"""

    def test_lower(self):
        """Running the program with -l or --lower as arguments should result with
        "lower" stored in namespace returned from parser.parse_args and that
        "Hello" will return to "hello" when the program is run"""

    def test_title(self):
        """Running the program with -t or --title as arguments should result with
        "title" stored in namespace returned from parser.parse_args and that
        "hello" will return to "Hello" when the program is run"""
    
    def test_all(self):
        """Running the program with all three arguments should result with
        the first argument stored in namespace returned from
        parser.parse_args and that the first argument's case will be applied
        to the returned string"""
    
    def test_none(self):
        """Running the program with no arguments should result with
        the string being returned as-is"""

if __name__ == '__main__':
    unittest.main()
