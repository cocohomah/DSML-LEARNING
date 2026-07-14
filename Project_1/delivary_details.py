from tkinter import *
import json




class Customer:

 def __init__(self, data,id):
    self.name = data[id]['name']
    self.email = data[id]['email']
    self.phone = data[id]['phone']
    self.street = data[id]['street']
    self.zip_code = data[id]['zip_code']
    self.city = data[id]['city']
    self.status = data[id]['status']
    self.time = data[id]['time']
    self.contact_method = data[id]['contact_method']
 
 def display_details(self):
    window = Tk()
    window.geometry("500x700")
    window.title("Delivery Details")
    window.config(background = "#333333" )

    title = Label(window,text="Delivery Details",bg='#333333', fg="#FF3399", font=("Arial", 30,'bold'))
    title.pack(pady=20)

    details = f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nStreet: {self.street}\nZip Code: {self.zip_code}\nCity: {self.city}\nStatus: {self.status}\nTime: {self.time}\nContact Method: {self.contact_method}"
    details_label = Label(window, text=details, bg='#333333', fg="#FFFFFF", font=("Arial", 16), justify=LEFT)
    details_label.pack(pady=20)

    window.mainloop()

with open('/home/coder/Documents/DSML-LEARNING/Project_1/user_delivery_data.json',"r") as f:
  data = json.load(f)
  C1 = Customer(data, "12345")
  C1.display_details()

