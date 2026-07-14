from  tkinter import * 
import json

window = Tk()
window.geometry("500x500")
window.title("Courier Management System ")
window.config(background = "#0B5D70" )

def login_check():
    with open("data.json", "r") as f:
        login_data = json.load(f)


    user = username.get()
    pwd = password.get()
    
    if user not in login_data:
        Label(window, text="*Email not found*", pady=20,
              bg="#0B5D70", fg="red").pack()
    elif login_data[user] != pwd:
        Label(window, text="*Incorrect Password*", pady=20,
              bg="#0B5D70", fg="red").pack()
    else:
        Label(window, text="*Entered*", pady=20,
              bg="#0B5D70", fg="green").pack()

    
frame = Frame(bg='#333333')


login_title = Label(frame,text="Login Page",bg='#333333', fg="#FF3399", font=("Arial", 30,'bold'))




username_label = Label(frame, text = "Username",bg='#333333', fg="#FFFFFF", font=("Arial", 16))


username = Entry(frame, font=("Arial", 16))

password_label = Label(frame, text = "Password",bg='#333333', fg="#FFFFFF", font=("Arial", 16))

password = Entry(frame, show="*", font=("Arial", 16))




login_button = Button(frame, text = "Login", command = login_check,bg="#FF3399", fg="#FFFFFF", font=("Arial", 16))



login_title.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()


window.mainloop()
