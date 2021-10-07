from funcs.clean_data import clean_data
import pandas as pd
import os

def test_clean_data():
    os.chdir('..')
    result = clean_data('example_data.txt')

    assert type(result) is dict
    assert len(result) is 3
    assert isinstance(result['df_final'], pd.DataFrame)
    assert result['start_time']
    assert result['no_of_anchors'] > 0
