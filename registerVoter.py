import tkinter as tk
import dframe as df
import Admin as adm
from tkinter import ttk
from Admin import *
from tkinter import *
from dframe import *

def reg_server(root,frame1,name,sex,zone,city,passw,msg_label,e2):
    if passw.get().strip() == '' or sex.get() == "-- Select Gender --":
        msg_label.config(text="Error: Missing Fields", fg="red")
        return -1

    vid = df.taking_data_voter(name.get(), sex.get(), zone.get(), city.get(), passw.get())
    if vid == -1:
        msg_label.config(text="You are already registered!", fg="red")
        
        name.set("")
        sex.set("-- Select Gender --")
        zone.set("")
        city.set("")
        passw.set("")
        e2.focus_set()
        return

    msg_label.config(text=f"Registered Successfully! VOTER ID: {vid}", fg="green")
    
    name.set("")
    sex.set("-- Select Gender --")
    zone.set("")
    city.set("")
    passw.set("")
    e2.focus_set()
    def redirect_to_login():
        from voter import voterLogin
        voterLogin(root, frame1)

    root.after(1500, redirect_to_login)

    return

def Register(root,frame1):

    root.title("Register Voter")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Register Voter",bg="#dad7cd", font=('Tahoma', 20, 'bold')).grid(row = 0, column = 2, rowspan=1)
    Label(frame1, text="",bg="#dad7cd").grid(row = 1,column = 0)
    Label(frame1, text="Name:   ", anchor="e",bg="#dad7cd",font=('Tahoma', 10, 'bold'), justify=LEFT).grid(row = 3,column = 0,pady=5)
    Label(frame1, text="Sex:   ", anchor="e",bg="#dad7cd",font=('Tahoma', 10, 'bold'), justify=LEFT).grid(row = 4,column = 0,pady=5)
    Label(frame1, text="Zone:   ", anchor="e",bg="#dad7cd",font=('Tahoma', 10, 'bold'), justify=LEFT).grid(row = 5,column = 0,pady=5)
    Label(frame1, text="City:   ", anchor="e",bg="#dad7cd",font=('Tahoma', 10, 'bold'), justify=LEFT).grid(row = 6,column = 0,pady=5)
    Label(frame1, text="Password:   ", anchor="e",bg="#dad7cd",font=('Tahoma', 10, 'bold'), justify=LEFT).grid(row = 7,column = 0,pady=5)

    name = tk.StringVar()
    sex = tk.StringVar()
    zone = tk.StringVar()
    city = tk.StringVar()
    password = tk.StringVar()

    e2 = Entry(frame1, textvariable = name)
    e2.grid(row = 3, column = 2)
    e5 = Entry(frame1, textvariable = zone)
    e5.grid(row = 5, column = 2)
    e6 = Entry(frame1, textvariable = city)
    e6.grid(row = 6, column = 2)
    e7 = Entry(frame1, textvariable = password,show="*")
    e7.grid(row = 7, column = 2)

    e4 = ttk.Combobox(frame1, textvariable = sex, width=17, state='readonly')
    e4['values'] = ("-- Select Gender --", "Male", "Female", "Transgender")
    e4.grid(row = 4, column = 2)
    e4.current(0) 


    reg = Button(frame1, text="Register",bg="#d6ccc2",font=('Tahoma', 12, 'bold'), width=12,height=1, command = lambda: reg_server(root, frame1, name, sex, zone, city, password,msg_label,e2))
    Label(frame1, text="",bg="#dad7cd").grid(row = 8,column = 0)
    reg.grid(row = 9, column = 0, columnspan = 5)
    
    Label(frame1, text="", bg="#dad7cd").grid(row=10)
    
    msg_label = Label(frame1, text="", bg="#dad7cd", fg="red", font=('Tahoma', 10, 'bold'))
    msg_label.grid(row=11, column=0, columnspan=5)

    frame1.pack()
    root.mainloop()


if __name__ == "__main__":
        root = Tk()
        root.geometry('500x500')
        root.config(bg="#dad7cd",relief=GROOVE)
        frame1 = Frame(root)
        Register(root,frame1)
