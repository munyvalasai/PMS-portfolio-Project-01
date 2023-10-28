import tkinter as tk
from tkinter import ttk

import json
from tkinter import messagebox

# Label setting
TEXT_COLOR = "#dbff00"
BG_COLR = "#5A5A5A"
FONT = ("Courier New", 16, "bold")

# Button setting
BUTTON_BG_COLR = "#90DDF1"
BUTTON_FONT = ("Courier New", 12, "normal")


class RetrievePasswordWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Retrieve Password Window")
        self.config(width=400, height=400, bg=BG_COLR, pady=10, padx=10)
        self.user_name = ""
        self.app_password = ""
        self.app_name_entry = ''

    def find_password(self):
        """ Function to get Password of website """
        try:
            website = self.app_name_entry.get()
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No data file found!...")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                self.user_name = email
                self.app_password = password

                username_label = tk.Label(self, text=f"UserName: {self.user_name}", bg=BG_COLR, foreground=TEXT_COLOR,
                                          font=FONT)
                username_label.grid(row=3, column=1)
                password_label = tk.Label(self, text=f"Password: {self.app_password}", bg=BG_COLR,
                                          foreground=TEXT_COLOR, font=FONT)
                password_label.grid(row=4, column=1)

                # messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showerror(title="Error", message=f"No details found for the {website}.")

        finally:
            self.app_name_entry.delete(0, tk.END)


    def destroyRetrievewindow(self, w):
        """ Sub window destroy OR closing work is done here """
        self.destroy()


    def retrievePassFields(self):
        """ Retrieving password fields work is done here """
        label = tk.Label(self, text="This is a Retrieve Password Window", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        label.grid(row=0, column=1)

        space_label2 = tk.Label(self, bg=BG_COLR)
        space_label2.grid(row=1, column=1)

        app_name_label = tk.Label(self, text="App Name: ", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        app_name_label.grid(row=2, column=0)
        username_label = tk.Label(self, text=f"UserName: {self.user_name}", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        username_label.grid(row=3, column=1)
        password_label = tk.Label(self, text=f"Password: {self.app_password}", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        password_label.grid(row=4, column=1)

        self.app_name_entry = tk.Entry(self, width=40)
        self.app_name_entry.grid(row=2, column=1, columnspan=2)

        space_label2 = tk.Label(self, bg=BG_COLR)
        space_label2.grid(row=5, column=1)

        back_button = tk.Button(self, text="Back", command=lambda: self.destroyRetrievewindow(tk.Toplevel(self)), width=10, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
        back_button.grid(row=6, column=0)
        save_password = tk.Button(self, text="Get", command=self.find_password, width=10, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
        save_password.grid(row=6, column=1)


