import json
import random
import sys
import subprocess


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
    """
    DeliveryAgent class.

    Import this class into your Delivery Boy page.

    Delivery Boy features:
    - Search for customers
    - View customer details
    - Request a delivery status change
    - Generate an OTP for the customer
    """

    def __init__(self, file_path):
        self.file_path = file_path




    # ==============================================================
    # DELIVERY BOY METHOD: Request a delivery status change
    # ==============================================================

    def request_delivery_status_change(self, tracking_id, requested_status):
        """
        Request a delivery status change and generate an OTP.

        This method does not immediately change the customer's
        actual status.

        It adds these two fields to the customer record:

            "pending_status": "Delivered",
            "otp": "123456"

        Your future Customer page can ask the customer for the OTP.
        If the OTP is correct, that page can complete the status change.

        Returns:
            The generated OTP as a string if successful.
            None if the customer was not found.

        Example in your Delivery Boy page:

            otp = delivery_agent.request_delivery_status_change(
                "12345",
                "Delivered"
            )

            if otp is not None:
                print("OTP generated:", otp)
            else:
                print("Customer not found.")
        """

        tracking_id = str(tracking_id).strip()
        requested_status = str(requested_status).strip()

        # Read the current database.
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Check that the customer exists.
        if tracking_id not in data:
            return None

        # Generate a random six-digit OTP.
        otp = str(random.randint(100000, 999999))

        # Save the requested status and OTP.
        # The original status is not changed yet.
        data[tracking_id]["request"]={}
        data[tracking_id]["request"]["pending_status"] = requested_status
        data[tracking_id]["request"]["otp"] = otp

        # Save the updated database.
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return otp