from square_matlin.nums_squared import numbers_added_and_squared
from errors import ERROR_wrong_input_type


def cmd_interface_for_squared():
    x_value = input("Enter a numeric value to represent X: ")
    y_value = input("Enter a numeric value to represent Y: ")
    try:
        print("The result of the calculation is: ", numbers_added_and_squared(int(x_value), int(y_value)))
    except TypeError:
        print(ERROR_wrong_input_type)


if __name__ == '__main__':
    cmd_interface_for_squared()
