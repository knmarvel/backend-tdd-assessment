#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import subprocess
import echo


# Your test case class goes here
class TestEcho(unittest.TestCase):
    def setUp(self):
        self.parser = echo.create_parser()

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
        args_u = ["hello", "-u"]
        namespace_u = self.parser.parse_args(args_u)

        args_upper = ["hello", "--upper"]
        namespace_upper = self.parser.parse_args(args_upper)

        process = subprocess.Popen(
            ["python", "./echo.py", "-u", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout_u = stdout.decode("utf-8")

        process = subprocess.Popen(
            ["python", "./echo.py", "--upper", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout_upper = stdout.decode("utf-8")

        usage = open("./USAGEUPPER", "r").read()

        self.assertTrue(namespace_u.upper)
        self.assertTrue(namespace_upper.upper)
        self.assertEquals(stdout_u, usage)
        self.assertEquals(stdout_upper, usage)

    def test_lower(self):
        """Running the program with -l or --lower as arguments should result with
        "lower" stored in namespace returned from parser.parse_args and that
        "Hello" will return to "hello" when the program is run"""

        args_l = ["hello", "-l"]
        namespace_l = self.parser.parse_args(args_l)

        args_lower = ["hello", "--lower"]
        namespace_lower = self.parser.parse_args(args_lower)

        process = subprocess.Popen(
            ["python", "./echo.py", "-l", "Hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout_l = stdout.decode("utf-8")

        process = subprocess.Popen(
            ["python", "./echo.py", "--lower", "Hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout_lower = stdout.decode("utf-8")

        usage = open("./USAGELOWER", "r").read()

        self.assertTrue(namespace_l.lower)
        self.assertTrue(namespace_lower.lower)
        self.assertEquals(stdout_l, usage)
        self.assertEquals(stdout_lower, usage)

    def test_title(self):
        """Running the program with -t or --title as arguments should result with
        "title" stored in namespace returned from parser.parse_args and that
        "hello" will return to "Hello" when the program is run"""
        args_t = ["hello", "-t"]
        namespace_t = self.parser.parse_args(args_t)

        args_title = ["hello", "--title"]
        namespace_title = self.parser.parse_args(args_title)

        process = subprocess.Popen(
            ["python", "./echo.py", "-t", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout_t = stdout.decode("utf-8")

        process = subprocess.Popen(
            ["python", "./echo.py", "--title", "hello"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout_title = stdout.decode("utf-8")

        usage = open("./USAGETITLE", "r").read()

        self.assertTrue(namespace_t.title)
        self.assertTrue(namespace_title.title)
        self.assertEquals(stdout_t, usage)
        self.assertEquals(stdout_title, usage)

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
