import sys, pathlib
import pandas as pd
import fitbit
import pytest

# Get the dynamic path to the file so we can edit the tests in interactive mode
# Need to put hfkpy on the python path to get this to work without pathlib
ROOT_DIR = str(pathlib.Path(__file__).parents[2])
sys.path.insert(0, ROOT_DIR)

from hfkpy.fitbit.get_data import client


def load_tokens(root_directory):
    return pd.read_csv(pathlib.Path(root_directory) / "tokens.csv")


# Test that we can instantiate a Fitbit client object
# https://stackoverflow.com/questions/58645563/how-does-pytest-mark-filterwarnings-work
# https://docs.pytest.org/en/stable/how-to/capture-warnings.html#pytest-mark-filterwarnings
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_client():
    try:
        auth2_client = client(load_tokens(ROOT_DIR))
        assert isinstance(auth2_client, fitbit.api.Fitbit)
    except:
        assert False, "Client did not instantiate successfully"

