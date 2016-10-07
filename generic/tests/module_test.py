"""
Run the test suite with `python setup.py test`

Don't add an __init__.py to this directory to make it a module. Find another way to do what you want. If it's a module
it could get installed and put `tests` into the global namespace.
"""

import unittest

import my_project.module


class TestMyLib(unittest.TestCase):
    def test_add_two(self):
        self.assertEqual(my_project.module.add_two(2), 4)
