"""
Run the test suite with `python setup.py test`
"""

import unittest

import my_project.module


class TestMyLib(unittest.TestCase):
    def test_add_two(self):
        self.assertEqual(my_project.module.add_two(2), 4)
