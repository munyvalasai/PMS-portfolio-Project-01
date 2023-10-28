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


class PasswordUpdateWindow(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Update Password Window")
        self.config(width=400, height=400, bg=BG_COLR, pady=10, padx=10)
        self.app_name_entry = ''
        self.username_entry = ""
        self.password_old_entry = ""
        self.password_new_entry = ""

    def updatePassword(self):
        """ Update Password functionality goes here """
        try:
            app_name = self.app_name_entry.get()
            username = self.username_entry.get()
            old_pass = self.password_old_entry.get()
            new_pass = self.password_new_entry.get()
            with open("data.json") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No data file found!...")

        else:

            if len(app_name) == 0 or len(username) == 0 or len(old_pass) == 0 or len(new_pass) == 0:
                messagebox.showerror(title="Oops!", message="Please make sure you haven't left any field empty. ")
            else:
                if app_name in data:

                    email = data[app_name]['email']
                    password = data[app_name]['password']

                    if email == username and password == old_pass:

                        data[app_name]['password'] = new_pass
                        with open("data.json", "w") as a_file:
                            json.dump(data, a_file, indent=4)

                        self.app_name_entry.delete(0, tk.END)
                        self.username_entry.delete(0, tk.END)
                        self.password_old_entry.delete(0, tk.END)
                        self.password_new_entry.delete(0, tk.END)
                        messagebox.showinfo(title="Success!", message=f"{app_name}'s Password Updated Successfully!... ")

                    else:
                        messagebox.showerror(title="Error", message=f"You entered invalid Username/Password for this {app_name}. ")

                else:
                    messagebox.showerror(title="Error", message=f"No any Website exist for this name: {app_name}.")


    def destroyUpdatewindow(self, w):
        """ Sub window destroy OR closing work is done here """
        self.destroy()

    def createFieldsForUpdate(self):
        """ Creating password updating fields here """
        label = tk.Label(self, text="This is a Update Password Window", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        label.grid(row=0, column=1)

        app_name_label = tk.Label(self, text="App Name: ", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        app_name_label.grid(row=1, column=0)
        username_label = tk.Label(self, text="UserName: ", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        username_label.grid(row=2, column=0)
        password_old_label = tk.Label(self, text="Old Password: ", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        password_old_label.grid(row=3, column=0)

        password_new_label = tk.Label(self, text="New Password: ", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        password_new_label.grid(row=4, column=0)

        self.app_name_entry = tk.Entry(self, width=50)
        self.app_name_entry.grid(row=1, column=1, columnspan=2)
        self.username_entry = tk.Entry(self, width=50)
        self.username_entry.grid(row=2, column=1, columnspan=2)
        self.password_old_entry = tk.Entry(self, width=50)
        self.password_old_entry.grid(row=3, column=1, columnspan=2)
        self.password_new_entry = tk.Entry(self, width=50)
        self.password_new_entry.grid(row=4, column=1, columnspan=2)

        # Buttons work done here
        space_label2 = tk.Label(self, bg=BG_COLR)
        space_label2.grid(row=5, column=1)

        back_button = tk.Button(self, text="Back", command=lambda: self.destroyUpdatewindow(tk.Toplevel(self)), width=10, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
        back_button.grid(row=6, column=0)
        save_password = tk.Button(self, text="Update", command=self.updatePassword, width=10, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
        save_password.grid(row=6, column=1)


