import tkinter as tk
from tkinter import ttk

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
        self.user_name = "Manesh"
        self.app_password = "Password"


    def destroyRetrievewindow(self, w):
        self.destroy()


    def retrievePassFields(self):
        label = tk.Label(self, text="This is a Retrieve Password Window", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        label.grid(row=0, column=1)

        # canvas1 = tk.Canvas(self, height=40, width=40, bg=BG_COLR, highlightthickness=0)
        # logo1 = tk.PhotoImage(file="logo1.png")
        # canvas1.create_image(5, 5, image=logo1)
        # canvas1.grid(row=1, column=1)

        space_label2 = tk.Label(self, bg=BG_COLR)
        space_label2.grid(row=1, column=1)

        app_name_label = tk.Label(self, text="App Name: ", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        app_name_label.grid(row=2, column=0)
        username_label = tk.Label(self, text=f"UserName: {self.user_name}", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        username_label.grid(row=3, column=1)
        password_label = tk.Label(self, text=f"Password: {self.app_password}", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
        password_label.grid(row=4, column=1)
        #
        app_name_entry = tk.Entry(self, width=40)
        app_name_entry.grid(row=2, column=1, columnspan=2)

        space_label2 = tk.Label(self, bg=BG_COLR)
        space_label2.grid(row=5, column=1)

        back_button = tk.Button(self, text="Back", command=lambda: self.destroyRetrievewindow(tk.Toplevel(self)), width=10, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
        back_button.grid(row=6, column=0)
        save_password = tk.Button(self, text="Get", width=10, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
        save_password.grid(row=6, column=1)


