import pandas as pd
import time


def clean_data(txt_file_name):
    print()
    # Create pandas dataframe from txt file
    try:
        df = pd.read_fwf(txt_file_name, sep='\t', names=['tmp_column', 'coord'])
    except Exception as e:
        return str(e)
    start_time = time.time()

    # Create new column from next row
    df['coord'] = df['tmp_column'].shift(-1)

    # Remove unnecessary rows
    df = df.loc[(df['tmp_column'].str.find('RR_L') != -1)]

    # Copy RR_L data into new df
    df_rr = pd.DataFrame(columns=['tmp_column'])
    df_rr['tmp_column'] = df['tmp_column']

    # Copy COORD data into new df
    df_coord = pd.DataFrame(columns=['coord'])
    df_coord['coord'] = df['coord']

    # Split df_rr df rows into columns
    df_rr = df_rr['tmp_column'].str.split(',', expand=True)

    # Find the number of anchors
    no_of_anchors = int((len(df_rr.columns) - 6) / 3)
    df_rr.fillna("", inplace=True)

    # Correct the values in last columns
    for index in range(1, 4):
        df_rr.loc[(df_rr[len(df_rr.columns) - index] != '0x00') &
                  (df_rr[len(df_rr.columns) - index] != '0x01'), len(df_rr.columns) - index] = '0x00'

    # Split df_coord df rows into columns
    df_coord = df_coord['coord'].str.split(',', expand=True)

    # Combine two dataframes
    df_final = pd.merge(df_rr, df_coord, left_index=True, right_index=True, how='outer')

    # Remove the rows with the error message
    df_final = df_final.loc[(df_final['7_y'].str.len() == 0)]

    # Remove unnecessary columns
    df_final = df_final.drop(columns=['0_x', '1_x', '0_y', '1_y', '2_y', '3_y', '7_y'])

    # Rename columns
    mapping = {df_final.columns[0]: 'sequence',
               df_final.columns[1]: 'tag_id',
               df_final.columns[no_of_anchors * 2 + 2]: 'tag_timestamp',
               df_final.columns[-5]: 'move',
               df_final.columns[-4]: 'x_coord',
               df_final.columns[-3]: 'y_coord',
               df_final.columns[-2]: 'z_coord',
               df_final.columns[-1]: 'time',
               }
    df_final = df_final.rename(columns=mapping)

    mapping = {}
    add = 0
    for no in range(1, no_of_anchors + 1):
        mapping[df_final.columns[no + 1 + add]] = 'anchor_' + str(no)
        mapping[df_final.columns[no + 2 + add]] = 'dist_' + str(no)
        mapping[df_final.columns[no_of_anchors * 2 + no + 2]] = 'tag_' + str(no) + '_move'
        add += 1
    df_final = df_final.rename(columns=mapping)
    print('Data cleaned...')

    return {'df_final': df_final, 'start_time': start_time, 'no_of_anchors': no_of_anchors}
