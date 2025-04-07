import tkinter as tk
import socket
from tkinter import *
from VotingPage import votingPg
from PIL import Image,ImageTk

def establish_connection():
    host = socket.gethostname()
    port = 4001
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(client_socket)
    message = client_socket.recv(1024)      #connection establishment message   #1
    if(message.decode()=="Connection Established"):
        return client_socket
    else:
        return 'Failed'


def failed_return(root,frame1,client_socket,message):
    for widget in frame1.winfo_children():
        widget.destroy()
    retry_messages = ["Connection failed", "Invalid Voter", "Server Error"]
    if message in retry_messages:
        message += "... \nTry again..."
    Label(frame1, text=message,bg="#dad7cd", font=('Tahoma', 13, 'bold'),fg="green").grid(row = 1, column = 1)
    client_socket.close()
    if message.startswith("Vote has Already been Cast"):
        root.after(1500, lambda: voterLogin(root, frame1))  

def log_server(root,frame1,client_socket,voter_ID,password):
    message = voter_ID + " " + password
    client_socket.send(message.encode()) #2

    message = client_socket.recv(1024) #Authenticatication message
    message = message.decode()

    if(message=="Authenticate"):
        votingPg(root, frame1, client_socket)

    elif(message=="VoteCasted"):
        message = "Vote has Already been Cast"
        failed_return(root,frame1,client_socket,message)

    elif(message=="InvalidVoter"):
        message = "Invalid Voter"
        failed_return(root,frame1,client_socket,message)

    else:
        message = "Server Error"
        failed_return(root,frame1,client_socket,message)



def voterLogin(root,frame1):

    client_socket = establish_connection()
    if(client_socket == 'Failed'):
        message = "Connection failed"
        failed_return(root,frame1,client_socket,message)

    root.title("Voter Login")
    user = Image.open('img/user.png')
    user__=user.resize((50,50))
    _user = ImageTk.PhotoImage(user__)
    
    # password icon
    password = Image.open('img/password.png')
    password__=password.resize((50,50))
    _password = ImageTk.PhotoImage(password__)
    
    def on_entry_click(event):
       if e1.get() == 'Enter your Voter Id':
            e1.delete(0, "end")  
            e1.config(fg='black')

    def on_focusout(event):
       if e1.get() == '':
            e1.insert(0, 'Enter your Voter Id')
            e1.config(fg='gray')
            
    def on_entry_click_pass(event):
       if e3.get() == 'Enter your Password':
            e3.delete(0, "end")  
            e3.config(fg='black')

    def on_focusout_pass(event):
       if e3.get() == '':
            e3.insert(0, 'Enter your Password')
            e3.config(fg='gray')
    

    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Voter Login",bg="#dad7cd", font=('Tahoma', 20, 'bold')).grid(row = 0, column = 2, rowspan=1)
    Label(frame1, text="",bg="#dad7cd").grid(row = 1,column = 0)
    Label(frame1, text="Voter ID:      ",image=_user, anchor="e",bg="#dad7cd",font=('Tahoma', 10, 'bold'),justify=LEFT).grid(row = 2,column = 0,pady=5)
    Label(frame1, text="Password:   ",image=_password, anchor="e",bg="#dad7cd",font=('Tahoma', 10, 'bold'), justify=LEFT).grid(row = 3,column = 0,pady=5)

    voter_ID = tk.StringVar()
    password = tk.StringVar()

    e1 = Entry(frame1, fg='gray',font=('Tahoma', 10),textvariable=voter_ID)
    e1.insert(0, 'Enter your Voter Id') 
    e1.bind('<FocusIn>', on_entry_click)
    e1.bind('<FocusOut>', on_focusout)
    e1.grid(row = 2,column = 2,ipadx=25,ipady=6)
    e3 = Entry(frame1, fg='gray',font=('Tahoma', 10),textvariable=password)
    e3.insert(0, 'Enter your Password') 
    e3.bind('<FocusIn>', on_entry_click_pass)
    e3.bind('<FocusOut>', on_focusout_pass)
    e3.grid(row = 3,column = 2,ipadx=25,ipady=6)

    sub = Button(frame1, text="Login",bg="#d6ccc2",font=('Tahoma', 12, 'bold'), width=12,height=1, command = lambda: log_server(root, frame1, client_socket, voter_ID.get(), password.get()))
    Label(frame1, text="",bg="#dad7cd").grid(row = 4,column = 0)
    sub.grid(row = 5, column = 0, columnspan = 5)

    frame1.pack()
    root.mainloop()


if __name__ == "__main__":
        root = Tk()
        root.geometry('500x500')
        root.config(bg="#dad7cd",relief=GROOVE)
        frame1 = Frame(root)
        voterLogin(root,frame1)
