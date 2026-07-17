from roles import DeliveryAgent
from tkinter import *
import sys
import json

email = sys.argv[1]

DATA_FILE = "/home/coder/Documents/DSML-LEARNING/TEST_PHASE/user_delivery_data.json"

delivery_agent = DeliveryAgent(DATA_FILE)

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


def tracking_menu_delivery_agent(tracking_id,delivery_agent = delivery_agent):
    clear_window()
    frame = new_frame()

    label = Label(frame, text="NSM_Courier delivery_agent Panel", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
    label.pack(pady=20)
    def view_tracking_details_delivery_agent(tracking_id,delivery_agent = delivery_agent):
        item = delivery_agent.search_tracking_id(tracking_id)
        if item:
            clear_window()
            frame = new_frame()

            label = Label(frame, text="Tracking Details", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
            label.pack(pady=20)

            for key, value in item.items():
                if key == "request_by_delivery_agent":
                    continue
                detail_label = Label(frame, text=f"{key}: {value}", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
                detail_label.pack(pady=5)


            
        else:
            label_error = Label(frame, text="Tracking ID not found!", font=("Arial", 12), fg="red", bg="#333333")
            label_error.pack(pady=10)
        
        back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=lambda: tracking_menu_delivery_agent(tracking_id))
        back.pack(pady=10)


    button_view = Button(frame,bg="#FF3399", fg="#FFFFFF", text="View Tracking Details", font=("Arial", 12), command=lambda: view_tracking_details_delivery_agent(tracking_id))
    button_view.pack(pady=10)

    back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=item_search)
    back.pack(pady=10)
    


def item_search(delivery_agent = delivery_agent):
    clear_window()
    frame = new_frame()

    label = Label(frame, text="NSM_Courier delivery_agent Panel", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
    label.pack(pady=20)

    label_search = Label(frame, text="Search Item by Tracking ID:", font=("Arial", 12), fg ="#FFFFFF", bg="#333333")
    label_search.pack(pady=10)
    entry_search = Entry(frame, font=("Arial", 12))
    entry_search.pack(pady=5)
    def search_now(tracking_id,delivery_agent = delivery_agent):
        item = delivery_agent.search_tracking_id(tracking_id)
        if item:
            label_success = Label(frame, text="Tracking ID found!", font=("Arial", 12), fg="green", bg="#333333")
            label_success.pack(pady=10)
            tracking_menu_delivery_agent(tracking_id)
        else:
            label_error = Label(frame, text="Tracking ID not found!", font=("Arial", 12), fg="red", bg="#333333")
            label_error.pack(pady=10)
    button_search = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Search", font=("Arial", 12), command=lambda: search_now(entry_search.get()))
    button_search.pack(pady=10)

    back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=main_delivery_agent_menu)
    back.pack(pady=10)


def change_password_delivery_agent(email,delivery_agent = delivery_agent):
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
            delivery_agent.change_password(email, new_password)
            label_success = Label(frame, text="Password updated successfully!", font=("Arial", 12), fg="green", bg="#333333")
            label_success.pack(pady=10)
        else:
            label_error = Label(frame, text="Please enter a new password.", font=("Arial", 12), fg="red", bg="#333333")
            label_error.pack(pady=10)

    button_submit = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Submit", font=("Arial", 12), command=lambda: update_password(entry_new_password.get(), email))
    button_submit.pack(pady=10)

    back = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Back", font=("Arial", 12), command=main_delivery_agent_menu)
    back.pack(pady=10)



def main_delivery_agent_menu():
    clear_window()
    frame = new_frame()

    label = Label(frame, text="NSM_Courier delivery_agent Panel", font=("Arial", 16,"bold"), fg ="#FF3399", bg="#333333")
    label.pack(pady=20)


    button_search = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Search Item", font=("Arial", 12), command=item_search)
    button_search.pack(pady=10)

    button_change_password = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Change Password", font=("Arial", 12), command=lambda: change_password_delivery_agent(email))
    button_change_password.pack(pady=10)

    button_logout = Button(frame, bg="#FF3399", fg="#FFFFFF", text="Logout", font=("Arial",12), command=lambda: delivery_agent.logout(window))
    button_logout.pack(pady=10)

    button_exit = Button(frame,bg="#FF3399", fg="#FFFFFF", text="Exit", font=("Arial", 12), command=window.destroy)
    button_exit.pack(pady=10)


main_delivery_agent_menu()
window.mainloop()



# # Request a status change and generate an OTP
# otp = delivery_agent.request_delivery_status_change(
#     "12345",
#     "Delivered"
# )

# if otp is not None:
#     print("Give this OTP to the item:", otp)