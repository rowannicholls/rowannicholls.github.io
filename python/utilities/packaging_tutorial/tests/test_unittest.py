"""
Unit tests with unittest, pytest and nose2.

Using unittest
--------------
There is no need for installation; unittest is in the the standard library.

Use by running this script directly or use from the terminal with:
$ python3.11 -m unittest test_unittest
or, for a more verbose output:
$ python3.11 -m unittest -v test_unittest

Discover and test all modules with names of the form "test*.py" with:
$ python3.11 -m unittest discover

Using pytest
------------
Install with:
$ python3.11 -m pip install pytest

Use with:
$ pytest

Using nose2
-----------
Install with:
$ python3.11 -m pip install nose2

Use with:
$ python3.11 -m nose2
"""
import unittest
import numpy as np
import sys
import os

sys.path.insert(1, os.path.join(os.path.dirname(__file__), '..', 'src'))

from example_package_rowannicholls import module


class TestCases(unittest.TestCase):
    """Test cases."""

    def test_case(self):
        """Test case."""
        v_0 = 27  # m/s
        r_y0 = 1.8  # m
        theta = 58 * np.pi / 180  # radians
        actual = module.spud_gun_firing_distance(v_0, r_y0, theta)
        expected = 67.89755324030912
        error_message = f'Expected "{expected}", got "{actual}"'
        self.assertEqual(expected, actual, error_message)


if __name__ == '__main__':
    unittest.main()
