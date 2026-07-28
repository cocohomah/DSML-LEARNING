from roles import Admin
from tkinter import *
import json
import sys
import pandas as pd

email = sys.argv[1]


DATA_FILE = "/home/coder/Documents/DSML-LEARNING/TEST_PHASE/user_delivery_data.json"

admin = Admin(DATA_FILE)

window = Tk()
window.geometry("800x700")
window.title("NSM_Courriers")
window.config(background="#333333")

def tracking_item_fields(tracking_id):
    with open("/home/coder/Documents/DSML-LEARNING/TEST_PHASE/user_delivery_data.json","r") as f:
        my_dict = json.load(f) 
    
    keys_string = " ".join(str(key) for key in my_dict[tracking_id].keys())
    return keys_string

def new_frame():
    frame = Frame(window, bg='#333333')
    frame.pack(fill=BOTH, expand=True)
    return frame

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def tracking_menu_admin(tracking_id,admin = admin):
    clear_window()
    frame = new_frame()

    label = Label(frame, text="NSM_Courier Admin Panel", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
    label.pack(pady=20)
    def view_tracking_details_admin(tracking_id,admin = admin):
        item = admin.search_tracking_id(tracking_id)
        if item:
            clear_window()
            frame = new_frame()

            label = Label(frame, text="Tracking Details", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
            label.pack(pady=20)

            for key, value in item.items():
                detail_label = Label(frame, text=f"{key}: {value}", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
                detail_label.pack(pady=5)

            
        else:
            label_error = Label(frame, text="Tracking ID not found!", font=("Arial", 12), fg="red", bg="#333333")
            label_error.pack(pady=10)
        
        back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=lambda: tracking_menu_admin(tracking_id))
        back.pack(pady=10)


    button_view = Button(frame,bg="#FF3399", fg="#FFFFFF", text="View Tracking Details", font=("Arial", 12), command=lambda: view_tracking_details_admin(tracking_id))
    button_view.pack(pady=10)
    
    def item_update_admin(tracking_id,admin = admin):
        clear_window()
        frame = new_frame()

        label = Label(frame, text="Update Tracking Info", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
        label.pack(pady=20)

        field_name = Label(frame,text = "Fields: " + tracking_item_fields(tracking_id), font=("Arial",9,"italic"), fg ="#FFFFFF", bg="#333333")
        field_name.pack()

        label_field = Label(frame, text="Field to Update:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
        label_field.pack(pady=10)
        entry_field = Entry(frame, font=("Arial", 12))
        entry_field.pack(pady=5)

        label_value = Label(frame, text="New Value:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
        label_value.pack(pady=10)
        entry_value = Entry(frame, font=("Arial", 12))
        entry_value.pack(pady=5)
        
        def update_now(field,value, tracking_id,admin = admin ):

            if field and value:
                admin.update_tracking_info(tracking_id, field, value)
                label_success = Label(frame, text="Tracking info updated successfully!", font=("Arial", 12),  fg="green", bg="#333333")
                label_success.pack(pady=10)
            else:
                label_error = Label(frame, text="Please fill in both fields.", font=("Arial", 12),  fg="red", bg="#333333")
                label_error.pack(pady=10)

        button_submit = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Submit", font=("Arial", 12), command= lambda: update_now(entry_field.get(), entry_value.get(), tracking_id))
        button_submit.pack(pady=10)

        back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=lambda: tracking_menu_admin(tracking_id))
        back.pack(pady=10)


    button_update = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Update item Info", font=("Arial", 12), command=lambda:item_update_admin(tracking_id))
    button_update.pack(pady=10)

    def add_extra_admin(tracking_id,admin = admin):
        clear_window()
        frame = new_frame()

        label = Label(frame, text="Add Extra Details", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
        label.pack(pady=20)



        label_value = Label(frame, text="Value:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
        label_value.pack(pady=10)
        entry_value = Entry(frame, font=("Arial", 12))
        entry_value.pack(pady=5)

        def add_now(value, tracking_id,admin = admin):
            admin.add_extra_details(tracking_id, value)
            label_success = Label(frame, text="Extra details added successfully!", font=("Arial", 12),  fg="green", bg="#333333")
            label_success.pack(pady=10)

        button_submit = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Submit", font=("Arial", 12), command=lambda: add_now( entry_value.get(), tracking_id))
        button_submit.pack(pady=10)

        back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=lambda: tracking_menu_admin(tracking_id))
        back.pack(pady=10)


    button_add = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Add Extra Details", font=("Arial", 12), command=lambda: add_extra_admin(tracking_id))
    button_add.pack(pady=10)

    def delete_field_admin(tracking_id,admin = admin):
        clear_window()
        frame = new_frame()

        

        label = Label(frame, text="Update Tracking Info", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
        label.pack(pady=20)

        field_name = Label(frame,text = "Fields: " + tracking_item_fields(tracking_id), font=("Arial",9,"italic"), fg ="#FFFFFF", bg="#333333")
        field_name.pack()

        label_field = Label(frame, text="Field to Update:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
        label_field.pack(pady=10)
        entry_field = Entry(frame, font=("Arial", 12))
        entry_field.pack(pady=5)

        
        def delete_now(value, tracking_id,admin = admin):
            admin.delete_item_key(tracking_id,value)
            label_success = Label(frame, text="Field deleted successfully!", font=("Arial", 12),  fg="green", bg="#333333")
            label_success.pack(pady=10)

        button_submit = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Submit", font=("Arial", 12), command=lambda: delete_now( entry_field.get(), tracking_id))
        button_submit.pack(pady=10)

        back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=lambda: tracking_menu_admin(tracking_id))
        back.pack(pady=10)

    button_delete = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Delete item's data field", font=("Arial", 12), command=lambda: delete_field_admin(tracking_id))
    button_delete.pack(pady=10)

    def delete_item_admin(tracking_id,admin = admin):
        admin.delete_item(tracking_id)
        label_success = Label(frame, text="Item deleted successfully!", font=("Arial", 12), fg="green", bg="#333333")
        label_success.pack(pady=10)




    button_delete = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Delete item", font=("Arial", 12), command=lambda: delete_item_admin(tracking_id))
    button_delete.pack(pady=10)

    back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=tracking_id_search)
    back.pack(pady=10)

def tracking_id_search(admin = admin):
    clear_window()
    frame = new_frame()

    label = Label(frame, text="NSM_Courier Admin Panel", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
    label.pack(pady=20)

    label_search = Label(frame, text="Search Item by Tracking ID:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
    label_search.pack(pady=10)
    entry_search = Entry(frame, font=("Arial", 12))
    entry_search.pack(pady=5)
    def search_now(tracking_id,admin = admin):
        item = admin.search_tracking_id(tracking_id)
        if item:
            label_success = Label(frame, text="Item found!", font=("Arial", 12), fg="green", bg="#333333")
            label_success.pack(pady=10)
            tracking_menu_admin(tracking_id)
        else:
            label_error = Label(frame, text="Item not found!", font=("Arial", 12), fg="red", bg="#333333")
            label_error.pack(pady=10)
    button_search = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Search", font=("Arial", 12), command=lambda: search_now(entry_search.get()))
    button_search.pack(pady=10)

    back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=main_admin_menu)
    back.pack(pady=10)

def change_password_admin(email,admin = admin):
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
            admin.change_password(email, new_password)
            label_success = Label(frame, text="Password updated successfully!", font=("Arial", 12), fg="green", bg="#333333")
            label_success.pack(pady=10)
        else:
            label_error = Label(frame, text="Please enter a new password.", font=("Arial", 12), fg="red", bg="#333333")
            label_error.pack(pady=10)

    button_submit = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Submit", font=("Arial", 12), command=lambda: update_password(entry_new_password.get(), email))
    button_submit.pack(pady=10)

    back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=main_admin_menu)
    back.pack(pady=10)

def backup(DATAFILE):
    rows = []
    with open(DATAFILE,'r')as f:
      data = json.load(f)
    for customer_id, details in data.items():
        row = {"customer_id": customer_id}
        row.update(details)
        rows.append(row)


    df = pd.DataFrame(rows)


    df.to_csv("customers.csv", index=False)

def add_employee():
    clear_window()
    frame = new_frame()

    Label(frame, text="Add Employee", bg="#333333", fg="#FF3399",
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

    def add_agent():
        with open("/home/coder/Documents/DSML-LEARNING/TEST_PHASE/user_login_data.json", "r") as f:
            data = json.load(f)
        if email.get() in data:
            Label(frame, text="*Email already exists*", bg="#333333", fg="red").pack(pady=10)
        else:
            data[email.get()] = [phone.get(), password.get(), "delivery_agent",name.get()]
            with open("/home/coder/Documents/DSML-LEARNING/TEST_PHASE/user_login_data.json", "w") as f:
                json.dump(data, f, indent=4)
            Label(frame, text="*Agent Added*", bg="#333333", fg="green").pack(pady=10)

    Button(frame, text="ADD", command=add_agent,
           bg="#FF3399", fg="white", font=("Arial", 16)).pack(pady=20)


def main_admin_menu(DATAFILE):
    clear_window()
    frame = new_frame()

    label = Label(frame, text="NSM_Courier Admin Panel", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
    label.pack(pady=20)


    button_search = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Search item", font=("Arial", 12), command=tracking_id_search)
    button_search.pack(pady=10)

    button_backup = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Backup Customer Details", font=("Arial", 12), command=lambda: backup(DATAFILE))
    button_backup.pack(pady=10)

    button_add_employee = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Add New Delivery Agent", font=("Arial", 12), command=add_employee)
    button_add_employee.pack(pady=10)

    button_change_password = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Change Password", font=("Arial", 12), command=lambda: change_password_admin(email))
    button_change_password.pack(pady=10)

    button_logout = Button(frame, bg="#FF3399", fg="#FFFFFF", text="Logout", font=("Arial",12), command=lambda: admin.logout(window))
    button_logout.pack(pady=10)

    button_exit = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Exit", font=("Arial", 12), command=window.destroy)
    button_exit.pack(pady=10)

    

main_admin_menu(DATA_FILE)

window.mainloop()


