from funcs.create_tag_df import create_tag_df

# Function to check if a position lies inside a circle
# The idea is to calculate the distance of the position from the center
# If the distance from the center is less than or equal to the radius,
# then the position is in a circle. Otherwise, the position is out of the circle.

def inside_positions(circle_center_x, circle_center_y, circle_radius, df):
    print()
    # Get separate dataframe for each device
    unique_tags_dict = create_tag_df(df)

    device_id = ''
    inside = ''

    # Compare radius of circle with distance of its center from given point
    for device_id, tag_df in unique_tags_dict.items():
        tag_df.loc[(tag_df['tag_id'] == device_id), 'position'] = \
            ((tag_df['x_coord'] - circle_center_x) ** 2) + \
            ((tag_df['y_coord'] - circle_center_y) ** 2) <= \
            circle_radius ** 2

        inside = 0
        outside = 0
        try:
            inside = tag_df['position'].value_counts()[True]
        except:
            pass
        try:
            outside = tag_df['position'].value_counts()[False]
        except:
            pass

        print(
            f'Device {device_id} is located inside the circle {inside} times and outside the circle {outside} times')
    return device_id, inside
