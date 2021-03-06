"""
Math functions.
"""
from __future__ import absolute_import, division

try:
    # New Py>=3.5 import
    from math import gcd as pygcd
except ImportError:
    # Deprecated import from Py3.5 onwards.
    from fractions import gcd as pygcd

__author__ = 'Shyue Ping Ong'
__copyright__ = 'Copyright 2013, The Materials Virtual Lab'
__version__ = '0.1'
__maintainer__ = 'Shyue Ping Ong'
__email__ = 'ongsp@ucsd.edu'
__date__ = '8/6/14'


def gcd(*numbers):
    """
    Returns the greatest common divisor for a sequence of numbers.

    Args:
        \*numbers: Sequence of numbers.

    Returns:
        (int) Greatest common divisor of numbers.
    """
    n = numbers[0]
    for i in numbers:
        n = pygcd(n, i)
    return n


def lcm(*numbers):
    """
    Return lowest common multiple of a sequence of numbers.

    Args:
        \*numbers: Sequence of numbers.

    Returns:
        (int) Lowest common multiple of numbers.
    """
    n = 1
    for i in numbers:
        n = (i * n) // gcd(i, n)
    return n
