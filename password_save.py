import tkinter as tk
from tkinter import ttk, messagebox
# from PIL import ImageTk, Image
import json

import random

# Label setting
TEXT_COLOR = "#dbff00"
BG_COLR = "#5A5A5A"
FONT = ("Courier New", 16, "bold")

# Button setting
BUTTON_BG_COLR = "#90DDF1"
BUTTON_FONT = ("Courier New", 12, "normal")


class PasswordSaveWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Save Password Window")
        self.config(width=400, height=400, bg=BG_COLR, pady=10, padx=10)
        self.password_entry = ""
        self.app_name_entry = ""
        self.username_entry = ""



    def generate_password(self):
        """ Password generating work done here """
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?', '+']
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                   'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        pass_letters = [random.choice(letters) for _ in range(8, 13)]
        pass_symbols = [random.choice(symbols) for _ in range(2, 4)]
        pass_numbers = [random.choice(numbers) for _ in range(2, 5)]

        password_list = pass_letters + pass_symbols + pass_numbers
        random.shuffle(password_list)

        password = "".join(password_list)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)


    def destroySaveWindow(self, w):
        """ Sub window destroy OR closing work is done here """
        self.destroy()


    def storeData(self):
        """ Data saving into file works goes here """
        app_name = self.app_name_entry.get()
        user_name = self.username_entry.get()
        password = self.password_entry.get()

        if len(app_name) == 0 or len(user_name) == 0 or len(password) == 0:
            messagebox.showerror(title="Oops!", message="Please make sure you haven't left any field empty. ")
        else:
            is_okay = messagebox.askokcancel(title=app_name+" Information ", message=f"App Name : {app_name}\nUser Name : {user_name}\n"
                                                                     f"\nPassword : {password} \n \n Are you confirm to save")
            if is_okay:
                new_json_data = {
                    app_name: {
                        "email": user_name,
                        "password": password,
                    }
                }

                try:
                    with open("data.json", "r") as data_file:  # through this file closed automatically
                        # Reading old data
                        data = json.load(data_file)
                except:
                    with open("data.json", "w") as data_file:
                        # Storing updated data
                        json.dump(new_json_data, data_file, indent=4)
                else:
                    # Updating old with new data
                    data.update(new_json_data)
                    with open("data.json", "w") as data_file:
                        # Storing updated data
                        json.dump(data, data_file, indent=4)  # this one is used to write the data

                finally:
                    self.app_name_entry.delete(0, tk.END)
                    self.username_entry.delete(0, tk.END)
                    self.password_entry.delete(0, tk.END)
                    messagebox.showinfo(title="Success!", message=f"{app_name}'s Data Stored Successfully!... ")
                # print("Done")
                # with open("data.txt", "a") as data_file:  # through this file closed automatically
                #     data_file.write(f"{website} | {email} | {password}\n")
                #     website_entry.delete(0, tk.END)
                #     password_entry.delete(0, tk.END)


    def createFields(self):
        """ Creating password saving fields here """
        label = tk.Label(self, text="This is a Save Password Window", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        label.grid(row=0, column=1)

        app_name_label = tk.Label(self, text="App Name: ", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        app_name_label.grid(row=1, column=0)
        username_label = tk.Label(self, text="UserName: ", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        username_label.grid(row=2, column=0)
        password_label = tk.Label(self, text="Password: ", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        password_label.grid(row=3, column=0)

        self.app_name_entry = tk.Entry(self, width=50)
        self.app_name_entry.grid(row=1, column=1, columnspan=2)
        self.username_entry = tk.Entry(self, width=50)
        self.username_entry.grid(row=2, column=1, columnspan=2)
        self.password_entry = tk.Entry(self, text="", width=50)
        self.password_entry.grid(row=3, column=1, columnspan=2)

        # Buttons work done here
        generate_pass = tk.Button(self, text="Generate Pass", command=self.generate_password, width=14, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
        generate_pass.grid(row=4, column=1)

        space_label2 = tk.Label(self, bg=BG_COLR)
        space_label2.grid(row=5, column=1)

        back_button = tk.Button(self, text="Back", command=lambda: self.destroySaveWindow(tk.Toplevel(self)), width=10, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
        back_button.grid(row=6, column=0)
        save_password = tk.Button(self, text="Save", command=self.storeData, width=10, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
        save_password.grid(row=6, column=1)

        # canvas1 = tk.Canvas(self, height=100, width=100, bg=BG_COLR, highlightthickness=0)
        # logo1 = ImageTk.PhotoImage(Image.open("logo.png"))
        # image2 = canvas1.create_image(20, 20, anchor='nw', image=logo1)
        # canvas1.grid(row=7, column=1)





