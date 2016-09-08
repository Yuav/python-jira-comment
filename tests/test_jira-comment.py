import os
from os.path import dirname
import unittest
import subprocess

root = dirname(dirname(os.path.realpath(__file__)))
jira_comment = "%s/bin/jira-comment" % root


class TestCLIParser(unittest.TestCase):
    def test_does_compile(self):
        output = subprocess.check_output("coverage run %s -h" % jira_comment, shell=True)
