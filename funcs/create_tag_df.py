import pandas as pd


# Find unique tags and create dataframes for them
def create_tag_df(df):
    # Change coordinate columns type to numeric
    df[["x_coord", "y_coord"]] = df[["x_coord", "y_coord"]].apply(pd.to_numeric)

    # Get unique tags
    unique_tags = df.tag_id.unique()

    # Create your own dataframe for each device
    unique_tags_dict = {}
    for device_id in unique_tags:
        unique_tags_dict[device_id] = df.loc[(df['tag_id'] == device_id)].copy()

    return unique_tags_dict
