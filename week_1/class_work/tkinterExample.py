import tkinter
from ex_package_matlin import example

print(example.add_one(1))

def clicked():
    txtval2 = int(txt.get()) * 2
    txt2.insert(0, txtval2)
    print(selected.get())


window = tkinter.Tk()

window.title("Welcome ICS0019")
window.geometry('350x500')

tkinter.Label(window, text='Input').grid(row=0)
tkinter.Label(window, text='Output').grid(row=1)

txt = tkinter.Entry(window, width=15)
txt.grid(column=1, row=0)
txt.focus()

txt2 = tkinter.Entry(window, width=15)
txt2.grid(column=1, row=1)

selected = tkinter.IntVar()
rad1 = tkinter.Radiobutton(window,text='First', value=1, variable=selected)
rad2 = tkinter.Radiobutton(window,text='Second', value=2, variable=selected)
rad1.grid(column=0, row=3)
rad2.grid(column=1, row=3)

btn = tkinter.Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=4)

window.mainloop()
