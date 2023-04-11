import tkinter
from decimal import *


ERROR_wrong_input_type = "Inputs must be Integers."


def numbers_added_and_squared(x, y):
    if isinstance(x, int) or isinstance(y, int):
        return (x + y) * (x + y)
    else:
        raise TypeError


def square_matlin_cmd():
    x_value = input("Enter a numeric value to represent X: ")
    y_value = input("Enter a numeric value to represent Y: ")
    try:
        print("The result of the calculation is: ", numbers_added_and_squared(int(x_value), int(y_value)))
    except TypeError:
        print(ERROR_wrong_input_type)


def square_matlin_gui():
    def clicked():
        try:
            math = numbers_added_and_squared(int(x_value.get()), int(y_value.get()))
            result.config(text=str(math))
            res_label.config(text='The result is:', fg='green')
            listbox.insert("0", "(" + x_value.get() + " + " + y_value.get() + ")²" + " = " + str(math))
        except (ValueError, TypeError):
            res_label.config(text=ERROR_wrong_input_type, fg='red')

    window = tkinter.Tk()

    window.title("Welcome ICS0019")
    window.geometry('500x300')

    window.option_add("*font", "arial 12")

    listbox_border = tkinter.Frame(window, bd=1, relief="sunken", background="white")
    listbox_border.grid(column=2, pady=15, padx=15, rowspan=10)

    listbox = tkinter.Listbox(listbox_border, highlightthickness=0, borderwidth=0,
                              background=listbox_border.cget("background"))
    listbox.grid(column=2, rowspan=10, padx=10, pady=10)

    heading = tkinter.Label(window, text='(X + Y)²', font='arial 18')
    heading.grid(row=0, column=1, pady=10)

    X_label = tkinter.Label(window, text='X Value')
    X_label.grid(row=1, padx=10, pady=2)

    Y_label = tkinter.Label(window, text='Y Value')
    Y_label.grid(row=2, padx=10, pady=2)

    x_value = tkinter.Entry(window, width=15)
    x_value.grid(column=1, row=1)
    x_value.focus()

    y_value = tkinter.Entry(window, width=15)
    y_value.grid(column=1, row=2)

    btn = tkinter.Button(window, text="Calculate", command=clicked)
    btn.grid(column=1, row=3, pady=5)

    res_label = tkinter.Label(window, text='', font='arial 12')
    res_label.grid(row=5, column=1, pady=8)

    result = tkinter.Label(window, text='RESULT', font='arial 25')
    result.grid(row=6, column=1)

    window.mainloop()