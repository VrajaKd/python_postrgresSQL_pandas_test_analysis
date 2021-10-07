from pathlib import Path


def user_values():
    error_message = 'Please enter a numeric value!'

    values = {}
    # Get values from user
    while True:
        try:
            values['circle_center_x'] = float(input("Enter the x coordinate of the center of the circle: "))
            break
        except:
            print(error_message)

    while True:
        try:
            values['circle_center_y'] = float(input("Enter the y coordinate of the center of the circle: "))
            break
        except:
            print(error_message)

    while True:
        try:
            circle_radius = float(input("Enter the radius of the circle (m): "))
            if circle_radius < 0:
                print('Please enter a positive value!')
            else:
                values['circle_radius'] = circle_radius
                break
        except:
            print(error_message)

    while True:
        txt_file_name = Path(input("Enter a file name: "))
        if txt_file_name.is_file():
            values['txt_file_name'] = txt_file_name
            break
        else:
            print('No such file.')

    return values
