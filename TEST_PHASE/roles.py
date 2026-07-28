import json
import random
import sys
import subprocess
import string

class BaseUser:

        # ==============================================================
    # ADMIN METHOD: Search for a customer
    # ==============================================================

    def search_tracking_id(self, tracking_id):


        # JSON object keys are strings, so convert the ID to a string.
        tracking_id = str(tracking_id).strip()

        # Open and read the JSON database.
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Check whether the customer ID exists.
        if tracking_id in data:
            return data[tracking_id]

        return None

    # ==============================================================
    # ADMIN METHOD: View customer details
    # ==============================================================

    def view_tracking_details(self, tracking_id):


        customer = self.search_tracking_id(tracking_id)

        if customer is None:
            return None

        # Convert the dictionary into readable text.
        return json.dumps(customer, indent=4)

    def change_password(self,email, new_password):
        with open("/home/coder/Documents/DSML-LEARNING/TEST_PHASE/user_login_data.json") as file:
            data = json.load(file)
        data[email][1] = new_password
        with open("/home/coder/Documents/DSML-LEARNING/TEST_PHASE/user_login_data.json", "w") as file:
            json.dump(data, file, indent=4)

    def logout(self,window):
            subprocess.Popen([sys.executable, "/home/coder/Documents/DSML-LEARNING/TEST_PHASE/login_system.py"])
            window.destroy()

class Admin(BaseUser):

    def __init__(self, file_path):

        self.file_path = file_path


        self.extra_counter = random.randint(1000, 999999)



    # ==============================================================
    # ADMIN METHOD: Update existing customer information
    # ==============================================================

    def update_tracking_info(self, tracking_id, key, value):


        tracking_id = str(tracking_id).strip()
        key = str(key).strip()

        # Read the current database.
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Check that the customer exists.
        if tracking_id not in data:
            return False

        # Check that the key already exists.
        if key not in data[tracking_id]:
            return False

        # Update the value.
        data[tracking_id][key] = value

        # Save the updated database.
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True

    # ==============================================================
    # ADMIN METHOD: Add extra information
    # ==============================================================

    def add_extra_details(self, tracking_id, extra_value):


        tracking_id = str(tracking_id).strip()

        # Read the database.
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Check that the customer exists.
        if tracking_id not in data:
            return None

        # Create a key for the extra information.
        key_name = "extra_" + str(self.extra_counter)

        # Make sure the generated key does not already exist.
        while key_name in data[tracking_id]:
            self.extra_counter += 1
            key_name = "extra_" + str(self.extra_counter)

        # Add the new information.
        data[tracking_id][key_name] = extra_value

        # Increase the counter for the next extra detail.
        self.extra_counter += 1

        # Save the updated database.
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return key_name

    # ==============================================================
    # ADMIN METHOD: Delete a customer
    # ==============================================================

    def delete_item(self, tracking_id):

        tracking_id = str(tracking_id).strip()

        # Read the database.
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Check that the customer exists.
        if tracking_id not in data:
            return False

        # Delete the customer.
        del data[tracking_id]

        # Save the database after deletion.
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True
    # ==============================================================
    # ADMIN METHOD: Delete a key from a customer record
    # ==============================================================
    def delete_item_key(self, tracking_id, key):

        tracking_id = str(tracking_id).strip()
        key = str(key).strip()

        # Read the database.
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Check that the customer exists.
        if tracking_id not in data:
            return False

        # Check that the key exists.
        if key not in data[tracking_id]:
            return False

        # Delete the key from the customer's record.
        del data[tracking_id][key]

        # Save the updated database.
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True


class DeliveryAgent(BaseUser):

    def __init__(self, file_path):
        self.file_path = file_path




    # ==============================================================
    # DELIVERY BOY METHOD: Request a delivery status change
    # ==============================================================

    def request_delivery_status_change(self, tracking_id, requested_status):


        tracking_id = str(tracking_id).strip()
        requested_status = str(requested_status).strip()


        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if tracking_id not in data:
            return None

        otp = str(random.randint(100000, 999999))

        data[tracking_id]["request_by_delivery_agent"]={}
        data[tracking_id]["request_by_delivery_agent"]["pending_status"] = requested_status
        data[tracking_id]["request_by_delivery_agent"]["otp"] = otp

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

        return True
    
    # ==============================================================
    # DELIVERY BOY METHOD: CHECK THE OTP
    # ==============================================================

    def check_otp(self,tracking_id, otp):
        
        tracking_id = str(tracking_id).strip()
        otp = str(otp).strip()


        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        if  data[tracking_id]["request_by_delivery_agent"]["otp"] == otp:
            data[tracking_id]["status"] = "Delivered"
            del data[tracking_id]["request_by_delivery_agent"]
        else:
            return None
        

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)
        
        return True





class customer(BaseUser):

    def __init__(self, file_path):

        self.file_path = file_path

    def add(self,name, weight, handling, delivered_to_address, sent_from_address,email, time,contact_method,number_of_recceiver,email_of_recceiver):
        tracking_id = ''.join(random.choices(string.ascii_letters + string.digits,k = 20))
        
        with open(self.file_path, "r") as file:
             data = json.load(file)

        with open('/home/coder/Documents/DSML-LEARNING/TEST_PHASE/user_login_data.json',"r") as file:
            login_data = json.load(file)

        delivery_agents = []
        for key, value in login_data.items():
            if value[2] == "delivery_agent":
                delivery_agents.append(key)

        delivery_agent_email = random.choice(delivery_agents)
        delivery_agent_name = login_data[str(delivery_agent_email)][3]

        data[tracking_id]={}
        data[tracking_id]["Name"] = name
        data[tracking_id]["Weight"] = weight + "KG"
        data[tracking_id]["Handling"] = handling
        data[tracking_id]["Delivered_to_address"] = delivered_to_address
        data[tracking_id]["Recceiver's Phone Number"]=number_of_recceiver
        data[tracking_id]["Recceiver's Email"]=email_of_recceiver
        data[tracking_id]["Sent_from_address"] = sent_from_address
        data[tracking_id]["Status"] = "Not Delivered"
        data[tracking_id]["Email"] = email
        data[tracking_id]["Time"] = time
        data[tracking_id]["Contact_method"] = contact_method
        data[tracking_id]["Delivery_agent_email"] = delivery_agent_email
        data[tracking_id]["Delivery_agent_name"] = delivery_agent_name

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

