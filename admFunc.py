import tkinter as tk
import dframe as df
from tkinter import *
from tkinter import messagebox
from dframe import *
from PIL import ImageTk,Image


def resetAll(root,frame1):
    answer = messagebox.askyesno("Confirm Reset", "Are you sure you want to reset all data?")
    if answer:
        df.count_reset()
        df.reset_voter_list()
        def show_msg():
            Label(frame1, text="", bg="#dad7cd").grid(row=10, column=0)
            msg = Message(frame1, text="Reset Complete", font=('Tahoma', 12, 'bold'), fg="green", bg="#dad7cd", width=500)
            msg.grid(row=11, column=0, columnspan=5)
    
            def clear_msg():
                msg.destroy()

            root.after(1500, clear_msg)  
        show_msg()


def showVotes(root,frame1):

    result = df.show_result()
    root.title("Votes")
    root.config(bg="#dad7cd")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="🗳️ Vote Count",bg="#dad7cd", font=('Tahoma', 20, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="",bg="#dad7cd").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((35,35),Image.Resampling.LANCZOS))
    bjpImg = Label(frame1,bg="#dad7cd", image=bjpLogo).grid(row = 2,column = 0)

    congLogo = ImageTk.PhotoImage((Image.open("img/cong.png")).resize((25,38),Image.Resampling.LANCZOS))
    congImg = Label(frame1,bg="#dad7cd", image=congLogo).grid(row = 3,column = 0)

    aapLogo = ImageTk.PhotoImage((Image.open("img/aap.png")).resize((45,30),Image.Resampling.LANCZOS))
    aapImg = Label(frame1,bg="#dad7cd", image=aapLogo).grid(row = 4,column = 0)

    ssLogo = ImageTk.PhotoImage((Image.open("img/ss.png")).resize((40,35),Image.Resampling.LANCZOS))
    ssImg = Label(frame1,bg="#dad7cd", image=ssLogo).grid(row = 5,column = 0)

    notaLogo = ImageTk.PhotoImage((Image.open("img/nota.png")).resize((35,25),Image.Resampling.LANCZOS))
    notaImg = Label(frame1,bg="#dad7cd", image=notaLogo).grid(row = 6,column = 0)


    Label(frame1, text="BJP              :       ", font=('Tahoma', 12, 'bold'),bg="#dad7cd").grid(row = 2, column = 1)
    Label(frame1, text=result['bjp'], font=('Tahoma', 12, 'bold'),bg="#dad7cd").grid(row = 2, column = 2)

    Label(frame1, text=" Cong             :          ", font=('Tahoma', 12, 'bold'),bg="#dad7cd").grid(row = 3, column = 1)
    Label(frame1, text=result['cong'], font=('Tahoma', 12, 'bold'),bg="#dad7cd").grid(row = 3, column = 2)

    Label(frame1, text=" AAP               :          ", font=('Tahoma', 12, 'bold'),bg="#dad7cd").grid(row = 4, column = 1)
    Label(frame1, text=result['aap'], font=('Tahoma', 12, 'bold'),bg="#dad7cd").grid(row = 4, column = 2)

    Label(frame1, text=" Shiv Sena    :          ", font=('Tahoma', 12, 'bold'),bg="#dad7cd").grid(row = 5, column = 1)
    Label(frame1, text=result['ss'], font=('Tahoma', 12, 'bold'),bg="#dad7cd").grid(row = 5, column = 2)

    Label(frame1, text=" NOTA            :          ", font=('Tahoma', 12, 'bold'),bg="#dad7cd").grid(row = 6, column = 1)
    Label(frame1, text=result['nota'], font=('Tahoma', 12, 'bold'),bg="#dad7cd").grid(row = 6, column = 2)

    frame1.pack()
    root.mainloop()


if __name__ == "__main__":
        root = Tk()
        root.geometry('500x500')
        root.config(bg="#dad7cd",relief=GROOVE)
        frame1 = Frame(root)
        showVotes(root,frame1)
