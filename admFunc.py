import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from PIL import Image, ImageTk
import dframe as df
from ttkbootstrap.widgets import Meter, Progressbar
from ttkbootstrap.constants import INFO, SUCCESS, WARNING, DANGER, PRIMARY

def resetAll(root, frame1):
    current_data = df.show_result()
    
    # Check if all values are already 0
    if all(v == 0 for v in current_data.values()):
        msg = tb.Label(frame1, text="⚠️ Data is already reset.", font=('Tahoma', 12, 'bold'),
                       bootstyle="warning", background="#e2e3e5")
        msg.pack(pady=(10, 5))

        def clear_msg():
            msg.destroy()

        root.after(1500, clear_msg)
        return
    
    answer = messagebox.askyesno("Confirm Reset", "Are you sure you want to reset all data?")
    if answer:
        df.count_reset()
        df.reset_voter_list()

        msg = tb.Label(frame1, text="✅ Reset Complete", font=('Tahoma', 12, 'bold'), bootstyle="success",background="#e2e3e5")
        msg.pack(pady=(10, 5))


        def clear_msg():
            msg.destroy()

        root.after(1500, clear_msg)

def showVotes(root, main_container):

    # Clear main container
    for widget in main_container.winfo_children():
        widget.destroy()

    main_container.configure(style="Gray.TFrame")
    result = df.show_result()
    root.title("Vote Count")

    # Total votes to calculate percentages
    total_votes = sum(result.values()) or 1  # Avoid divide by zero, but ensure it's not 0

    # Heading
    tb.Label(
        main_container,
        text="🗳️ Vote Count",
        font=('Tahoma', 20, 'bold'),
        background="#e2e3e5"
    ).pack(pady=(20, 10))

    # White form
    frame1 = tb.Frame(main_container, style="White.TFrame",borderwidth=2,
    relief="solid", padding=20)
    frame1.pack()

    parties = [
        ("BJP", "img/bjp.png", result.get('bjp', 0), (35, 35), "warning"),   # orange
        ("Congress", "img/cong.png", result.get('cong', 0), (25, 38), "primary"),  # blue
        ("AAP", "img/aap.png", result.get('aap', 0), (45, 30), "info"),      # teal
        ("Shiv Sena", "img/ss.png", result.get('ss', 0), (40, 35), "danger"), # red
        ("NOTA", "img/nota.png", result.get('nota', 0), (35, 25), "secondary"), # grey
    ]

    images = []

    for i, (name, path, count, size, color) in enumerate(parties):
        img = Image.open(path).resize(size, Image.Resampling.LANCZOS)
        logo = ImageTk.PhotoImage(img)
        images.append(logo)

        tb.Label(frame1, image=logo, background="white").grid(row=i*2, column=0, padx=10, pady=(10, 0), rowspan=2)
        tb.Label(frame1, text=f"{name}:", font=('Tahoma', 11, 'bold'), background="white").grid(row=i*2, column=1, sticky="w", pady=5)
        tb.Label(frame1, text=str(count), font=('Tahoma', 11), background="white").grid(row=i*2, column=2, sticky="e", pady=5)

        # Safeguard against 0% showing up as full (if there are no votes)
        percent = int((count / total_votes) * 100) if total_votes > 0 else 0

        pb = Progressbar(frame1, bootstyle=color, length=200, value=percent, maximum=100)
        pb.grid(row=i*2+1, column=1, columnspan=2, pady=(0, 10), sticky="we")

    frame1.pack(padx=20, pady=20)
    root.mainloop()


# Main
if __name__ == "__main__":
    root = tb.Window()
    root.config(background="#e2e3e5")
    root.geometry('500x500')
    frame1 = tb.Frame(root, padding=10)
    frame1.pack(fill=BOTH, expand=True)
    showVotes(root, frame1)
