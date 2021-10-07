import time

from funcs.clean_data import clean_data
from funcs.insert_into_db import insert_into_db
from funcs.get_data_from_db import get_data_from_db
from funcs.total_distance import total_distance
from funcs.inside_positions import inside_positions
from funcs.user_values import user_values


def record_handler():
    print('Positioning analysis')
    print('----------------------')

    # Collect user values
    values = user_values()

    # Load data from txt file and clean it
    cleaned_df = clean_data(values['txt_file_name'])

    # Insert cleaned data into database
    insert_into_db(cleaned_df['df_final'], str(values['txt_file_name']))

    # Get data from a database
    df = get_data_from_db(str(values['txt_file_name']))

    # Calculate total distance per tag
    total_distance(df, cleaned_df['no_of_anchors'])

    # Count the positions inside the circle
    inside_positions(values['circle_center_x'], values['circle_center_y'], values['circle_radius'], df)

    start_time = cleaned_df['start_time']
    print(f'--- All tasks completed in {round((time.time() - start_time), 2)} seconds ---')


record_handler()
