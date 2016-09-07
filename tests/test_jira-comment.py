import os
from os.path import dirname
import unittest


class TestCLIParser(unittest.TestCase):
    def test_does_compile(self):
        root = dirname(dirname(os.path.realpath(__file__)))
        exitcode = os.system("%s/bin/jira-comment -h" % root)
        self.assertEqual(0, exitcode)

