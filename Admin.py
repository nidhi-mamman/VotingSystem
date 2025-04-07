import subprocess as sb_p
import tkinter as tk
import registerVoter as regV
import admFunc as adFunc
from tkinter import *
from registerVoter import *
from admFunc import *



def AdminHome(root,frame1,frame3):
    
    root.title("Admin")
    back = Image.open('img/back.png')
    back__=back.resize((40,40))
    _back = ImageTk.PhotoImage(back__)
    

    
    for widget in frame1.winfo_children():
        widget.destroy()


    Button(frame3, text="Admin",image= _back,bd=0,bg="#dad7cd", command = lambda: AdminHome(root, frame1, frame3)).grid(row=1,column=0)
    frame3.pack(side=TOP)

    Label(frame1, text="Admin",bg="#dad7cd", font=('Tahoma', 25, 'bold')).grid(row = 0, column = 1)

    #Admin Login
    runServer = Button(frame1, text="Run Server",font=('Tahoma', 12, 'bold'),width=15,height=1,bg="#d6ccc2", command = lambda: sb_p.call('start python Server.py', shell=True))

    #Voter Login
    registerVoter = Button(frame1, text="Register Voter", font=('Tahoma', 12, 'bold'),width=15,height=1,bg="#d6ccc2", command = lambda: regV.Register(root, frame1))

    #Show Votes
    showVotes = Button(frame1, text="Show Votes", font=('Tahoma', 12, 'bold'),width=15,height=1,bg="#d6ccc2", command = lambda: adFunc.showVotes(root, frame1))
    
    #Reset All
    reset = Button(frame1, text="Reset All", font=('Tahoma', 12, 'bold'),width=15,height=1,bg="#d6ccc2", command = lambda: adFunc.resetAll(root, frame1))

    Label(frame1, text="",bg="#dad7cd").grid(row = 2,column = 0)
    Label(frame1, text="",bg="#dad7cd").grid(row = 4,column = 0)
    Label(frame1, text="",bg="#dad7cd").grid(row = 6,column = 0)
    Label(frame1, text="",bg="#dad7cd").grid(row = 8,column = 0)
    runServer.grid(row = 3, column = 1, columnspan = 2)
    registerVoter.grid(row = 5, column = 1, columnspan = 2)
    showVotes.grid(row = 7, column = 1, columnspan = 2)
    reset.grid(row = 9, column = 1, columnspan = 2)
    
    frame1.pack()
    root.mainloop()



def log_admin(root,frame1,admin_ID,password):

    if(admin_ID=="Admin" and password=="admin"):
        frame3 = root.winfo_children()[1]
        AdminHome(root, frame1, frame3)
    else:
        msg = Message(frame1, text="Either ID or Password is Incorrect",bg="#dad7cd",font=("Tahoma",10,"bold"),fg="red", width=500)
        msg.grid(row = 6, column = 0, columnspan = 5)


def AdmLogin(root,frame1):

    root.title("Admin Login")
    root.config(bg="#dad7cd",relief=GROOVE)
       # user icon
    user = Image.open('img/user.png')
    user__=user.resize((50,50))
    _user = ImageTk.PhotoImage(user__)
    
    # password icon
    password = Image.open('img/password.png')
    password__=password.resize((50,50))
    _password = ImageTk.PhotoImage(password__)

    def on_entry_click(event):
       if entry.get() == 'Enter your name':
            entry.delete(0, "end")  
            entry.config(fg='black')

    def on_focusout(event):
       if entry.get() == '':
            entry.insert(0, 'Enter your name')
            entry.config(fg='gray')
    
    def on_entry_click_password(event):
       if entry1.get() == 'Enter your password':
            entry1.delete(0, "end")  
            entry1.config(fg='black')

    def on_focusout_password(event):
       if entry1.get() == '':
            entry1.insert(0, 'Enter your password')
            entry1.config(fg='gray')
    
    
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Admin Login",bg="#dad7cd", font=('Tahoma', 20, 'bold')).grid(row = 0, column = 2, rowspan=1)
    Label(frame1, text="",bg="#dad7cd").grid(row = 1,column = 0)
    Label(frame1, text="Admin ID:   " ,image=_user, anchor="e",bg="#dad7cd", justify=LEFT).grid(row = 2,column = 0)
    Label(frame1, text="Password:   ",image=_password, anchor="e",bg="#dad7cd", justify=LEFT).grid(row = 3,column = 0)

    admin_ID = tk.StringVar()
    password = tk.StringVar()

    entry = Entry(frame1, fg='gray',font=('Tahoma', 10),textvariable=admin_ID)
    entry.insert(0, 'Enter your name') 
    entry.bind('<FocusIn>', on_entry_click)
    entry.bind('<FocusOut>', on_focusout)
    entry.grid(row=2,column=2,ipadx=25,ipady=6)
    entry1 = Entry(frame1, fg='gray',font=('Tahoma', 10),textvariable=password)
    entry1.insert(0, 'Enter your password') 
    entry1.bind('<FocusIn>', on_entry_click_password)
    entry1.bind('<FocusOut>', on_focusout_password)
    entry1.grid(row=3,column=2,ipadx=25,ipady=6)

    sub = Button(frame1, text="Login", font=('Tahoma', 12, 'bold'),width=10,height=1,bg="#d6ccc2", command = lambda: log_admin(root, frame1, admin_ID.get(), password.get()))
    Label(frame1, text="",bg="#dad7cd").grid(row = 0,column = 0)
    sub.grid(row = 4, column = 1, columnspan = 2,padx=20,pady=20)

    frame1.pack()
    root.mainloop()
