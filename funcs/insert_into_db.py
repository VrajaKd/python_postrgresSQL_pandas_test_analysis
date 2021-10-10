from sqlalchemy import create_engine
from sqlalchemy.types import Integer, Float, String
import io
import os
from dotenv import load_dotenv


def insert_into_db(df, table_name):
    table_name = (table_name.replace('.txt', '')).lower()
    load_dotenv()

    engine = create_engine('postgresql+psycopg2://' +
                           os.environ.get('POSTGRES_USER') + ':' +
                           os.environ.get('POSTGRES_PASSW') + '@' +
                           os.environ.get('POSTGRES_HOST') + ':' +
                           os.environ.get('POSTGRES_PORT') + '/' +
                           os.environ.get('POSTGRES_DB'))

    # Reset df index from 0
    df = df.reset_index(drop=True)

    try:
        # Insert db head and metadata
        dtype = {'sequence': Integer(), 'tag_id': String, 'tag_timestamp': Integer, 'move':String, 'x_coord': Float, 'y_coord': Float, 'z_coord': Float, 'time': Float}
        for column_name in list(df):
            if column_name.find('anchor') != -1:
                dtype[column_name] = String
            if column_name.find('dist_') != -1:
                dtype[column_name] = Integer
            if column_name.find('_move') != -1:
                dtype[column_name] = String

        # Drop old table and create new empty table
        df.head(0).to_sql(table_name, engine, if_exists='replace', index=True, index_label='id', dtype=dtype)

        conn = engine.raw_connection()
        cur = conn.cursor()

        # Insert into the db
        output = io.StringIO()
        df.to_csv(output, sep='\t', header=False, index=True)
        output.seek(0)
        cur.copy_from(output, table_name, null="")  # Null values become ''
        conn.commit()

        print(f'Data entered into the database table "{table_name}"...')
        return 'ok'
    except Exception as e:
        print(f'Insert into database error - {e}')
