from tkinter import *

def on_button_click(value):
    current_text = entry_var.get()
    if value == "C":
        entry_var.set("")
    elif value == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
    else:
        entry_var.set(current_text + value)

window = Tk()
window.title("Calculator")
window.config(padx=20, pady=20, bg="black")

entry_var = StringVar()
entry = Entry(window, textvariable=entry_var, font=("Arial", 24), width=15, borderwidth=5, relief=RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

black_img = PhotoImage(file='images/circle.png')
white_img = PhotoImage(file='images/pngtree-blank-round-sticker-template-png-image_4684569.png')

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for text, row, col in buttons:
    btn_image = white_img if text.isdigit() else black_img
    btn = Button(window, text=text, font=("Arial", 18), image=btn_image, compound="center",
                 width=40, height=40, bg='black', fg='white', command=lambda t=text: on_button_click(t))
    btn.image = btn_image  # Keep a reference to avoid garbage collection
    btn.grid(row=row, column=col, padx=5, pady=5)

window.mainloop()