import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=5, pady=5)

my_label = tkinter.Label(text="Miles")
my_label.config(text="Miles")
my_label.grid(column=2, row=0)
my_label.config(padx=5, pady=5)

new_label = tkinter.Label(text="is equal to")
new_label.grid(column=0, row=1)

another_label = tkinter.Label(text="Km")
another_label.grid(column=2, row=1)


def button_clicked():
    new_text = Input.get()
    final_label.config(text=int(new_text)*1.609)


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)


Input = tkinter.Entry(width=10)
print(Input.get())
Input.grid(column=1, row=0)

final_label = tkinter.Label(text=0)
final_label.grid(column=1, row=1)


window.mainloop()
