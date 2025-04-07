import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image

def voteCast(root, frame1, vote_value):
    for widget in frame1.winfo_children():
        widget.destroy()

    try:
        client_socket = socket.socket()
        client_socket.connect(("localhost", 4001))  # Or replace with server IP

        # Send login credentials (example: ID and password)
        client_socket.send("10001 password".encode())
        response = client_socket.recv(1024).decode()

        if not response or response != "Authenticate":
            Label(frame1, text="Authentication Failed", font=('tahoma', 20, 'bold'), bg="#dad7cd").grid(row=1, column=1)
            client_socket.close()
            return

        # Now send the vote
        client_socket.send(vote_value.encode())

        try:
            message = client_socket.recv(1024)
            if not message:
                raise ValueError("Empty response from server")
            message = message.decode()
            print("Server response:", message)

            if message == "Successful":
                Label(frame1, text="Vote Casted Successfully", font=('tahoma', 20, 'bold'), bg="#dad7cd").grid(row=1, column=1)
            else:
                Label(frame1, text="Vote Cast Failed... \nTry again", font=('tahoma', 20, 'bold'), bg="#dad7cd").grid(row=1, column=1)
        except Exception as e:
            print("[CLIENT RECEIVE ERROR]", e)
            Label(frame1, text="Error Receiving Vote Status", font=('tahoma', 20, 'bold'), bg="#dad7cd").grid(row=1, column=1)

        client_socket.close()

    except Exception as e:
        print("[CLIENT ERROR]", e)
        Label(frame1, text="Network Error", font=('tahoma', 20, 'bold'), bg="#dad7cd").grid(row=1, column=1)



def votingPg(root,frame1,client_socket):

    root.title("Cast Vote")
    root.config(bg="#dad7cd")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Cast Vote", font=('tahoma', 20, 'bold'),bg="#dad7cd").grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="",bg="#dad7cd").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "BJP\n\nNarendra Modi", variable = vote, value = "bjp",bg="#d6ccc2", indicator = 0, height = 4, width=15, command = lambda: voteCast(root, frame1, "bjp")).grid(row = 2,column = 1)
    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((45,45), Image.Resampling.LANCZOS))
    bjpImg = Label(frame1, image=bjpLogo,bg="#dad7cd").grid(row = 2,column = 0)

    Radiobutton(frame1, text = "Congress\n\nRahul Gandhi", variable = vote, value = "cong", bg="#d6ccc2",indicator = 0, height = 4, width=15, command = lambda: voteCast(root, frame1, "cong")).grid(row = 3,column = 1)
    congLogo = ImageTk.PhotoImage((Image.open("img/cong.png")).resize((35,48), Image.Resampling.LANCZOS))
    congImg = Label(frame1, image=congLogo,bg="#dad7cd").grid(row = 3,column = 0)

    Radiobutton(frame1, text = "Aam Aadmi Party\n\nArvind Kejriwal", variable = vote, value = "aap",bg="#d6ccc2", indicator = 0, height = 4, width=15, command = lambda: voteCast(root, frame1, "aap") ).grid(row = 4,column = 1)
    aapLogo = ImageTk.PhotoImage((Image.open("img/aap.png")).resize((55,40), Image.Resampling.LANCZOS))
    aapImg = Label(frame1, image=aapLogo,bg="#dad7cd").grid(row = 4,column = 0)

    Radiobutton(frame1, text = "Shiv Sena\n\nUdhav Thakrey", variable = vote, value = "ss",bg="#d6ccc2", indicator = 0, height = 4, width=15, command = lambda: lambda: voteCast(root, frame1, "ss")).grid(row = 5,column = 1)
    ssLogo = ImageTk.PhotoImage((Image.open("img/ss.png")).resize((50,45), Image.Resampling.LANCZOS))
    ssImg = Label(frame1, image=ssLogo,bg="#dad7cd").grid(row = 5,column = 0)

    Radiobutton(frame1, text = "\nNOTA    \n  ", variable = vote, value = "nota",bg="#d6ccc2", indicator = 0, height = 4, width=15, command = lambda:lambda: voteCast(root, frame1, "nota")).grid(row = 6,column = 1)
    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.png")).resize((45,35), Image.Resampling.LANCZOS))
    notaImg = Label(frame1, image=notaLogo,bg="#dad7cd").grid(row = 6,column = 0)

    frame1.pack()
    root.mainloop()


if __name__ == "__main__":
        root = Tk()
        root.geometry('500x500')
        root.config(bg="#dad7cd",relief=GROOVE)
        frame1 = Frame(root)
        client_socket='Fail'
        votingPg(root,frame1,client_socket)
