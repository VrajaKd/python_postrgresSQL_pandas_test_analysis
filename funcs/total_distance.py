import numpy as np
from funcs.create_tag_df import create_tag_df


def total_distance(df, no_of_anchors):
    print('Data analysis...')
    # Get separate dataframe for each device
    unique_tags_dict = create_tag_df(df)

    print('----------------------')
    print(f'No of anchords: {no_of_anchors}')
    print(f'No of devices: {len(unique_tags_dict)}')
    print()

    device_id = ''
    tot_distance = ''

    # Calculate total distance for each device
    for device_id, tag_df in unique_tags_dict.items():
        tag_df.loc[(tag_df['tag_id'] == device_id), 'distance'] = \
            np.sqrt(((tag_df['x_coord'] - tag_df['x_coord'].shift(-1)) ** 2) +
                    ((tag_df['y_coord'] - tag_df['y_coord'].shift(-1)) ** 2))
        tot_distance = round(tag_df['distance'].sum(), 2)

        print(f'The total distance of device {device_id} is {tot_distance} m')
    return device_id, tot_distance
