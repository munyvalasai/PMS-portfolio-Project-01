import tkinter as tk
from tkinter import messagebox

# Custom classes importing work here
from password_save import PasswordSaveWindow
from retrieve_password import RetrievePasswordWindow
from password_update import PasswordUpdateWindow

counter = 0
root = None
obj = None

# Label setting
TEXT_COLOR = "#dbff00"
BG_COLR = "#5A5A5A"
FONT = ("Courier New", 16, "bold")

# Button setting
BUTTON_BG_COLR = "#90DDF1"
BUTTON_FONT = ("Courier New", 18, "normal")


def openSavePasswordWindow():
    """ Open Password Create window functionality done here!... """
    global counter
    global obj
    if (counter < 1):
        create_pass_window = PasswordSaveWindow(counter=counter)
        create_pass_window.createFields()
        counter += 1
        obj = create_pass_window
    else:
        if obj.counter == 1:
            print("Window is already opened")
        else:
            counter -= 1
            create_pass_window = PasswordSaveWindow(counter=counter)
            # create_pass_window.destroySaveWindow()
            create_pass_window.createFields()
            counter += 1
            obj = create_pass_window

    # create_pass_window = PasswordSaveWindow(top)
    # # create_pass_window.destroySaveWindow()
    # create_pass_window.createFields()




def openRetrievePassWindow():
    """ Open Password retrieve Window functionality done here!... """
    global counter
    global obj
    if (counter < 1):
        retrieve_pass_window = RetrievePasswordWindow(counter=counter)
        retrieve_pass_window.retrievePassFields()
        counter += 1
        obj = retrieve_pass_window
    else:
        if obj.counter == 1:
            print("Window is already opened")
        else:
            counter -= 1
            retrieve_pass_window = RetrievePasswordWindow(counter=counter)
            retrieve_pass_window.retrievePassFields()
            counter += 1
            obj = retrieve_pass_window


def openUpdatePassWindow():
    """ Open Password Update Window functionality done here!... """
    global counter
    global obj
    if (counter < 1):
        update_pass_window = PasswordUpdateWindow(counter=counter)
        update_pass_window.createFieldsForUpdate()
        counter += 1
        obj = update_pass_window
    else:
        if obj.counter == 1:
            print("Window is already opened")
        else:
            counter -= 1
            update_pass_window = PasswordUpdateWindow(counter=counter)
            update_pass_window.createFieldsForUpdate()
            counter += 1
            obj = update_pass_window



def exitWindow():
    root.destroy()

# Setting up the root screen like title, minsize etc
root = tk.Tk()        # tk.Tk(className="My first GIU Program in Tkinter") (Passing the title)
root.title("Portfolio Project-01 in Tkinter")
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

save_pass_button = tk.Button(root, text="Save Password", width=20, command=openSavePasswordWindow, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
# save_pass_button.bind("<Button>", lambda e: PasswordSaveWindow(root))
save_pass_button.grid(row=2, column=1)

retrieve_pass_button = tk.Button(root, text="Retrieve Password", width=20, command=openRetrievePassWindow, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
retrieve_pass_button.grid(row=3, column=1)

update_pass_button = tk.Button(root, text="Update Password", width=20, command=openUpdatePassWindow, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
update_pass_button.grid(row=4, column=1)

exit_button = tk.Button(root, text="Exit", width=8, command=exitWindow, bg=BUTTON_BG_COLR, font=BUTTON_FONT)
exit_button.grid(row=5, column=1)

#  to set all child widgets padding
for widget in root.winfo_children():
    widget.grid_configure(padx=8, pady=8)

tk.mainloop()
