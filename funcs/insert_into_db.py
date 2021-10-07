from sqlalchemy import create_engine
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

    # Drop old table and create new empty table
    try:
        df.head(0).to_sql(table_name, engine, if_exists='replace', index=False)

        conn = engine.raw_connection()
        cur = conn.cursor()
        output = io.StringIO()
        df.to_csv(output, sep='\t', header=False, index=False)
        output.seek(0)
        cur.copy_from(output, table_name, null="")  # Null values become ''
        conn.commit()
        print(f'Data entered into the database table "{table_name}"...')
        return 'ok'
    except Exception as e:
        print(f'Insert into database error - {e}')
