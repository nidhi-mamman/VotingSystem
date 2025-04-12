import ttkbootstrap as tb
from ttkbootstrap.constants import *
import socket
from PIL import Image, ImageTk


def establish_connection():
    host = socket.gethostname()
    port = 4001
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        msg = client_socket.recv(1024).decode()
        if msg == "Connection Established":
            return client_socket
        else:
            return 'Fail'
    except Exception as e:
        print("Connection failed:", e)
        return 'Fail'


def failed_return(root, main_container, client_socket, message):
    for widget in main_container.winfo_children():
        widget.destroy()
    if message in ["Connection failed", "Invalid Voter", "Server Error"]:
        message += "... \nTry again..."
    tb.Label(main_container, text=message, font=('Tahoma', 13, 'bold'), foreground="green", background="#dad7cd").pack(pady=30)
    try:
        client_socket.close()
    except:
        pass


def log_server(root, main_container, client_socket, voter_ID, password):
    message = voter_ID + " " + password
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()

    if response == "Authenticate":
        from VotingPage import votingPg
        votingPg(root, main_container, client_socket)
    elif response == "VoteCasted":
        failed_return(root, main_container, client_socket, "Vote has Already been Cast")
    elif response == "InvalidVoter":
        failed_return(root, main_container, client_socket, "Invalid Voter")
    else:
        failed_return(root, main_container, client_socket, "Server Error")


def voterLogin(root, main_container):
    client_socket = establish_connection()
    if client_socket == 'Fail':
        failed_return(root, main_container, None, "Connection failed")
        return

    for widget in main_container.winfo_children():
        widget.destroy()

    main_container.configure(style="Gray.TFrame")

    tb.Label(main_container, text="Voter Login", font=('Tahoma', 20, 'bold'), background="#e2e3e5").pack(pady=(10, 20))

    form_frame = tb.Frame(main_container, padding=20, style="White.TFrame")
    form_frame.pack()

    # Load icons
    user_icon = Image.open('img/user.png').resize((25, 25))
    user_icon = ImageTk.PhotoImage(user_icon)
    pass_icon = Image.open('img/password.png').resize((25, 25))
    pass_icon = ImageTk.PhotoImage(pass_icon)

    # Variables
    voter_ID = tb.StringVar()
    password = tb.StringVar()

    def set_placeholder(entry, text, is_password=False):
        def on_focus_in(event):
            if entry.get() == text:
                entry.delete(0, "end")
                entry.config(foreground="black")
                if is_password:
                    entry.config(show="*")

        def on_focus_out(event):
            if entry.get() == "":
                entry.insert(0, text)
                entry.config(foreground="gray")
                if is_password:
                    entry.config(show="")

        entry.insert(0, text)
        entry.config(foreground="gray")
        entry.bind('<FocusIn>', on_focus_in)
        entry.bind('<FocusOut>', on_focus_out)

    # Voter ID Entry
    tb.Label(form_frame, text="Voter ID:", font=('Tahoma', 10, 'bold'), background="white", compound="left").grid(row=0, column=0, pady=10, sticky="w")
    e1 = tb.Entry(form_frame, textvariable=voter_ID, width=30)
    e1.grid(row=0, column=1, padx=10)
    set_placeholder(e1, "Enter your Voter Id")

    # Password Entry
    tb.Label(form_frame, text="Password:", font=('Tahoma', 10, 'bold'), background="white", compound="left").grid(row=1, column=0, pady=10, sticky="w")
    e3 = tb.Entry(form_frame, textvariable=password, width=30)
    e3.grid(row=1, column=1, padx=10)
    set_placeholder(e3, "Enter your Password", is_password=True)
    
    style = tb.Style()
    style.configure("SuccessHover.TButton", font=('Tahoma', 10))
    style.map("SuccessHover.TButton",
              background=[("active", "#3a86ff"), ("!active", "#28a745")],
              foreground=[("pressed", "white"), ("active", "white")])

    # Login Button
    tb.Button(
        form_frame,
        text="Login",
        style="SuccessHover.TButton",
        width=20,
        command=lambda: log_server(root, main_container, client_socket, voter_ID.get(), password.get())
    ).grid(row=2, column=0, columnspan=2, pady=20)


# Run Test
if __name__ == "__main__":
    root = tb.Window()
    root.title("Voter Login")
    root.geometry("600x450")
    root.configure(bg="#e2e3e5")

    style = tb.Style()
    style.configure("White.TFrame", background="white")
    style.configure("Gray.TFrame", background="#e2e3e5")

    main_container = tb.Frame(root, style="Gray.TFrame")
    main_container.place(relx=0.5, rely=0.5, anchor="center")

    voterLogin(root, main_container)
    root.mainloop()
