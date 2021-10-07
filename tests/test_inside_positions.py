from funcs.get_data_from_db import get_data_from_db
from funcs.inside_positions import inside_positions


def test_inside_positions():
    result = inside_positions(30, 50, 5, get_data_from_db('example_data'))
    assert result[0]
    assert result[1]
