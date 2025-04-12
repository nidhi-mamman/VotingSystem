import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from PIL import Image, ImageTk
import socket

def voteCast(main_container, vote, client_socket):
    for widget in main_container.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode())
    message = client_socket.recv(1024).decode()

    status = "✅ Vote Casted Successfully" if message == "Successful" else "❌ Vote Cast Failed... Try Again"
    style = "success" if message == "Successful" else "danger"

    tb.Label(main_container, text=status, font=("Tahoma", 16, "bold"), bootstyle=style, background="#e2e3e5").pack(pady=40)
    client_socket.close()


def confirm_vote(main_container, vote, client_socket):
    answer = messagebox.askyesno("Confirm Vote", f"Are you sure you want to vote for {vote.upper()}?")
    if answer:
        voteCast(main_container, vote, client_socket)


def votingPg(root, main_container, client_socket):
    # Clear screen
    for widget in main_container.winfo_children():
        widget.destroy()

    root.title("Cast Your Vote")
    root.configure(background="#e2e3e5")

    tb.Label(main_container, text="🗳️ Cast Your Vote", font=("Tahoma", 20, "bold"), background="#e2e3e5").pack(pady=20)

    vote = tb.StringVar(main_container, "-1")

    # Outer white bordered frame
    vote_frame = tb.Frame(main_container, style="White.TFrame", borderwidth=2, relief="solid", padding=20)
    vote_frame.pack(pady=10)

    # Candidate info
    candidates = [
        ("BJP", "Narendra Modi", "img/bjp.png", "bjp", (45, 45), "warning"),
        ("Congress", "Rahul Gandhi", "img/cong.png", "cong", (35, 48), "primary"),
        ("AAP", "Arvind Kejriwal", "img/aap.png", "aap", (55, 40), "info"),
        ("Shiv Sena", "Uddhav Thackeray", "img/ss.png", "ss", (50, 45), "danger"),
        ("NOTA", "", "img/nota.png", "nota", (45, 35), "secondary")
    ]

    images = []

    for i, (party, leader, img_path, value, size, color) in enumerate(candidates):
        frame = tb.Frame(vote_frame, style="White.TFrame")
        frame.pack(pady=10, fill=X)

        img = Image.open(img_path).resize(size, Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        images.append(photo)

        tb.Label(frame, image=photo, background="white").pack(side=LEFT, padx=(0, 10), anchor=W)

        label_text = f"{party}\n{leader}" if leader else party


        tb.Radiobutton(
            frame,
            text=label_text,
            variable=vote,
            value=value,
            bootstyle=f"{color}-toolbutton",
            command=lambda v=value: confirm_vote(main_container, v, client_socket),
            width=30
        ).pack(side=LEFT, padx=10)

    main_container.place(relx=0.5, rely=0.5, anchor="center")

    root.mainloop()

if __name__ == "__main__":
    root = tb.Window()
    root.geometry("600x600")
    root.config(background="#e2e3e5")

    main_container = tb.Frame(root, padding=10)
    main_container.place(relx=0.5, rely=0.5, anchor="center")


    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket = socket.socket()
        host = socket.gethostname()
        port = 4001
        client_socket.connect((host,port)) 
    except:
        client_socket = None
        messagebox.showerror("Connection Error", "Failed to connect to server.")

    if client_socket:
        votingPg(root, main_container, client_socket)
