import json
from tkinter import *
from tkinter import messagebox # message box is a module not a class. so when we import *, it is not imported. so we should do it again separately.


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
import pyperclip
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)


    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)

    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_name=website_entry.get()
    email=email_username_entry.get()
    password=password_entry.get()
    new_data={
        website_name:{
            "email": email,
            "password":password
        }
    }
    if len(website_name)>0 and len(email)>0 and len(password)>0:
        # option=messagebox.askokcancel(title=website_name, message=f"email : {email},\n password : {password}.\n click okay to continue.")
        # print(option)
        # if option==True:
    # write
        #     with open("password.json", "w") as f:
        #         json.dump(new_data, f, indent=4)
        #         website_entry.delete(0, END)
        #         password_entry.delete(0, END)
    # read
        #         with open("password.json", "r") as f:
        #             data=json.load(f)
        #             print(data)
        #             print(type(data))  #dict
    #append
        try:
            with open("password.json","r") as f:
                data=json.load(f)
                data.update(new_data)
            with open("password.json","w") as f:
                json.dump(data,f,indent=4)
        except FileNotFoundError:
            with open("password.json", "w") as f:
                json.dump(new_data, f, indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showinfo(message="enter all the details.")
# ---------------------------- SEARCH ------------------------------- #

def search():
    website_name = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website_name: {
            "email": email,
            "password": password
        }
    }
    website_name=website_entry.get()
    try:
        with open("password.json", "r") as f:
            data = json.load(f)

            if website_name in data:
                password=data[website_name]["password"]
                email=data[website_name]["email"]
                messagebox.showinfo(message=f"email={email}, password={password}")
            else:
                response = messagebox.askokcancel(message="no website found. do you want to enter a new entry? ")
                if response:
                    save()
    except FileNotFoundError:
        messagebox.showinfo(message="no file found")




# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("password manager")
window.config(padx=20, pady=20)

lock_img=PhotoImage(file="logo.png")
canvas=Canvas(width=lock_img.width(), height=lock_img.height())
canvas.create_image(lock_img.width()/2,lock_img.height()/2,image=lock_img)#position this at the center of the canvas. when canvas is the dimensions of the image
canvas.grid(column=1, row=0)

#---------ROW-1------------
website=Label(text="Website       :", font=("Courier",10,"normal"))
website.grid(column=0, row=1)

website_Frame=Frame()
website_Frame.grid(column=1, row=1)

website_entry=Entry(website_Frame, width=28)
website_entry.grid(column=0, row=0)

button=Button(website_Frame, text="search", command=search)
button.grid(column=1, row=0)

# website_entry=Entry(width=45)
# website_entry.focus()#put the cursor in the field(focus)
# website_entry.grid(column=1, row=1)

#---------ROW-2-------------
email_username=Label(text="Email/Username : ", font=("Courier",10,"normal"))
email_username.grid(column=0, row=2)

email_username_entry=Entry(width=45)
email_username_entry.insert(0,"mperuri@gmu.edu")
email_username_entry.grid(column=1, row=2)

#---------ROW-3-------------
Password=Label(text="Password       : ", font=("Courier",10,"normal"))
Password.grid(column=0, row=3)

password_Frame=Frame()
password_Frame.grid(column=1, row=3)

password_entry=Entry(password_Frame, width=28)
password_entry.grid(column=0, row=0)

button=Button(password_Frame, text="generate password", command=generate_password)
button.grid(column=1, row=0)

#---------ROW-4-------------

AddButton=Button(text="Add", width=40, command=save)
AddButton.grid(column=1, row=4)

window.mainloop()
