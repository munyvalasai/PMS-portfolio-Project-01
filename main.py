import tkinter as tk
from tkinter import messagebox, ttk

# Custom classes importing work here
from password_save import PasswordSaveWindow
from retrieve_password import RetrievePasswordWindow
from password_update import PasswordUpdateWindow

top = None
counter = 1
root = None

# Label setting
TEXT_COLOR = "#dbff00"
BG_COLR = "#5A5A5A"
FONT = ("Courier New", 16, "bold")

# Button setting
BUTTON_BG_COLR = "#90DDF1"
BUTTON_FONT = ("Courier New", 18, "normal")


def openSavePasswordWindow():
    """ Open Password Create window functionality done here!... """
    global top
    global counter

    if (counter < 2):
        create_pass_window = PasswordSaveWindow(top)
        # create_pass_window.destroySaveWindow()
        create_pass_window.createFields()
        counter += 1
    else:
        print("Window is already opened")
        # print(counter)




def openRetrievePassWindow():
    """ Open Password retrieve Window functionality done here!... """
    retrieve_pass_window = RetrievePasswordWindow(root)
    retrieve_pass_window.retrievePassFields()


def openUpdatePassWindow():
    """ Open Password Update Window functionality done here!... """
    update_pass_window = PasswordUpdateWindow(root)
    update_pass_window.createFieldsForUpdate()


# Setting up the root screen like title, minsize etc
root = tk.Tk()        # tk.Tk(className="My first GIU Program in Tkinter") (Passing the title)
root.title("My first GIU Program in Tkinter")
root.config(padx=10, pady=10)

root['background'] = BG_COLR  # OR root.configure(bg='#D3FF2F')
root.minsize(width=400, height=400)  # OR root.geometry("600x400")


# labeling and text fields
my_label = tk.Label(text="Welcome to Password Management System.", bg=BG_COLR, foreground=TEXT_COLOR, font=FONT)
my_label.grid(row=0, column=1)

canvas = tk.Canvas(height=100, width=100, bg=BG_COLR, highlightthickness=0)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(50, 50, image=logo)
canvas.grid(row=1, column=1)

# This is used for skipping one row
space_label = tk.Label(bg=BG_COLR)
space_label.grid(row=2, column=1)


save_pass_button = tk.Button(root, text="Save Password", width=20, command=openSavePasswordWindow, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
# save_pass_button.bind("<Button>", lambda e: PasswordSaveWindow(root))
save_pass_button.grid(row=3, column=1)


# This is used for skipping one row
space_label1 = tk.Label(bg=BG_COLR)
space_label1.grid(row=4, column=1)

retrieve_pass_button = tk.Button(root, text="Retrieve Password", width=20, command=openRetrievePassWindow, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
retrieve_pass_button.grid(row=5, column=1)


# This is used for skipping one row
space_label2 = tk.Label(bg=BG_COLR)
space_label2.grid(row=6, column=1)

update_pass_button = tk.Button(root, text="Update Password", width=20, command=openUpdatePassWindow, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
update_pass_button.grid(row=7, column=1)

tk.mainloop()
