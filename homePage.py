import os
import subprocess as sb_p
import tkinter as tk
from tkinter import *
from Admin import AdmLogin
from voter import voterLogin
from PIL import Image,ImageTk
from tkinter import messagebox


def Home(root, frame1, frame2,_image, _admin, _voter ):

    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()

    Button(frame2,image=_image, text="Home", bg="#dad7cd", width=50,height=50,bd=0,command = lambda: Home(root, frame1, frame2,_image, _admin, _voter )).grid(row=0,column=0)
    Label(frame2,bg="#dad7cd", text="                                                                         ").grid(row = 0,column = 1)
    Label(frame2,bg="#dad7cd", text="                                                                         ").grid(row = 0,column = 2)
    Label(frame2,bg="#dad7cd", text="         ").grid(row = 1,column = 1)
    frame2.pack(side=TOP)

    root.title("Home")

    Label(frame1, text="Vote. Influence. Inspire.",bg="#dad7cd", font=('Tahoma', 20, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="",bg="#dad7cd").grid(row = 1,column = 0)

    # Voter Login - wrapped with error handling
    def safe_voter_login():
        try:
            voterLogin(root, frame1)
        except Exception as e:
            messagebox.showerror("Server Error", "Server not running! Please start the server and try again.")
    
    #Admin Login
    admin = Button(frame1,image= _admin, text="  Admin Login",font=('Tahoma', 12, 'bold'),compound="left",bg="#d6ccc2", width=175,height=50, command = lambda: AdmLogin(root, frame1))

    admin.grid(ipady=5)

    #Voter Login
    voter = Button(frame1,image= _voter , text="  Voter Login", font=('Tahoma', 12, 'bold'),compound="left",bg="#d6ccc2", width=175,height=50, command =safe_voter_login)
    voter.grid(ipady=5)
    #New Tab
    newTab = Button(frame1, text="New Window",font=('Tahoma', 12, 'bold'),bg="#d6ccc2", width=16,height=2, command = lambda: sb_p.call('start python homePage.py', shell=True))

    Label(frame1, text="",bg="#dad7cd",).grid(row = 2,column = 0)
    Label(frame1, text="",bg="#dad7cd",).grid(row = 4,column = 0)
    Label(frame1, text="",bg="#dad7cd",).grid(row = 6,column = 0)
    admin.grid(row = 3, column = 1, columnspan = 2)
    voter.grid(row = 5, column = 1, columnspan = 2)
    newTab.grid(row = 7, column = 1, columnspan = 2)

    frame1.pack()
    root.mainloop()
    

def new_home():
    root = Tk()
    root.geometry("500x500")
    root.resizable(False, False)  
    root.config(bg="#dad7cd",relief=GROOVE)
    #home icon
    image = Image.open('img/home.png')
    image__=image.resize((40,40))
    _image = ImageTk.PhotoImage(image__)
    #admin button image``
    admin = Image.open('img/admin1.png')
    admin__=admin.resize((45,45))
    _admin = ImageTk.PhotoImage(admin__)
    #voter button image
    voter = Image.open('img/voter.png')
    voter__=voter.resize((50,50))
    _voter = ImageTk.PhotoImage(voter__)
    
    frame1 = Frame(root,bg="#dad7cd")
    frame2 = Frame(root,bg="#dad7cd")
 
    Home(root, frame1, frame2,_image, _admin, _voter )


if __name__ == "__main__":
    new_home()



