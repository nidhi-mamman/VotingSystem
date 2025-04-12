import ttkbootstrap as tb
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import tkinter as tk
import subprocess as sb_p
import registerVoter as regV
import admFunc as adFunc


import ttkbootstrap as tb
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import tkinter as tk
import subprocess as sb_p
import registerVoter as regV
import admFunc as adFunc

def log_admin(root, frame1, main_container, admin_ID, password, topbar_frame, home_function, home_icon):
    if admin_ID == "Admin" and password == "admin":
        frame1.destroy()
        AdminHome(root, main_container, topbar_frame, home_function, home_icon)
    else:
        msg = tb.Label(main_container, text="Either ID or Password is Incorrect",
                       bootstyle="danger", font=("Tahoma", 10, "bold"))
        msg.grid(row=5, column=0, columnspan=2, pady=5)

def AdmLogin(root, main_container, topbar_frame, home_function, home_icon):
    root.title("Admin Login")
    root.configure(background="#e2e3e5")

    for widget in main_container.winfo_children():
        widget.destroy()

    container = tb.Frame(main_container, style="Gray.TFrame")
    container.pack()

    tb.Label(container, text="Admin Login", font=('Tahoma', 20, 'bold'), background="#e2e3e5").pack(pady=(0, 10))

    frame1 = tb.Frame(container, style="White.TFrame", padding=30, borderwidth=1, relief="solid")
    frame1.pack()

    user = Image.open('img/user.png').resize((30, 30))
    password = Image.open('img/password.png').resize((30, 30))
    _user = ImageTk.PhotoImage(user)
    _password = ImageTk.PhotoImage(password)

    admin_ID = tb.StringVar()
    password_val = tb.StringVar()

    def set_placeholder(entry_widget, placeholder_text, is_password=False):
        def on_focus_in(event):
            if entry_widget.get() == placeholder_text:
                entry_widget.delete(0, 'end')
                entry_widget.config(foreground='black')
                if is_password:
                    entry_widget.config(show='*')

        def on_focus_out(event):
            if entry_widget.get() == '':
                entry_widget.insert(0, placeholder_text)
                entry_widget.config(foreground='gray')
                if is_password:
                    entry_widget.config(show='')

        entry_widget.insert(0, placeholder_text)
        entry_widget.config(foreground='gray')
        entry_widget.bind('<FocusIn>', on_focus_in)
        entry_widget.bind('<FocusOut>', on_focus_out)

    user_frame = tb.Frame(frame1)
    user_frame.grid(row=1, column=0, columnspan=2, pady=10)
    tb.Label(user_frame, image=_user).pack(side="left", padx=5)
    username_entry = tb.Entry(user_frame, textvariable=admin_ID, font=('Tahoma', 10), width=30, bootstyle="info")
    username_entry.pack(side="left")
    set_placeholder(username_entry, 'Enter your name')

    pass_frame = tb.Frame(frame1)
    pass_frame.grid(row=2, column=0, columnspan=2, pady=10)
    tb.Label(pass_frame, image=_password).pack(side="left", padx=5)
    password_entry = tb.Entry(pass_frame, textvariable=password_val, font=('Tahoma', 10), width=30, bootstyle="info")
    password_entry.pack(side="left")
    set_placeholder(password_entry, 'Enter your password', is_password=True)

    style = tb.Style()
    style.configure("SuccessHover.TButton", font=('Tahoma', 10))
    style.map("SuccessHover.TButton",
              background=[("active", "#3a86ff"), ("!active", "#28a745")],
              foreground=[("pressed", "white"), ("active", "white")])

    login_btn = tb.Button(frame1, text="Login", width=20,
                          style="SuccessHover.TButton",
                          command=lambda: log_admin(root, frame1, main_container,
                                                    admin_ID.get(), password_val.get(),
                                                    topbar_frame, home_function, home_icon))
    login_btn.grid(row=4, column=0, columnspan=2, pady=20)
    login_btn.configure(takefocus=0)

    frame1.image_user = _user
    frame1.image_password = _password

def AdminHome(root, main_container, topbar_frame, home_function, home_icon):
    root.title("Admin")

    back = Image.open('img/back.png').resize((40, 40))
    _back = ImageTk.PhotoImage(back)

    for widget in main_container.winfo_children():
        widget.destroy()
    for widget in topbar_frame.winfo_children():
        widget.destroy()

    style = tb.Style()
    style.configure("Custom.TButton", background="#e2e3e5", foreground="grey", relief="flat", borderwidth=0)
    style.map("Custom.TButton", background=[("active", "#d6d7d9"), ("pressed", "#c5c6c8")])

    tb.Button(topbar_frame, image=_back, text=" Admin", style="Custom.TButton",
              command=lambda: AdminHome(root, main_container, topbar_frame, home_function, home_icon)).pack(side="left", padx=10, pady=10)
    topbar_frame.pack(side="top", fill="x")

    home_label = tb.Label(topbar_frame, text="Go to Homepage",
                          font=('Tahoma', 10, 'underline'),
                          cursor="hand2", bootstyle="info",background="#e2e3e5")
    home_label.pack(side="right", padx=10, pady=10)
    home_label.bind("<Button-1>", lambda e: home_function(root, main_container, topbar_frame, home_icon))

    header_label = tb.Label(main_container, text="Admin Dashboard", font=('Tahoma', 25, 'bold'), bootstyle="dark", background="#e2e3e5")
    header_label.pack(pady=(10, 20))

    white_box = tb.Frame(main_container, style="White.TFrame", padding=30, borderwidth=1, relief="solid")
    white_box.pack()

    tb.Button(white_box, text="Run Server", width=20, bootstyle="primary",
              command=lambda: sb_p.call('start python Server.py', shell=True))\
        .grid(row=1, column=0, columnspan=2, pady=5)

    tb.Button(white_box, text="Register Voter", width=20, bootstyle="success",
              command=lambda: regV.Register(root, main_container))\
        .grid(row=2, column=0, columnspan=2, pady=5)

    tb.Button(white_box, text="Show Votes", width=20, bootstyle="info",
              command=lambda: adFunc.showVotes(root, main_container))\
        .grid(row=3, column=0, columnspan=2, pady=5)

    tb.Button(white_box, text="Reset All", width=20, bootstyle="danger",
              command=lambda: adFunc.resetAll(root, main_container))\
        .grid(row=4, column=0, columnspan=2, pady=5)

    topbar_frame._back = _back


# Example main starter
if __name__ == "__main__":
    root = tb.Window()
    root.state("zoomed")
    root.configure(bg="#e2e3e5")
    root.resizable(False,False)

    # Frame for login form
    style = tb.Style()
    style.configure("White.TFrame", background="white")

    frame1 = tb.Frame(root, style="White.TFrame", padding=30)
    frame1.place(relx=0.5, rely=0.5, anchor="center")

    # Top nav bar (even if blank initially)
    frame3 = tb.Frame(root, padding=10)
    frame3.pack(side="top", fill="x")

    AdmLogin(root, frame1)
    root.mainloop()
