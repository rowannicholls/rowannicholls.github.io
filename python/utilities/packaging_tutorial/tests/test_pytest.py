"""
Unit tests with pytest and nose2.

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
import numpy as np
import sys
import os

sys.path.insert(1, os.path.join(os.path.dirname(__file__), '..', 'src'))

from example_package_rowannicholls import module


def test_case():
    """Test case."""
    v_0 = 27  # m/s
    r_y0 = 1.8  # m
    theta = 58 * np.pi / 180  # radians
    actual = module.spud_gun_firing_distance(v_0, r_y0, theta)
    expected = 67.89755324030912
    assert expected == actual, f'Expected "{expected}", got "{actual}"'
