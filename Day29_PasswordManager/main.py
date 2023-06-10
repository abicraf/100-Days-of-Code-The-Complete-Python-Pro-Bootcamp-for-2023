from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    # clear the password in the entry box.
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    #password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    letter_list = [random.choice(letters) for _ in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)
    # print(password_list)

    # Use .join() to rephrase the code below
    #
    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)

    # Use pyperclip to auto copy the password to clipboard
    pyperclip.copy(password)

    # insert the new generated password in to the entry box.
    password_entry.insert(0, password)
    # print(f"Your password is: {password}")

# ---------------------------- Search PASSWORD ------------------------------- #
def find_password():
    web_content = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            #print(data.keys())  # print out the keys in data dictionary
            #print(data["jfowejif"])  # print out hte jfowejif key's value.
    except FileNotFoundError:
        messagebox.showinfo(title="No File", message="No Data File Found.")
    else:
        if web_content in data:
            messagebox.showinfo(title=f'Search Result of {web_content}',
                                message=f"Email: {data[web_content]['email']}\n"
                                        f"Password: {data[web_content]['password']}")
        else:
            messagebox.showinfo(title=f'Search Result of {web_content}',
                                message=f"No details for the {web_content} exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # get the content in entries
    web_content = web_entry.get()
    email_content = email_entry.get()
    password_content = password_entry.get()

    # Day 30 practice, use JSON to search email and password
    # create a dictionary type to manage data
    new_data = {
        web_content: {
            "email": email_content,
            "password": password_content,
        }
    }


    # check if the content is correct before saving information to the file
    if web_content == '' or password_content =='' or email_content =='':
        messagebox.showinfo(title='Oops', message="Don't leave any field empty!")
    else:
        # is_ok = messagebox.askokcancel(title="Please confirm",
        #                                message=f"Website:{web_content}\nEmail/User:{email_content}\n"
        #                                        f"Password:{password_content}\n\n Is these correct?")
        # if is_ok:
        #     # open a file and write the content
        #     with open("password.txt", "a") as file:
        #         # save the content in entries.
        #         file.write(f"{web_content}  |  {email_content}  |  {password_content}\n")
        #
        # Day 30 practice, Use JSON to rephrace code above.
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # clear the content
            web_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Label
web_label = Label(text='Website:')
web_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entry
web_entry = Entry(width=21)
web_entry.grid(row=1, column=1)
web_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "kay@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Button
GenPassword_button = Button(text="Generate Password", width=15, command=password_generator)
GenPassword_button.grid(row=3, column=2)

Add_button = Button(text="Add", width=38, command=save)
Add_button.grid(row=4, column=1, columnspan=2)

Search_button = Button(text="Search", width=15, command= find_password)
Search_button.grid(row=1, column=2)

window.mainloop()
