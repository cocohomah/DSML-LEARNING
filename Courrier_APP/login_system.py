from tkinter import *
import json
import subprocess
import sys

window = Tk()
window.geometry("900x800")
window.title("NSM_Courriers")
window.config(background="#333333")

# --- Helpers ---
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def new_frame():
    frame = Frame(window, bg="#333333")

    frame.pack(fill=BOTH, expand=True)
    return frame


def login_tab():
    clear_window()
    frame = new_frame()

    Label(frame, text="Login Page", bg="#333333", fg="#FF3399",
          font=("Arial", 30, 'bold')).pack(pady=20)

    email_label = Label(frame, text="Email:", bg="#333333", fg="white", font=("Arial", 16))
    email_label.pack(pady=10)
    email = Entry(frame, font=("Arial", 16))
    email.pack(pady=10)

    password_label = Label(frame, text="Password:", bg="#333333", fg="white", font=("Arial", 16))
    password_label.pack(pady=10)
    password = Entry(frame, show="*", font=("Arial", 16))
    password.pack(pady=10)

    def login_check(user, pwd):
        with open("/home/coder/Documents/DSML-LEARNING/Courrier_APP/user_login_data.json", "r") as f:
            data = json.load(f)

        if user not in data:
            Label(frame, text="*Email not found*", bg="#333333", fg="red").pack(pady=10)
        elif data[user][1] != pwd:
            Label(frame, text="*Incorrect Password*", bg="#333333", fg="red").pack(pady=10)
        else:
            Label(frame, text="*Loading*", bg="#333333", fg="green").pack(pady=10)
            role = data[user][2]
            if role == "admin":
                subprocess.Popen([sys.executable, "DSML-LEARNING/Courrier_APP/admin.py", user])
            elif role == "customer":
                subprocess.Popen([sys.executable, "DSML-LEARNING/Courrier_APP/customer.py", user])
            elif role == "delivery_agent":
                subprocess.Popen([sys.executable, "DSML-LEARNING/Courrier_APP/delivery_agent.py", user])
            window.destroy()

    Button(frame, text="Login", command=lambda: login_check(email.get(), password.get()),
           bg="#FF3399", fg="white", font=("Arial", 16)).pack(pady=20)

    Button(frame, text="Sign Up", bg="#333333", fg="#70939E",
           command=signup_tab).pack(pady=10)
    Button(frame, text="Forgot Password", bg="#333333", fg="#70939E",
           command=forgot_tab).pack(pady=10)


def signup_tab():
    clear_window()
    frame = new_frame()

    Label(frame, text="Sign Up", bg="#333333", fg="#FF3399",
          font=("Arial", 30, 'bold')).pack(pady=20)
    
    name_label = Label(frame, text="Name:", bg="#333333", fg="white")
    name_label.pack(pady=10)
    name = Entry(frame, font=("Arial", 16))
    name.pack(pady=10)

    email_label = Label(frame, text="Email:", bg="#333333", fg="white")
    email_label.pack(pady=10)
    email = Entry(frame, font=("Arial", 16))
    email.pack(pady=10)

    phone_label = Label(frame, text="Phone:", bg="#333333", fg="white")
    phone_label.pack(pady=10)
    phone = Entry(frame, font=("Arial", 16))
    phone.pack(pady=10)

    password_label = Label(frame, text="Password:", bg="#333333", fg="white")
    password_label.pack(pady=10)
    password = Entry(frame, show="*", font=("Arial", 16))
    password.pack(pady=10)

    def signup_action():
        with open("/home/coder/Documents/DSML-LEARNING/Courrier_APP/user_login_data.json", "r") as f:
            data = json.load(f)
        if email.get() in data:
            Label(frame, text="*Email already exists*", bg="#333333", fg="red").pack(pady=10)
        else:
            data[email.get()] = [phone.get(), password.get(), "customer",name.get()]
            with open("/home/coder/Documents/DSML-LEARNING/Courrier_APP/user_login_data.json", "w") as f:
                json.dump(data, f, indent=4)
            Label(frame, text="*Signup Successful*", bg="#333333", fg="green").pack(pady=10)

    Button(frame, text="Submit", command=signup_action,
           bg="#FF3399", fg="white", font=("Arial", 16)).pack(pady=20)
    Button(frame, text="Back", command=login_tab,
           bg="#333333", fg="#70939E").pack(pady=10)


def forgot_tab():
    clear_window()
    frame = new_frame()

    Label(frame, text="Forgot Password", bg="#333333", fg="#FF3399",
          font=("Arial", 30, 'bold')).pack(pady=20)

    email_label = Label(frame, text="Email:", bg="#333333", fg="white")
    email_label.pack(pady=10)
    email = Entry(frame, font=("Arial", 16))
    email.pack(pady=10)

    phone_label = Label(frame, text="Phone:", bg="#333333", fg="white")
    phone_label.pack(pady=10)
    phone = Entry(frame, font=("Arial", 16))
    phone.pack(pady=10)

    new_pwd_label = Label(frame, text="New Password:", bg="#333333", fg="white")
    new_pwd_label.pack(pady=10)
    new_pwd = Entry(frame, show="*", font=("Arial", 16))
    new_pwd.pack(pady=10)

    def reset_password():
        with open("/home/coder/Documents/DSML-LEARNING/Courrier_APP/user_login_data.json", "r") as f:
            data = json.load(f)
        if email.get() not in data:
            Label(frame, text="*Email not found*", bg="#333333", fg="red").pack(pady=10)
        elif data[email.get()][0] != phone.get():
            Label(frame, text="*Phone mismatch*", bg="#333333", fg="red").pack(pady=10)
        else:
            data[email.get()][1] = new_pwd.get()
            with open("/home/coder/Documents/DSML-LEARNING/Courrier_APP/user_login_data.json", "w") as f:
                json.dump(data, f, indent=4)
            Label(frame, text="*Password Updated*", bg="#333333", fg="green").pack(pady=10)

    Button(frame, text="Submit", command=reset_password,
           bg="#FF3399", fg="white", font=("Arial", 16)).pack(pady=20)
    Button(frame, text="Back", command=login_tab,
           bg="#333333", fg="#70939E").pack(pady=10)


# --- Start ---
login_tab()
window.mainloop()
