import json
import random



class BaseUser:
    def change_password(self,email, new_password):
        with open("/home/coder/Documents/DSML-LEARNING/TEST_PHASE/user_login_data.json") as file:
            data = json.load(file)
        data[email][1] = new_password
        with open("/home/coder/Documents/DSML-LEARNING/TEST_PHASE/user_login_data.json", "w") as file:
            json.dump(data, file, indent=4)

class Admin(BaseUser):

    def __init__(self, file_path):

        self.file_path = file_path


        self.extra_counter = random.randint(1000, 999999)

    # ==============================================================
    # ADMIN METHOD: Search for a customer
    # ==============================================================

    def search_customer(self, customer_id):


        # JSON object keys are strings, so convert the ID to a string.
        customer_id = str(customer_id).strip()

        # Open and read the JSON database.
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Check whether the customer ID exists.
        if customer_id in data:
            return data[customer_id]

        return None

    # ==============================================================
    # ADMIN METHOD: View customer details
    # ==============================================================

    def view_customer_details(self, customer_id):


        customer = self.search_customer(customer_id)

        if customer is None:
            return None

        # Convert the dictionary into readable text.
        return json.dumps(customer, indent=4)

    # ==============================================================
    # ADMIN METHOD: Update existing customer information
    # ==============================================================

    def update_customer_info(self, customer_id, key, value):


        customer_id = str(customer_id).strip()
        key = str(key).strip()

        # Read the current database.
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Check that the customer exists.
        if customer_id not in data:
            return False

        # Check that the key already exists.
        if key not in data[customer_id]:
            return False

        # Update the value.
        data[customer_id][key] = value

        # Save the updated database.
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True

    # ==============================================================
    # ADMIN METHOD: Add extra information
    # ==============================================================

    def add_extra_details(self, customer_id, extra_value):


        customer_id = str(customer_id).strip()

        # Read the database.
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Check that the customer exists.
        if customer_id not in data:
            return None

        # Create a key for the extra information.
        key_name = "extra_" + str(self.extra_counter)

        # Make sure the generated key does not already exist.
        while key_name in data[customer_id]:
            self.extra_counter += 1
            key_name = "extra_" + str(self.extra_counter)

        # Add the new information.
        data[customer_id][key_name] = extra_value

        # Increase the counter for the next extra detail.
        self.extra_counter += 1

        # Save the updated database.
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return key_name

    # ==============================================================
    # ADMIN METHOD: Delete a customer
    # ==============================================================

    def delete_customer(self, customer_id):

        customer_id = str(customer_id).strip()

        # Read the database.
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Check that the customer exists.
        if customer_id not in data:
            return False

        # Delete the customer.
        del data[customer_id]

        # Save the database after deletion.
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True
    # ==============================================================
    # ADMIN METHOD: Delete a key from a customer record
    # ==============================================================
    def delete_customer_key(self, customer_id, key):

        customer_id = str(customer_id).strip()
        key = str(key).strip()

        # Read the database.
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Check that the customer exists.
        if customer_id not in data:
            return False

        # Check that the key exists.
        if key not in data[customer_id]:
            return False

        # Delete the key from the customer's record.
        del data[customer_id][key]

        # Save the updated database.
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True


class DeliveryBoy(BaseUser):
    """
    DeliveryBoy class.

    Import this class into your Delivery Boy page.

    Delivery Boy features:
    - Search for customers
    - View customer details
    - Request a delivery status change
    - Generate an OTP for the customer
    """

    def __init__(self, file_path):
        """
        file_path is the location of your JSON database.

        Example:
            delivery_boy = DeliveryBoy("user_delivery_data.json")
        """
        self.file_path = file_path

    # ==============================================================
    # DELIVERY BOY METHOD: Search for a customer
    # ==============================================================

    def search_customer(self, customer_id):
        """
        Search for a customer using the customer ID.

        Returns:
            The customer's dictionary if the customer exists.
            None if the customer does not exist.

        Example in your Delivery Boy page:

            customer = delivery_boy.search_customer("12345")

            if customer is not None:
                print(customer)
            else:
                print("Customer not found.")
        """

        customer_id = str(customer_id).strip()

        # Open and read the JSON database.
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Check whether the customer ID exists.
        if customer_id in data:
            return data[customer_id]

        return None

    # ==============================================================
    # DELIVERY BOY METHOD: View customer details
    # ==============================================================

    def view_customer_details(self, customer_id):
        """
        Get customer details in a formatted JSON string.

        This can be displayed in your Delivery Boy page.

        Example:

            details = delivery_boy.view_customer_details("12345")

            if details is not None:
                details_label.config(text=details)
            else:
                details_label.config(text="Customer not found.")
        """

        customer = self.search_customer(customer_id)

        if customer is None:
            return None

        # Convert the dictionary into readable text.
        return json.dumps(customer, indent=4)

    # ==============================================================
    # DELIVERY BOY METHOD: Request a delivery status change
    # ==============================================================

    def request_delivery_status_change(self, customer_id, requested_status):
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

            otp = delivery_boy.request_delivery_status_change(
                "12345",
                "Delivered"
            )

            if otp is not None:
                print("OTP generated:", otp)
            else:
                print("Customer not found.")
        """

        customer_id = str(customer_id).strip()
        requested_status = str(requested_status).strip()

        # Read the current database.
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Check that the customer exists.
        if customer_id not in data:
            return None

        # Generate a random six-digit OTP.
        otp = str(random.randint(100000, 999999))

        # Save the requested status and OTP.
        # The original status is not changed yet.
        data[customer_id]["pending_status"] = requested_status
        data[customer_id]["otp"] = otp

        # Save the updated database.
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return otp