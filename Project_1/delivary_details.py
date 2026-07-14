from tkinter import *
import json

counter = 0


class Existing_Customer:

 def __init__(self, data,id):
    self.id = id
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

 def add_extra_details(self):
      window = Tk()
      window.geometry("500x700")
      window.title("Delivery Details")
      window.config(background = "#333333" )

      ask = Label(window,text="Enter extra data",bg='#333333', fg="#FF3399", font=("Arial", 20,'bold'))
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

      window.mainloop()

with open('/home/coder/Documents/DSML-LEARNING/Project_1/user_delivery_data.json',"r") as f:
  data = json.load(f)



