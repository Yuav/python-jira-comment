#!/usr/bin/env python
from setuptools import setup


setup(name='jira-comment',
      version='0.1.0',
      description='Command line tool to post comment to Jira',
      author='Jon Skarpeteig',
      author_email='jskarpet@cisco.com',
      url='https://gitscm.cisco.com/projects/CTG/repos/python-jira-comment/browse',
      packages=['app'],
      install_requires=[
          'docopt',
          'jira',
          'PyCrypto',
      ],
      tests_require=[
          'nose',
      ],
      setup_requires=[
          'package_version'
      ],
      scripts=['bin/jira-comment'],
      )
