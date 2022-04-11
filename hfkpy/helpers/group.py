import pandas as pd
import re


def flatten_column_index(data):
    """Flatten a MultiIndex dataframe columns. Approach taken from `stack overflow <https://stackoverflow.com/questions/14507794/pandas-how-to-flatten-a-hierarchical-index-in-columns>`_.

    Args:
        data (dataframe): Dataframe with MultiIndex to flatten.

    Returns:
        dataframe: The user supplied dataframe with the MultiIndex flattened.

    >>> flatten_column_index(df)
    """
    data = data.copy()
    new_names = ["_".join(col) for col in data.columns.values]
    new_names = [re.sub(r"_$", "", n) for n in new_names]
    data.columns = new_names

    return data
