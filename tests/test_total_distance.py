from funcs.get_data_from_db import get_data_from_db
from funcs.total_distance import total_distance


def test_total_distance():
    result = total_distance(get_data_from_db('example_data'), 6)

    assert result[0]
    assert result[1]
