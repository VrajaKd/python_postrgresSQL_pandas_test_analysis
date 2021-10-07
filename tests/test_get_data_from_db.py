from funcs.get_data_from_db import get_data_from_db
import pandas as pd


def test_get_data_from_db():
    assert isinstance(get_data_from_db('example_data'), pd.DataFrame)