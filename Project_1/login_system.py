from  tkinter import * 
import json


window = Tk()
window.geometry("800x700")
window.title("Courier Management System ")
window.config(background = "#333333" )


def switch_frame(new_frame):
    for widget in window.winfo_children():
        widget.destroy()
    new_frame()






def login_tab():
    frame = Frame(bg='#333333')


    login_title = Label(frame,text="Login Page",bg='#333333', fg="#FF3399", font=("Arial", 30,'bold'))




    username_label = Label(frame, text = "Email :       ",bg='#333333', fg="#FFFFFF", font=("Arial", 16))


    username = Entry(frame, font=("Arial", 16))

    password_label = Label(frame, text = "Password : ",bg='#333333', fg="#FFFFFF", font=("Arial", 16))

    password = Entry(frame, show="*", font=("Arial", 16))


    forgot_password = Button(frame, text = "forgot_password",bg='#333333', fg="#70939E", font=("Arial", 10),activeforeground = "#70939E", activebackground = "#333333",command=lambda: switch_frame(forgot_tab))
    sign_up = Button(frame, text = "sign_up",bg='#333333', fg="#70939E", font=("Arial", 10),relief="flat",activeforeground = "#70939E", activebackground = "#333333",command=lambda: switch_frame(signup_tab))




    def login_check():
        with open("/home/coder/Documents/DSML-LEARNING/Project_1/user_login_data.json", "r") as f:
            data = json.load(f)


        user = username.get()
        pwd = password.get()
        
        if user not in data:
            Label(frame, text="*Email not found*", pady=20, 
                bg="#333333", fg="red").grid(row=6, column=0, columnspan=2)

        elif data[user][1] != pwd:
            Label(frame, text="*Incorrect Password*", pady=20,
                bg="#333333", fg="red").grid(row=7, column=0, columnspan=2)

        else:
            Label(frame, text="*Loading*", pady=20,
                bg="#333333", fg="green").grid(row=5, column=0, columnspan=2)


    login_button = Button(frame, text = "Login", command = login_check,bg="#FF3399", fg="#FFFFFF", font=("Arial", 16))



    login_title.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password.grid(row=2, column=1, pady=20)
    login_button.grid(row=4, column=0, columnspan=2, pady=30)
    sign_up.grid(row=3, column = 0,columnspan=1,pady=20)
    forgot_password.grid(row=3, columnspan=2, column = 1, pady=20)

    frame.pack()

def signup_tab():
    frame1 = Frame(bg="#333333")

    signup_title = Label(frame1, text="Sign Up", bg="#333333", fg="#FF3399",
                         font=("Arial", 30, 'bold'))

    username_label = Label(frame1, text="Email:", bg="#333333", fg="white")
    username = Entry(frame1, font=("Arial", 16))

    phone_label = Label(frame1, text="Phone:", bg="#333333", fg="white")
    phone = Entry(frame1, font=("Arial", 16))

    password_label = Label(frame1, text="Password:", bg="#333333", fg="white")
    password = Entry(frame1, show="*", font=("Arial", 16))

    def signup_action():
        with open("/home/coder/Documents/DSML-LEARNING/Project_1/user_login_data.json", "r") as f:
            data = json.load(f)

        if username.get() in data:
            Label(frame1, text="*Email already exists*", bg="#333333", fg="red").grid(row=6, column=0, columnspan=2)
        else:
            data[username.get()] = [phone.get(), password.get()]
            with open("/home/coder/Documents/DSML-LEARNING/Project_1/user_login_data.json", "w") as f:
                json.dump(data, f, indent=4)
            Label(frame1, text="*Signup Successful*", bg="#333333", fg="green").grid(row=7, column=0, columnspan=2)

    signup_button = Button(frame1, text="Submit", command=signup_action,
                           bg="#FF3399", fg="white", font=("Arial", 16))
    back = Button(frame1, text="Back", command=lambda: switch_frame(login_tab),
                  bg="#333333", fg="#70939E")

    # Use grid consistently
    signup_title.grid(row=0, column=0, columnspan=2, pady=20)
    username_label.grid(row=1, column=0)
    username.grid(row=1, column=1, pady=10)
    phone_label.grid(row=2, column=0)
    phone.grid(row=2, column=1, pady=10)
    password_label.grid(row=3, column=0)
    password.grid(row=3, column=1, pady=10)
    signup_button.grid(row=4, column=0, columnspan=2, pady=20)
    back.grid(row=5, column=0, columnspan=2, pady=10)

    frame1.pack(fill="both", expand=True)





def forgot_tab():
    frame2 = Frame(bg="#333333")

    forgot_password_title = Label(frame2, text="Forgot Password", bg="#333333", fg="#FF3399",
                                    font=("Arial", 30, 'bold'))

    username_label = Label(frame2, text="Email:", bg="#333333", fg="white")
    username = Entry(frame2, font=("Arial", 16))

    phone_label = Label(frame2, text="Phone:", bg="#333333", fg="white")
    phone = Entry(frame2, font=("Arial", 16))

    new_pwd_label = Label(frame2, text="New Password:", bg="#333333", fg="white")
    new_pwd = Entry(frame2, show="*", font=("Arial", 16))

    def reset_password():
        with open("/home/coder/Documents/DSML-LEARNING/Project_1/user_login_data.json", "r") as f:
         data = json.load(f)
        if username.get() not in data:
            Label(frame2, text="*Email not found*", bg="#333333", fg="red").grid(row=6, column=0, columnspan=2)
        elif data[username.get()][0] != phone.get():
            Label(frame2, text="*Phone number mismatch*", bg="#333333", fg="red").grid(row=7, column=0, columnspan=2)
        else:
            data[username.get()][1] = new_pwd.get()
            with open("/home/coder/Documents/DSML-LEARNING/Project_1/user_login_data.json", "w") as f:
                json.dump(data, f, indent=4)
            Label(frame2, text="*Password Updated*", bg="#333333", fg="green").grid(row=9, column=0, columnspan=2)

    submit_button = Button(frame2, text="Submit", command=reset_password,
                            bg="#FF3399", fg="white", font=("Arial", 16))
    back = Button(frame2, text="Back", command=lambda: switch_frame(login_tab),
                    bg="#333333", fg="#70939E")

    # Use grid consistently
    forgot_password_title.grid(row=0, column=0, columnspan=2, pady=20)
    username_label.grid(row=1, column=0)
    username.grid(row=1, column=1, pady=10)
    phone_label.grid(row=2, column=0)
    phone.grid(row=2, column=1, pady=10)
    new_pwd_label.grid(row=3, column=0)
    new_pwd.grid(row=3, column=1, pady=10)
    submit_button.grid(row=4, column=0, columnspan=2, pady=20)
    back.grid(row=5, column=0, columnspan=2, pady=10)

    frame2.pack(fill="both", expand=True)



login_tab()
window.mainloop()
