import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv


def get_data_from_db(table_name):
    table_name = (table_name.replace('.txt', '')).lower()
    load_dotenv()

    engine = create_engine('postgresql+psycopg2://' +
                           os.environ.get('POSTGRES_USER') + ':' +
                           os.environ.get('POSTGRES_PASSW') + '@' +
                           os.environ.get('POSTGRES_HOST') + ':' +
                           os.environ.get('POSTGRES_PORT') + '/' +
                           os.environ.get('POSTGRES_DB'))

    try:
        df = pd.read_sql_query('select * from ' + table_name, con=engine)
        print('Data retrieved from the database...')
        return df
    except Exception as e:
        print(f'Get date from database error - {e}')
