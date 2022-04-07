import sys, pathlib

# get the dynamic path to the file so we can edit the tests in interactive mode
# need to put hfkpy on the python path to get this to work without pathlib
sys.path.append(str(pathlib.Path(__file__).parents[2]))

from hfkpy.helpers.mathematics import *


def test_add():
    assert add(1, 2, 3) == 6


def test_multiply():
    assert multiply(3, 2) == 6
