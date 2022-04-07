import sys, pathlib

# get the dynamic path to the file so we can edit the tests in interactive mode
sys.path.append(str(pathlib.Path(__file__).parents[2]))

from hfkpy.helpers.mathematics import *


def test_add():
    assert add(1, 2, 3) == 6


def test_multiply():
    assert multiply(3, 2) == 6

