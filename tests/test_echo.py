#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess


# Your test case class goes here
class TestEcho(unittest.TestCase):
    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect its output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode("utf-8")
        usage = open("./USAGE", "r").read()
        self.assertEquals(stdout, usage)

    def test_upper(self):
        """Running the program with -u or --upper as arguments should result with
        "upper" stored in namespace returned from parser.parse_args and that
        "hello" will return to "HELLO" when the program is run"""

        # Run the command `python ./echo.py -u hello` in a separate process,
        # then collect its output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-u", "hello"],
            stdout=subprocess.PIPE)
        args_u = process.args
        stdout, _ = process.communicate()
        stdout_u = stdout.decode("utf-8")

        process = subprocess.Popen(
            ["python", "./echo.py", "--upper", "hello"],
            stdout=subprocess.PIPE)
        args_upper = process.args
        stdout, _ = process.communicate()
        stdout_upper = stdout.decode("utf-8")

        usage = open("./USAGEUPPER", "r").read()
        self.assertEquals(stdout_u, usage)
        self.assertEqual("-u" in args_u, True)
        self.assertEquals(stdout_upper, usage)
        self.assertEqual("--upper" in args_upper, True)

    def test_lower(self):
        """Running the program with -l or --lower as arguments should result with
        "lower" stored in namespace returned from parser.parse_args and that
        "Hello" will return to "hello" when the program is run"""

        process = subprocess.Popen(
            ["python", "./echo.py", "-l", "Hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        args_l = process.args
        stdout_l = stdout.decode("utf-8")

        process = subprocess.Popen(
            ["python", "./echo.py", "--lower", "Hello"],
            stdout=subprocess.PIPE)
        args_lower = process.args
        stdout, _ = process.communicate()
        stdout_lower = stdout.decode("utf-8")

        usage = open("./USAGELOWER", "r").read()
        self.assertEquals(stdout_l, usage)
        self.assertEqual("-l" in args_l, True)
        self.assertEquals(stdout_lower, usage)
        self.assertEqual("--lower" in args_lower, True)

    def test_title(self):
        """Running the program with -t or --title as arguments should result with
        "title" stored in namespace returned from parser.parse_args and that
        "hello" will return to "Hello" when the program is run"""

        process = subprocess.Popen(
            ["python", "./echo.py", "-t", "hello"],
            stdout=subprocess.PIPE)
        args_t = process.args
        stdout, _ = process.communicate()
        stdout_t = stdout.decode("utf-8")

        process = subprocess.Popen(
            ["python", "./echo.py", "--title", "hello"],
            stdout=subprocess.PIPE)
        args_title = process.args
        stdout, _ = process.communicate()
        stdout_title = stdout.decode("utf-8")

        usage = open("./USAGETITLE", "r").read()
        self.assertEquals(stdout_t, usage)
        self.assertEqual("-t" in args_t, True)
        self.assertEquals(stdout_title, usage)
        self.assertEquals("--title" in args_title, True)

    def test_all(self):
        """Running the program with all three arguments should result with
        the first argument stored in namespace returned from
        parser.parse_args and that the first argument's case will be applied
        to the returned string"""

        process = subprocess.Popen(
            ["python", "./echo.py", "-t", "-u", "-l", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout_t = stdout.decode("utf-8")
        usage_t = open("./USAGETITLE", "r").read()
        self.assertEquals(stdout_t, usage_t)

        process = subprocess.Popen(
            ["python", "./echo.py", "-u", "-t", "-l", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout_t = stdout.decode("utf-8")
        usage_t = open("./USAGETITLE", "r").read()
        self.assertEquals(stdout_t, usage_t)

        process = subprocess.Popen(
            ["python", "./echo.py", "-l", "-u", "-t", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout_t = stdout.decode("utf-8")
        usage_t = open("./USAGETITLE", "r").read()
        self.assertEquals(stdout_t, usage_t)

    def test_none(self):
        """Running the program with no arguments should result with
        the string being returned as-is"""
        process = subprocess.Popen(
            ["python", "./echo.py", "hElLo"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode("utf-8")
        usage = open("./USAGENONE", "r").read()
        self.assertEquals(stdout, usage)


if __name__ == '__main__':
    unittest.main()
