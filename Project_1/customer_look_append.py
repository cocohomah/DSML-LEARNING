

from tkinter import *
import json
import random

counter = random.randint(0, 100000000)

with open('/home/coder/Documents/DSML-LEARNING/Project_1/user_delivery_data.json',"r") as f:
    data = json.load(f)


def get_customer_id():
    window = Tk()
    window.geometry("500x700")
    window.title("NSM_Courriers")
    window.config(background="#333333")

    ask = Label(window, text="Enter Customer ID", bg='#333333', fg="#FF3399", font=("Arial", 20, 'bold'))
    ask.pack(pady=20)

    id_label = Label(window, text="Customer ID:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    id_label.pack(pady=10)
    id_entry = Entry(window, font=("Arial", 16))
    id_entry.pack(pady=10)

    # variable to store the result
    result = {"id": None}

    def submit_id():
        entered_id = id_entry.get()
        # convert to int if your JSON keys are integers
        if entered_id in data:
            result["id"] = entered_id
            window.destroy()
        else:
            Label(window, text="Invalid ID! Please enter a valid ID.", bg='#333333', fg="#FF0000", font=("Arial", 16)).pack(pady=10)

    submit_button = Button(window, text="Submit", command=submit_id, bg="#FF3399", fg="#FFFFFF", font=("Arial", 16))
    submit_button.pack(pady=20)

    window.mainloop()
    return result["id"]


customer_id = get_customer_id()

class Existing_Customer:
    def __init__(self, data, id):
        if id not in data:
            raise ValueError(f"Customer ID {id} not found in data")
        self.id = id


    def display_details(self):
        window = Tk()
        window.geometry("500x700")
        window.title("NSM_Courriers")
        window.config(background="#333333")

        title = Label(window, text="NSM_Courriers", bg='#333333', fg="#FF3399", font=("Arial", 30, 'bold'))
        title.pack(pady=20)

        details = json.dumps(data[self.id], indent=4)
        details_label = Label(window, text=details, bg='#333333', fg="#FFFFFF", font=("Arial", 16), justify=LEFT)
        details_label.pack(pady=20)

        exit_button = Button(window, text="Exit", command=window.destroy, bg="#FF3399", fg="#FFFFFF", font=("Arial", 16))
        exit_button.pack(pady=10)

        window.mainloop()

    def add_extra_details(self):
        window = Tk()
        window.geometry("500x700")
        window.title("NSM_Courriers")
        window.config(background="#333333")

        ask = Label(window, text="Enter extra data", bg='#333333', fg="#FF3399", font=("Arial", 20, 'bold'))
        ask.pack(pady=20)

        extra_data_label = Label(window, text="Extra Data:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        extra_data_label.pack(pady=10)
        extra_data_entry = Entry(window, font=("Arial", 16))
        extra_data_entry.pack(pady=10)

        def save_data():
            global counter
            data[self.id]['extra_'+str(counter)] = extra_data_entry.get()
            counter += 1
            with open('/home/coder/Documents/DSML-LEARNING/Project_1/user_delivery_data.json', 'w') as f:
                json.dump(data, f, indent=4)
            Label(window, text="Data saved successfully!", bg='#333333', fg="#00FF00", font=("Arial", 16)).pack(pady=10)


        submit_button = Button(window, text="Submit", command=save_data, bg="#FF3399", fg="#FFFFFF", font=("Arial", 16))
        submit_button.pack(pady=20)
        exit_button = Button(window, text="Exit", command=window.destroy, bg="#FF3399", fg="#FFFFFF", font=("Arial", 16))
        exit_button.pack(pady=10)
        window.mainloop()

    def update_info(self):
        window = Tk()
        window.geometry("700x700")
        window.title("NSM_Courriers")
        window.config(background="#333333")

        ask = Label(window, text="What do you want to update?", bg='#333333', fg="#FF3399", font=("Arial", 20, 'bold'))
        ask.pack(pady=20)

        key_label = Label(window, text="Key:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        key_label.pack(pady=10)
        key_entry = Entry(window, font=("Arial", 16))
        key_entry.pack(pady=10)

        ask = Label(window, text="What value do you want to enter?", bg='#333333', fg="#FF3399", font=("Arial", 20, 'bold'))
        ask.pack(pady=20)

        value_label = Label(window, text="Value:", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        value_label.pack(pady=10)
        value_entry = Entry(window, font=("Arial", 16))
        value_entry.pack(pady=10)

        def save_info():
            if key_entry.get() not in data[self.id]:
                Label(window, text="Invalid key! Please enter a valid key.", bg='#333333', fg="#FF0000", font=("Arial", 16)).pack(pady=10)
                return
            data[self.id][key_entry.get()] = value_entry.get()
            with open('/home/coder/Documents/DSML-LEARNING/Project_1/user_delivery_data.json', 'w') as f:
                json.dump(data, f, indent=4)
            Label(window, text="Info updated successfully!", bg='#333333', fg="#00FF00", font=("Arial", 16)).pack(pady=10)


        submit_button = Button(window, text="Submit", command=save_info, bg="#FF3399", fg="#FFFFFF", font=("Arial", 16))
        submit_button.pack(pady=20)
        exit_button = Button(window, text="Exit", command=window.destroy, bg="#FF3399", fg="#FFFFFF", font=("Arial", 16))
        exit_button.pack(pady=10)
        window.mainloop()

def refresh_data():
    c1 = Existing_Customer(data, customer_id)
    customer_menu(c1)

# Only create customer if ID is valid
if customer_id is not None:
    c1 = Existing_Customer(data, customer_id)

    def customer_menu(c1=c1):
        window = Tk()
        window.geometry("500x700")
        window.title("NSM_Courriers")
        window.config(background="#333333")

        ask = Label(window, text="What do you want to do?", bg='#333333', fg="#FF3399", font=("Arial", 20, 'bold'))
        ask.pack(pady=20)

        display_button = Button(window, text="Display Details", command=lambda: c1.display_details(), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16))
        display_button.pack(pady=10)

        add_button = Button(window, text="Add Extra Details", command=lambda: c1.add_extra_details(), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16))
        add_button.pack(pady=10)

        update_button = Button(window, text="Update Info", command=lambda: c1.update_info(), bg="#FF3399", fg="#FFFFFF", font=("Arial", 16))
        update_button.pack(pady=10)

        refresh_button = Button(window, text="Refresh", command=refresh_data, bg="#FF3399", fg="#FFFFFF", font=("Arial", 16))
        refresh_button.pack(pady=10)

        exit_button = Button(window, text="Exit", command=window.destroy, bg="#FF3399", fg="#FFFFFF", font=("Arial", 16))
        exit_button.pack(pady=10)
        window.mainloop()

    customer_menu()
