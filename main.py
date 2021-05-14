from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_number = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_number + password_letters + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    input3.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_data():
    file_value = []
    value1 = input1.get()
    value2 = input2.get()
    value3 = input3.get()
    file_value.append(value1)
    file_value.append(value2)
    file_value.append(value3)
    if len(value1) == 0 or len(value3) == 0:

        error = messagebox.showinfo(title="Oops", message="All the fields are not Entered")
    else:
        is_ok = messagebox.askokcancel(title=value1, message=f"These are the Details Entered: \nEmail :{value2} "
                                                             f"\nPassword:{value3}")
        if is_ok:
            f = open("password.txt", "a")
            f.write("\n")
            for i in file_value:
                f.write(f"{i} |")
            f.close()
            input1.delete(0, END)
            input3.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
WHITE = "#FFFFFF"
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=image)
canvas.grid(row=0, column=1)

label1 = Label(text="Website:", bg=WHITE)
label1.grid(row=1, column=0)
label2 = Label(text="Email/Username:", bg=WHITE)
label2.grid(row=2, column=0)
label3 = Label(text="Password:", bg=WHITE)
label3.grid(row=3, column=0)

input1 = Entry(width=35)
input1.grid(row=1, column=1, columnspan=2)
input1.focus()
input2 = Entry(width=35)
input2.grid(row=2, column=1, columnspan=2)
input2.insert(0, "prasadhegde@gmail.com")
input3 = Entry(width=21)
input3.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=get_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
