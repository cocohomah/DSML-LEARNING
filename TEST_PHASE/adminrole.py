from customer_roles import Admin
import json
from tkinter import *

admin = Admin("/home/coder/Documents/DSML-LEARNING/Project_1/user_delivery_data.json")

if admin.search_customer(customer_id):
    details = admin.view_customer_details(customer_id)
    admin.update_customer_details(customer_id, "status", "Delivered")
    admin.add_extra_info(customer_id, "Priority customer")
    admin.delete_customer(customer_id)