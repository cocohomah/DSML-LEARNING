from roles import Admin
from tkinter import *
import json
import sys

email = sys.argv[1]


DATA_FILE = "/home/coder/Documents/DSML-LEARNING/TEST_PHASE/user_delivery_data.json"

admin = Admin(DATA_FILE)

window = Tk()
window.geometry("800x700")
window.title("NSM_Courriers")
window.config(background="#333333")

def customerfields(customer_id):
    with open("/home/coder/Documents/DSML-LEARNING/TEST_PHASE/user_delivery_data.json","r") as f:
        my_dict = json.load(f) 
    
    keys_string = " ".join(str(key) for key in my_dict[customer_id].keys())
    return keys_string

def new_frame():
    frame = Frame(window, bg='#333333')
    frame.pack(fill=BOTH, expand=True)
    return frame

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def old_customer_menu_admin(customer_id,admin = admin):
    clear_window()
    frame = new_frame()

    label = Label(frame, text="NSM_Courier Admin Panel", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
    label.pack(pady=20)
    def view_customer_details_admin(customer_id,admin = admin):
        customer = admin.search_customer(customer_id)
        if customer:
            clear_window()
            frame = new_frame()

            label = Label(frame, text="Customer Details", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
            label.pack(pady=20)

            for key, value in customer.items():
                detail_label = Label(frame, text=f"{key}: {value}", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
                detail_label.pack(pady=5)

            
        else:
            label_error = Label(frame, text="Customer not found!", font=("Arial", 12), fg="red", bg="#333333")
            label_error.pack(pady=10)
        
        back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=lambda: old_customer_menu_admin(customer_id))
        back.pack(pady=10)


    button_view = Button(frame,bg="#FF3399", fg="#FFFFFF", text="View Customer Details", font=("Arial", 12), command=lambda: view_customer_details_admin(customer_id))
    button_view.pack(pady=10)
    
    def customer_update_admin(customer_id,admin = admin):
        clear_window()
        frame = new_frame()

        label = Label(frame, text="Update Customer Info", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
        label.pack(pady=20)

        field_name = Label(frame,text = "Fields: " + customerfields(customer_id), font=("Arial",9,"italic"), fg ="#FFFFFF", bg="#333333")
        field_name.pack()

        label_field = Label(frame, text="Field to Update:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
        label_field.pack(pady=10)
        entry_field = Entry(frame, font=("Arial", 12))
        entry_field.pack(pady=5)

        label_value = Label(frame, text="New Value:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
        label_value.pack(pady=10)
        entry_value = Entry(frame, font=("Arial", 12))
        entry_value.pack(pady=5)
        
        def update_now(field,value, customer_id,admin = admin ):

            if field and value:
                admin.update_customer_info(customer_id, field, value)
                label_success = Label(frame, text="Customer info updated successfully!", font=("Arial", 12),  fg="green", bg="#333333")
                label_success.pack(pady=10)
            else:
                label_error = Label(frame, text="Please fill in both fields.", font=("Arial", 12),  fg="red", bg="#333333")
                label_error.pack(pady=10)

        button_submit = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Submit", font=("Arial", 12), command= lambda: update_now(entry_field.get(), entry_value.get(), customer_id))
        button_submit.pack(pady=10)

        back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=lambda: old_customer_menu_admin(customer_id))
        back.pack(pady=10)


    button_update = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Update Customer Info", font=("Arial", 12), command=lambda:customer_update_admin(customer_id))
    button_update.pack(pady=10)

    def add_extra_admin(customer_id,admin = admin):
        clear_window()
        frame = new_frame()

        label = Label(frame, text="Add Extra Details", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
        label.pack(pady=20)



        label_value = Label(frame, text="Value:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
        label_value.pack(pady=10)
        entry_value = Entry(frame, font=("Arial", 12))
        entry_value.pack(pady=5)

        def add_now(value, customer_id,admin = admin):
            admin.add_extra_details(customer_id, value)
            label_success = Label(frame, text="Extra details added successfully!", font=("Arial", 12),  fg="green", bg="#333333")
            label_success.pack(pady=10)

        button_submit = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Submit", font=("Arial", 12), command=lambda: add_now( entry_value.get(), customer_id))
        button_submit.pack(pady=10)

        back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=lambda: old_customer_menu_admin(customer_id))
        back.pack(pady=10)


    button_add = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Add Extra Details", font=("Arial", 12), command=lambda: add_extra_admin(customer_id))
    button_add.pack(pady=10)

    def delete_field_admin(customer_id,admin = admin):
        clear_window()
        frame = new_frame()

        

        label = Label(frame, text="Update Customer Info", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
        label.pack(pady=20)

        field_name = Label(frame,text = "Fields: " + customerfields(customer_id), font=("Arial",9,"italic"), fg ="#FFFFFF", bg="#333333")
        field_name.pack()

        label_field = Label(frame, text="Field to Update:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
        label_field.pack(pady=10)
        entry_field = Entry(frame, font=("Arial", 12))
        entry_field.pack(pady=5)

        
        def delete_now(value, customer_id,admin = admin):
            admin.delete_customer_key(customer_id,value)
            label_success = Label(frame, text="Field deleted successfully!", font=("Arial", 12),  fg="green", bg="#333333")
            label_success.pack(pady=10)

        button_submit = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Submit", font=("Arial", 12), command=lambda: delete_now( entry_field.get(), customer_id))
        button_submit.pack(pady=10)

        back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=lambda: old_customer_menu_admin(customer_id))
        back.pack(pady=10)

    button_delete = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Delete Customer's data field", font=("Arial", 12), command=lambda: delete_field_admin(customer_id))
    button_delete.pack(pady=10)

    def delete_customer_admin(customer_id,admin = admin):
        admin.delete_customer(customer_id)
        label_success = Label(frame, text="Customer deleted successfully!", font=("Arial", 12), fg="green", bg="#333333")
        label_success.pack(pady=10)




    button_delete = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Delete Customer", font=("Arial", 12), command=lambda: delete_customer_admin(customer_id))
    button_delete.pack(pady=10)

    back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=customer_search)
    back.pack(pady=10)

def customer_search(admin = admin):
    clear_window()
    frame = new_frame()

    label = Label(frame, text="NSM_Courier Admin Panel", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
    label.pack(pady=20)

    label_search = Label(frame, text="Search Customer by ID:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
    label_search.pack(pady=10)
    entry_search = Entry(frame, font=("Arial", 12))
    entry_search.pack(pady=5)
    def search_now(customer_id,admin = admin):
        customer = admin.search_customer(customer_id)
        if customer:
            label_success = Label(frame, text="Customer found!", font=("Arial", 12), fg="green", bg="#333333")
            label_success.pack(pady=10)
            old_customer_menu_admin(customer_id)
        else:
            label_error = Label(frame, text="Customer not found!", font=("Arial", 12), fg="red", bg="#333333")
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

def main_admin_menu():
    clear_window()
    frame = new_frame()

    label = Label(frame, text="NSM_Courier Admin Panel", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
    label.pack(pady=20)


    button_search = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Search Customer", font=("Arial", 12), command=customer_search)
    button_search.pack(pady=10)

    button_change_password = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Change Password", font=("Arial", 12), command=lambda: change_password_admin(email))
    button_change_password.pack(pady=10)

    button_exit = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Exit", font=("Arial", 12), command=window.destroy)
    button_exit.pack(pady=10)

    

main_admin_menu()

window.mainloop()


