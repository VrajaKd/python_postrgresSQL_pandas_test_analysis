from funcs.insert_into_db import insert_into_db
from funcs.clean_data import clean_data


def test_insert_into_db():
    result = clean_data('example_data.txt')
    db_resp = insert_into_db(result['df_final'], 'example_data.txt')

    assert db_resp == 'ok'
