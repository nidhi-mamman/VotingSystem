import os
import subprocess as sb_p
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from Admin import AdmLogin
from voter import voterLogin
from PIL import Image, ImageTk
from tkinter import messagebox


def Home(root, main_container, topbar_frame, _home):
    for widget in main_container.winfo_children():
        widget.destroy()

    style = tb.Style()
    style.configure("Custom.TButton",
                    background="#e2e3e5",
                    foreground="grey",
                    relief="flat",
                    borderwidth=0)
    style.map("Custom.TButton",
              background=[("active", "#d6d7d9"), ("pressed", "#c5c6c8")])

    for widget in topbar_frame.winfo_children():
        widget.destroy()

    tb.Button(
        topbar_frame, text="Home", image=_home, style="Custom.TButton",
        command=lambda: Home(root, main_container, topbar_frame, _home)
    ).pack(anchor='nw', padx=10, pady=10)

    topbar_frame.pack(side=TOP, fill=X)
    root.title("Home")

    label = tb.Label(main_container, text="Vote. Influence. Inspire.", font=('Tahoma', 16, 'bold'), background="#e2e3e5")
    label.pack(pady=(0, 10))

    frame1 = tb.Frame(main_container, style="White.TFrame", padding=30, relief="solid", borderwidth=1)
    frame1.pack()

    def safe_voter_login():
        try:
            voterLogin(root, main_container)
        except Exception as e:
            messagebox.showerror("Server Error", "Server not running! Please start the server and try again.")

    admin = tb.Button(
        frame1, text="  Admin Login", compound="left",
        bootstyle=PRIMARY, width=20,
        command=lambda: AdmLogin(root, main_container, topbar_frame, Home, _home)
    )

    voter = tb.Button(
        frame1, text="  Voter Login", compound="left",
        bootstyle=SUCCESS, width=20, command=safe_voter_login
    )

    newTab = tb.Button(
        frame1, text="New Window", bootstyle=WARNING, width=20,
        command=lambda: sb_p.call('start python homePage.py', shell=True)
    )

    admin.grid(row=1, column=1, pady=10)
    voter.grid(row=2, column=1, pady=10)
    newTab.grid(row=3, column=1, pady=10)



def new_home():
    root = tb.Window()
    root.state('zoomed')
    root.configure(bg="#e2e3e5")
    root.resizable(False,False)

    style = tb.Style()
    style.configure("White.TFrame", background="white")
    style.configure("TopBar.TFrame", background="#e2e3e5")
    style.configure("Gray.TFrame", background="#e2e3e5")

    # Shared central container
    main_container = tb.Frame(root, style="Gray.TFrame")
    main_container.place(relx=0.5, rely=0.5, anchor="center")

    # Top nav bar
    frame2 = tb.Frame(root, style="TopBar.TFrame")
    frame2.pack(side=TOP, fill=X)

    # Load home icon
    home = Image.open('img/home.png').resize((50, 50))
    _home = ImageTk.PhotoImage(home)

    # Initialize Home view
    Home(root, main_container, frame2, _home)

    root.mainloop()


if __name__ == "__main__":
    new_home()
