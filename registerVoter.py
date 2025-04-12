import ttkbootstrap as tb
from ttkbootstrap.constants import *
import dframe as df


def reg_server(root, frame1, name, sex, zone, city, passw, msg_label, e2, main_container):
    if (
        name.get().strip() == "" or name.get() == "Enter your name" or
        zone.get().strip() == "" or zone.get() == "Enter your zone" or
        city.get().strip() == "" or city.get() == "Enter your city" or
        passw.get().strip() == "" or passw.get() == "Enter your password" or
        sex.get() == ""
    ):
        msg_label.config(text="Error: Missing Fields", foreground="red")
        root.after(1500, lambda: msg_label.config(text=""))
        return -1

    vid = df.taking_data_voter(name.get(), sex.get(), zone.get(), city.get(), passw.get())
    if vid == -1:
        msg_label.config(text="You are already registered!", foreground="red")
        name.set("")
        sex.set("")
        zone.set("")
        city.set("")
        passw.set("")
        e2.focus_set()
        return

    msg_label.config(text=f"Registered Successfully! VOTER ID: {vid}", foreground="green")
    name.set("")
    sex.set("")
    zone.set("")
    city.set("")
    passw.set("")
    e2.focus_set()

    def redirect_to_login():
        from voter import voterLogin
        voterLogin(root, main_container)

    root.after(1500, redirect_to_login)


def Register(root, main_container):
    # Clear main container
    for widget in main_container.winfo_children():
        widget.destroy()

    main_container.configure(style="Gray.TFrame")

    # Heading
    tb.Label(main_container, text="Register Voter", font=('Tahoma', 20, 'bold'), background="#e2e3e5").pack(pady=(0, 10))

    # Frame1 = form frame with white background
    frame1 = tb.Frame(main_container, style="White.TFrame", padding=20)
    frame1.pack()

    # Variables
    name = tb.StringVar()
    sex = tb.StringVar(value="")  # default value empty
    zone = tb.StringVar()
    city = tb.StringVar()
    password = tb.StringVar()

    def set_placeholder(entry_widget, placeholder_text, is_password=False):
        def on_focus_in(event):
            if entry_widget.get() == placeholder_text:
               entry_widget.delete(0, 'end')
               entry_widget.config(foreground='black')
               if is_password:
                   entry_widget.config(show='*')

        def on_focus_out(event):
            if entry_widget.get() == '':
               entry_widget.insert(0, placeholder_text)
               entry_widget.config(foreground='gray')
               if is_password:
                  entry_widget.config(show='')

        entry_widget.insert(0, placeholder_text)
        entry_widget.config(foreground='gray')
        entry_widget.bind('<FocusIn>', on_focus_in)
        entry_widget.bind('<FocusOut>', on_focus_out)

    # Name
    tb.Label(frame1, text="Name:", font=('Tahoma', 10, 'bold'), background="white").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    e2 = tb.Entry(frame1, textvariable=name, width=25)
    e2.grid(row=0, column=1, pady=5)
    set_placeholder(e2, "Enter your name")
    style = tb.Style()

    # Create a new custom style based on Toolbutton
    style.configure("HoverRadio.TRadiobutton", relief="flat", borderwidth=0)

    # Set border only on hover
    style.map("HoverRadio.TRadiobutton",
    relief=[("active", "groove")],
    bordercolor=[("active", "#0d6efd")],
    borderwidth=[("active", 2)],
    highlightcolor=[("active", "#0d6efd")]
)

    # Sex (Radio Buttons)
    tb.Label(frame1, text="Sex:", font=('Tahoma', 10, 'bold'), background="white").grid(row=1, column=0, sticky="ne", padx=5, pady=5)
    sex_frame = tb.Frame(frame1, style="White.TFrame")
    sex_frame.grid(row=1, column=1, sticky="w", pady=5)

    genders = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]
    for text, value in genders:
        tb.Radiobutton(
            sex_frame,
            text=text,
            variable=sex,
            value=value,
            style="HoverRadio.TRadiobutton",
            bootstyle="info"
        ).pack(side="left", padx=5)

    # Zone
    tb.Label(frame1, text="Zone:", font=('Tahoma', 10, 'bold'), background="white").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    e3 = tb.Entry(frame1, textvariable=zone, width=25)
    e3.grid(row=2, column=1, pady=5)
    set_placeholder(e3, "Enter your zone")

    # City
    tb.Label(frame1, text="City:", font=('Tahoma', 10, 'bold'), background="white").grid(row=3, column=0, sticky="e", padx=5, pady=5)
    e4 = tb.Entry(frame1, textvariable=city, width=25)
    e4.grid(row=3, column=1, pady=5)
    set_placeholder(e4, "Enter your city")

    # Password
    tb.Label(frame1, text="Password:", font=('Tahoma', 10, 'bold'), background="white").grid(row=4, column=0, sticky="e", padx=5, pady=5)
    e5 = tb.Entry(frame1, textvariable=password, show='', width=25)
    e5.grid(row=4, column=1, pady=5)
    set_placeholder(e5, "Enter your password", is_password=True)

    # Register Button
    msg_label = tb.Label(main_container, text="", font=('Tahoma', 10, 'bold'), background="#e2e3e5")
    msg_label.pack(pady=5)

    tb.Button(
        frame1,
        text="Register",
        bootstyle=SUCCESS,
        width=20,
        command=lambda: reg_server(root, frame1, name, sex, zone, city, password, msg_label, e2, main_container)
    ).grid(row=5, column=0, columnspan=2, pady=10)

    # Message Label below form (still in main_container)
    msg_label = tb.Label(main_container, text="", font=('Tahoma', 10, 'bold'), background="#e2e3e5")
    msg_label.pack(pady=5)


# Test runner
if __name__ == "__main__":
    root = tb.Window()
    root.title("Register Voter")
    root.geometry("600x500")
    root.configure(bg="#e2e3e5")

    style = tb.Style()
    style.configure("White.TFrame", background="white")
    style.configure("Gray.TFrame", background="#e2e3e5")

    main_container = tb.Frame(root, style="Gray.TFrame")
    main_container.place(relx=0.5, rely=0.5, anchor="center")

    Register(root, main_container)

    root.mainloop()
