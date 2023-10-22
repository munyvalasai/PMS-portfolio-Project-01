import tkinter as tk
from tkinter import ttk

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


    def destroyUpdatewindow(self, w):
        self.destroy()


    def createFieldsForUpdate(self):
        label = tk.Label(self, text="This is a Update Password Window", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        label.grid(row=0, column=1)

        # canvas1 = tk.Canvas(self, height=40, width=40, bg=BG_COLR, highlightthickness=0)
        # logo1 = tk.PhotoImage(file="logo1.png")
        # canvas1.create_image(5, 5, image=logo1)
        # canvas1.grid(row=1, column=1)

        app_name_label = tk.Label(self, text="App Name: ", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        app_name_label.grid(row=1, column=0)
        username_label = tk.Label(self, text="UserName: ", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        username_label.grid(row=2, column=0)
        password_old_label = tk.Label(self, text="Old Password: ", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        password_old_label.grid(row=3, column=0)

        password_new_label = tk.Label(self, text="New Password: ", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        password_new_label.grid(row=4, column=0)

        app_name_entry = tk.Entry(self, width=50)
        app_name_entry.grid(row=1, column=1, columnspan=2)
        username_entry = tk.Entry(self, width=50)
        username_entry.grid(row=2, column=1, columnspan=2)
        password_old_entry = tk.Entry(self, width=50)
        password_old_entry.grid(row=3, column=1, columnspan=2)
        password_new_entry = tk.Entry(self, width=50)
        password_new_entry.grid(row=4, column=1, columnspan=2)

        # Buttons work done here
        space_label2 = tk.Label(self, bg=BG_COLR)
        space_label2.grid(row=5, column=1)

        back_button = tk.Button(self, text="Back", command=lambda: self.destroyUpdatewindow(tk.Toplevel(self)), width=10, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
        back_button.grid(row=6, column=0)
        save_password = tk.Button(self, text="Update", width=10, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
        save_password.grid(row=6, column=1)


