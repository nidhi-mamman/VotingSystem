import tkinter as tk
import socket
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

def voteCast(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode()) #4

    message = client_socket.recv(1024) #Success message
    print(message.decode()) #5
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Vote Casted Successfully",bg="#dad7cd", font=('Tahoma', 20, 'bold')).grid(row = 1, column = 1)
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again",bg="#dad7cd", font=('Tahoma', 20, 'bold')).grid(row = 1, column = 1)

    client_socket.close()
    
    
def confirm_vote(root, frame1, vote, client_socket):
    answer = messagebox.askyesno("Confirm Vote", f"Are you sure you want to vote for {vote.upper()}?")
    if answer:
        voteCast(root, frame1, vote, client_socket)



def votingPg(root,frame1,client_socket):

    root.title("Cast Vote")
    root.config(bg="#dad7cd")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Cast Vote", font=('tahoma', 20, 'bold'),bg="#dad7cd").grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="",bg="#dad7cd").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "BJP\n\nNarendra Modi", variable = vote, value = "bjp", indicator = 0, height = 4, width=15, command = lambda: confirm_vote(root,frame1,"bjp",client_socket)).grid(row = 2,column = 1)
    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((45,45),Image.Resampling.LANCZOS))
    bjpImg = Label(frame1, image=bjpLogo).grid(row = 2,column = 0)

    Radiobutton(frame1, text = "Congress\n\nRahul Gandhi", variable = vote, value = "cong", indicator = 0, height = 4, width=15, command = lambda: confirm_vote(root,frame1,"cong",client_socket)).grid(row = 3,column = 1)
    congLogo = ImageTk.PhotoImage((Image.open("img/cong.png")).resize((35,48),Image.Resampling.LANCZOS))
    congImg = Label(frame1, image=congLogo).grid(row = 3,column = 0)

    Radiobutton(frame1, text = "Aam Aadmi Party\n\nArvind Kejriwal", variable = vote, value = "aap", indicator = 0, height = 4, width=15, command = lambda: confirm_vote(root,frame1,"aap",client_socket) ).grid(row = 4,column = 1)
    aapLogo = ImageTk.PhotoImage((Image.open("img/aap.png")).resize((55,40),Image.Resampling.LANCZOS))
    aapImg = Label(frame1, image=aapLogo).grid(row = 4,column = 0)

    Radiobutton(frame1, text = "Shiv Sena\n\nUdhav Thakrey", variable = vote, value = "ss", indicator = 0, height = 4, width=15, command = lambda: confirm_vote(root,frame1,"ss",client_socket)).grid(row = 5,column = 1)
    ssLogo = ImageTk.PhotoImage((Image.open("img/ss.png")).resize((50,45),Image.Resampling.LANCZOS))
    ssImg = Label(frame1, image=ssLogo).grid(row = 5,column = 0)

    Radiobutton(frame1, text = "\nNOTA    \n  ", variable = vote, value = "nota", indicator = 0, height = 4, width=15, command = lambda: confirm_vote(root,frame1,"nota",client_socket)).grid(row = 6,column = 1)
    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.png")).resize((45,35),Image.Resampling.LANCZOS))
    notaImg = Label(frame1, image=notaLogo).grid(row = 6,column = 0)
    
   

    frame1.pack()
    root.mainloop()


if __name__ == "__main__":
        root = Tk()
        root.geometry('600x600')
        root.resizable(False,False)
        root.config(bg="#dad7cd",relief=GROOVE)
        frame1 = Frame(root)
        client_socket='Fail'
        votingPg(root,frame1,client_socket)
