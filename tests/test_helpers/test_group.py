import sys, pathlib
import pandas as pd

# Get the dynamic path to the file so we can edit the tests in interactive mode
# Need to put hfkpy on the python path to get this to work without pathlib
ROOT_DIR = str(pathlib.Path(__file__).parents[2])
sys.path.insert(0, ROOT_DIR)

from hfkpy.helpers.group import flatten_column_index


# Test data
df = pd.DataFrame({"A": ["a", "b"] * 6, "B": [1, 2, 3] * 4, "C": [3, 4, 1] * 4})

grouped_df = (
    df.groupby("A")
    .agg({"B": [("name_1", "sum"), ("name_2", "min")], "C": [("name_1", "mean")]})
    .reset_index()
)

simple_df = pd.DataFrame({"A": [1, 2, 3]})

# This should successfully flatten the MultiIndex
def test_flatten_column_index_multiindex():
    assert list(flatten_column_index(grouped_df).columns) == [
        "A",
        "B_name_1",
        "B_name_2",
        "C_name_1",
    ]


# This should do nothing to the dataframe
def test_flatten_column_index_no_multiindex():
    assert list(flatten_column_index(simple_df).columns) == ["A"]
