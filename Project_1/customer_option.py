from tkinter import *
import json
import random

DATA_FILE = '/home/coder/Documents/DSML-LEARNING/Project_1/user_delivery_data.json'
counter = random.randint(0, 100000000)

# ---- Load data ----
try:
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data = {}

# ---- Window setup ----
window = Tk()
window.geometry("800x700")
window.title("NSM_Courriers")
window.config(background="#333333")

app_state = {"customer_id": None}


def clear_window():
    for widget in window.winfo_children():
        widget.destroy()


def save_data():
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)


def new_frame():
    frame = Frame(window, bg='#333333')
    frame.pack(fill=BOTH, expand=True)
    return frame


# ---------------- Screens ----------------

def show_id_screen():
    clear_window()
    frame = new_frame()

    Label(frame, text="Enter Customer ID", bg='#333333', fg="#FF3399",
          font=("Arial", 20, 'bold')).pack(pady=20)

    Label(frame, text="Customer ID:", bg='#333333', fg="#FFFFFF",
          font=("Arial", 16)).pack(pady=10)
    id_entry = Entry(frame, font=("Arial", 16))
    id_entry.pack(pady=10)
    id_entry.focus()

    error_label = Label(frame, text="", bg='#333333', fg="#FF0000", font=("Arial", 14))
    error_label.pack(pady=5)

    def submit_id(event=None):
        entered_id = id_entry.get().strip()
        if entered_id in data:
            app_state["customer_id"] = entered_id
            show_customer_menu()
        else:
            error_label.config(text="Invalid ID! Please enter a valid ID.")

    id_entry.bind("<Return>", submit_id)

    Button(frame, text="Submit", command=submit_id, bg="#FF3399", fg="#FFFFFF",
           font=("Arial", 16)).pack(pady=20)


def show_customer_menu():
    clear_window()
    frame = new_frame()

    Label(frame, text="What do you want to do?", bg='#333333', fg="#FF3399",
          font=("Arial", 20, 'bold')).pack(pady=20)

    Button(frame, text="Display Details", command=show_display_details,
           bg="#FF3399", fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)

    Button(frame, text="Add Extra Details", command=show_add_extra_details,
           bg="#FF3399", fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)

    Button(frame, text="Update Info", command=show_update_info,
           bg="#FF3399", fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)

    Button(frame, text="Log Out", command=logout,
           bg="#FF3399", fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)

    Button(frame, text="Exit", command=window.destroy,
           bg="#FF3399", fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)


def logout():
    app_state["customer_id"] = None
    show_id_screen()


def show_display_details():
    clear_window()
    frame = new_frame()
    customer_id = app_state["customer_id"]

    Label(frame, text="NSM_Courriers", bg='#333333', fg="#FF3399",
          font=("Arial", 30, 'bold')).pack(pady=20)

    details = json.dumps(data[customer_id], indent=4)
    Label(frame, text=details, bg='#333333', fg="#FFFFFF",
          font=("Arial", 14), justify=LEFT).pack(pady=20)

    Button(frame, text="Back", command=show_customer_menu,
           bg="#FF3399", fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)


def show_add_extra_details():
    clear_window()
    frame = new_frame()
    customer_id = app_state["customer_id"]

    Label(frame, text="Enter extra data", bg='#333333', fg="#FF3399",
          font=("Arial", 20, 'bold')).pack(pady=20)

    Label(frame, text="Extra Data:", bg='#333333', fg="#FFFFFF",
          font=("Arial", 16)).pack(pady=10)
    extra_entry = Entry(frame, font=("Arial", 16))
    extra_entry.pack(pady=10)

    status_label = Label(frame, text="", bg='#333333', font=("Arial", 16))
    status_label.pack(pady=10)

    def save_extra():
        global counter
        value = extra_entry.get().strip()
        if not value:
            status_label.config(text="Please enter some data.", fg="#FF0000")
            return
        data[customer_id]['extra_' + str(counter)] = value
        counter += 1
        save_data()
        status_label.config(text="Data saved successfully!", fg="#00FF00")
        extra_entry.delete(0, END)

    Button(frame, text="Submit", command=save_extra, bg="#FF3399", fg="#FFFFFF",
           font=("Arial", 16)).pack(pady=20)
    Button(frame, text="Back", command=show_customer_menu, bg="#FF3399", fg="#FFFFFF",
           font=("Arial", 16)).pack(pady=10)


def show_update_info():
    clear_window()
    frame = new_frame()
    customer_id = app_state["customer_id"]

    Label(frame, text="What do you want to update?", bg='#333333', fg="#FF3399",
          font=("Arial", 18, 'bold')).pack(pady=15)

    keys_text = "Available keys: " + ", ".join(data[customer_id].keys())
    Label(frame, text=keys_text, bg='#333333', fg="#AAAAAA",
          font=("Arial", 12), wraplength=700, justify=LEFT).pack(pady=5)

    Label(frame, text="Key:", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)
    key_entry = Entry(frame, font=("Arial", 16))
    key_entry.pack(pady=10)

    Label(frame, text="New Value:", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).pack(pady=10)
    value_entry = Entry(frame, font=("Arial", 16))
    value_entry.pack(pady=10)

    status_label = Label(frame, text="", bg='#333333', font=("Arial", 16))
    status_label.pack(pady=10)

    def save_info():
        key = key_entry.get().strip()
        if key not in data[customer_id]:
            status_label.config(text="Invalid key! Please enter a valid key.", fg="#FF0000")
            return
        data[customer_id][key] = value_entry.get()
        save_data()
        status_label.config(text="Info updated successfully!", fg="#00FF00")

    Button(frame, text="Submit", command=save_info, bg="#FF3399", fg="#FFFFFF",
           font=("Arial", 16)).pack(pady=20)
    Button(frame, text="Back", command=show_customer_menu, bg="#FF3399", fg="#FFFFFF",
           font=("Arial", 16)).pack(pady=10)


# ---- Start app ----
show_id_screen()
window.mainloop()