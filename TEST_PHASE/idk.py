


from roles import customer
from tkinter import *
import sys
import json

email = sys.argv[1]

DATA_FILE = "/home/coder/Documents/DSML-LEARNING/TEST_PHASE/user_delivery_data.json"

customer = customer(DATA_FILE)

window = Tk()
window.geometry("800x700")
window.title("NSM_Courriers")
window.config(background="#333333")

def new_frame():
    frame = Frame(window, bg='#333333')
    frame.pack(fill=BOTH, expand=True)
    return frame

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def tracking_menu_customer(tracking_id,customer = customer):
        clear_window()
        frame = new_frame()        
        def view_details(tracking_id, customer = customer):
            item = customer.search_tracking_id(tracking_id)
            if item:
                clear_window()
                frame = new_frame()

                label = Label(frame, text="Tracking Details", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
                label.pack(pady=20)

                for key, value in item.items():
                    if key == "Delivery_agent_email":
                        continue

                    if key == "request_by_delivery_agent":
                        continue
                    detail_label = Label(frame, text=f"{key}: {value}", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
                    detail_label.pack(pady=5)
            else:
                label_error = Label(frame, text="Tracking ID not found!", font=("Arial", 12), fg="red", bg="#333333")
                label_error.pack(pady=10)
            
            back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=lambda : tracking_menu_customer(tracking_id))
            back.pack(pady=10)

        def check_otp(tracking_id):
                clear_window()
                frame = new_frame()
                
                with open(DATA_FILE,"r") as f:
                    data = json.load(f)
                otp = data[tracking_id]["request_by_delivery_agent"]
                for key,value in otp.items():
                    detail_label = Label(frame, text=f"{key}: {value}", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
                    detail_label.pack(pady=5)
                
        button_view_details = Button(frame,bg="#FF3399", fg="#FFFFFF", text="View Details", font=("Arial", 12), command=lambda: view_details(tracking_id))
        button_view_details.pack(pady=10)

        button_view_details = Button(frame,bg="#FF3399", fg="#FFFFFF", text="View OTP", font=("Arial", 12), command=lambda: check_otp(tracking_id))
        button_view_details.pack(pady=10)

        back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=item_search)
        back.pack(pady=10)

def item_search(customer = customer ):
    clear_window()
    frame = new_frame()

    label = Label(frame, text="NSM_Courier delivery_agent Panel", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
    label.pack(pady=20)

    label_search = Label(frame, text="Search Item by Tracking ID:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
    label_search.pack(pady=10)
    entry_search = Entry(frame, font=("Arial", 12))
    entry_search.pack(pady=5)
    def search_now(tracking_id,customer  = customer ):
        item = customer.search_tracking_id(tracking_id)
        if item:
            label_success = Label(frame, text="Tracking ID found!", font=("Arial", 12), fg="green", bg="#333333")
            label_success.pack(pady=10)
            tracking_menu_customer(tracking_id)
        else:
            label_error = Label(frame, text="Tracking ID not found!", font=("Arial", 12), fg="red", bg="#333333")
            label_error.pack(pady=10)
    button_search = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Search", font=("Arial", 12), command=lambda: search_now(entry_search.get()))
    button_search.pack(pady=10)

    back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=customer_main_menu)
    back.pack(pady=10)


def change_password_customer(email,customer = customer):
    clear_window()
    frame = new_frame()

    label = Label(frame, text="Change Password", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
    label.pack(pady=20)

    label_new_password = Label(frame, text="New Password:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
    label_new_password.pack(pady=10)
    entry_new_password = Entry(frame, show="*", font=("Arial", 12))
    entry_new_password.pack(pady=5)

    def update_password(new_password,email):
        if new_password:
            customer.change_password(email, new_password)
            label_success = Label(frame, text="Password updated successfully!", font=("Arial", 12), fg="green", bg="#333333")
            label_success.pack(pady=10)
        else:
            label_error = Label(frame, text="Please enter a new password.", font=("Arial", 12), fg="red", bg="#333333")
            label_error.pack(pady=10)

    button_submit = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Submit", font=("Arial", 12), command=lambda: update_password(entry_new_password.get(), email))
    button_submit.pack(pady=10)

    back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=customer_main_menu)
    back.pack(pady=10)

def add_new_item(email,customer = customer):
    clear_window()
    frame = new_frame()
    item_name_label = Label(frame, text="Item Name:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
    item_name_label.pack(pady=10)
    entry_item_name = Entry(frame, font=("Arial", 12))
    entry_item_name.pack(pady=5)

    weight_label = Label(frame, text="Weight:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
    weight_label.pack(pady=10)
    entry_weight = Entry(frame, font=("Arial", 12))
    entry_weight.pack(pady=5)


    handling_label = Label(frame, text="Handling Cautions:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
    handling_label.pack(pady=10)
    entry_handling = Entry(frame, font=("Arial", 12))
    entry_handling.pack(pady=5)



    delivery_address_label = Label(frame, text="Delivery Address:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
    delivery_address_label.pack(pady=10)
    entry_delivery_address = Entry(frame, font=("Arial", 12))
    entry_delivery_address.pack(pady=5)



    sending_address_label = Label(frame, text="Sending Address:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
    sending_address_label.pack(pady=10)
    entry_sending_address = Entry(frame, font=("Arial", 12))
    entry_sending_address.pack(pady=5)




    time_label = Label(frame, text="Time of Delivery:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
    time_label.pack(pady=10)
    entry_time = Entry(frame, font=("Arial", 12))
    entry_time.pack(pady=5)

    time_label = Label(frame, text="Time of Delivery:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
    time_label.pack(pady=10)
    entry_time = Entry(frame, font=("Arial", 12))
    entry_time.pack(pady=5)

    time_label = Label(frame, text="Time of Delivery:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
    time_label.pack(pady=10)
    entry_time = Entry(frame, font=("Arial", 12))
    entry_time.pack(pady=5)


    time_label = Label(frame, text="Time of Delivery:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
    time_label.pack(pady=10)
    entry_time = Entry(frame, font=("Arial", 12))
    entry_time.pack(pady=5)


def customer_main_menu():
    clear_window()
    frame = new_frame()

    label = Label(frame, text="NSM_Courier Customer Panel", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
    label.pack(pady=20)


    button_search = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Search Item", font=("Arial", 12), command=item_search)
    button_search.pack(pady=10)

    button_add = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Add New Item", font=("Arial", 12), command=item_search)
    button_add.pack(pady=10)

    button_change_password = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Change Password", font=("Arial", 12), command=lambda: change_password_customer(email))
    button_change_password.pack(pady=10)

    button_logout = Button(frame, bg="#FF3399", fg="#FFFFFF", text="Logout", font=("Arial",12), command=lambda: customer.logout(window))
    button_logout.pack(pady=10)

    button_exit = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Exit", font=("Arial", 12), command=window.destroy)
    button_exit.pack(pady=10)


customer_main_menu()
window.mainloop()