import json
import os
import random


class DatabaseManager:
    """
    Handles all reading, writing, and safe modification of the customer JSON database.
    
    This class is a utility for managing the JSON file — it is not tied to any specific role.
    Both Admin and DeliveryBoy classes use it internally to interact with the database.
    
    Expected JSON database format:
    {
        "12345": {
            "name": "John Doe",
            "address": "123 Main St, New York",
            "status": "Not_delivered"
        },
        "67890": {
            "name": "Jane Smith",
            "address": "456 Oak Ave, California",
            "status": "Not_delivered"
        }
    }
    
    Where the key ("12345") is the customer_id.
    """
    
    def __init__(self, file_path: str):
        """
        Initialise the DatabaseManager with the path to the JSON database file.
        
        Args:
            file_path (str): The absolute or relative path to the customer database JSON file.
        """
        self.file_path = file_path
        self.data = self._load_data()
    
    def _load_data(self) -> dict:
        """
        Internal method to load customer data from the JSON file.
        
        If the file doesn't exist, a fallback local file will be created.
        If the directory doesn't exist, the file will be created in the current working directory.
        
        Returns:
            dict: A dictionary containing all customer records, keyed by customer_id.
        """
        # Get the directory path from the provided file path
        dir_name = os.path.dirname(self.file_path)
        
        # If a directory is specified but doesn't exist, fall back to local file
        if dir_name and not os.path.exists(dir_name):
            self.file_path = "user_delivery_data.json"
        
        # Check if the JSON file already exists
        if not os.path.exists(self.file_path):
            # Initialise with sample customer data if file doesn't exist
            initial_data = {
                "12345": {
                    "name": "John Doe",
                    "address": "123 Main St, New York",
                    "status": "Not_delivered"
                },
                "67890": {
                    "name": "Jane Smith",
                    "address": "456 Oak Ave, California",
                    "status": "Not_delivered"
                }
            }
            
            # Create and write initial data to the JSON file
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(initial_data, f, indent=4)
            
            return initial_data
        
        # Load existing data from the JSON file
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data if isinstance(data, dict) else {}
        
        except (json.JSONDecodeError, OSError):
            # Return empty dictionary if file is corrupted or unreadable
            return {}
    
    def save_data(self) -> None:
        """
        Save the current in-memory customer data back to the JSON file.
        
        This method should be called after any modification (update, add, delete)
        to persist changes to the database.
        """
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)
    
    def get_customer(self, customer_id: str) -> dict | None:
        """
        Retrieve a specific customer's data using their customer ID.
        
        Args:
            customer_id (str): The unique ID of the customer.
        
        Returns:
            dict | None: A dictionary containing customer details if found, otherwise None.
        """
        return self.data.get(customer_id)
    
    def delete_customer(self, customer_id: str) -> bool:
        """
        Remove a customer record from the database using their customer ID.
        
        Args:
            customer_id (str): The unique ID of the customer to delete.
        
        Returns:
            bool: True if the customer was successfully deleted, False if not found.
        """
        if customer_id in self.data:
            del self.data[customer_id]
            self.save_data()
            return True
        
        return False


class BaseRole:
    """
    Base class containing shared functionality accessible to all roles.
    
    This class provides common methods (like searching for a customer) 
    that are inherited by both Admin and DeliveryBoy.
    """
    
    def __init__(self, db_manager: DatabaseManager):
        """
        Initialise a role instance with a DatabaseManager.
        
        Args:
            db_manager (DatabaseManager): An instance of DatabaseManager used to interact 
                                         with the customer JSON database.
        """
        self.db = db_manager
    
    # --------------------------------------------------------------------------
    # SHARED METHOD (Available to both Admin and DeliveryBoy)
    # --------------------------------------------------------------------------
    
    def search_customer(self, customer_id: str) -> dict | None:
        """
        Search for and retrieve a customer's details by their customer ID.
        
        This method is shared by both Admin and DeliveryBoy roles.
        
        Intended usage when imported into page code:
        - Admin page: Use this to look up a customer before updating, adding, or deleting their details.
        - DeliveryBoy page: Use this to look up a customer before requesting a delivery status change.
        
        Args:
            customer_id (str): The unique ID of the customer to search for.
        
        Returns:
            dict | None: Customer data dictionary if found, otherwise None.
            
        Example (Admin page):
            >>> admin = Admin(db_manager)
            >>> customer = admin.search_customer("12345")
            >>> if customer: print(customer["name"])
        
        Example (DeliveryBoy page):
            >>> delivery_boy = DeliveryBoy(db_manager)
            >>> customer = delivery_boy.search_customer("12345")
            >>> if customer: print(customer["status"])
        """
        return self.db.get_customer(customer_id)


class Admin(BaseRole):
    """
    Admin Role Class
     
    This class contains all methods and operations that are exclusively 
    available to an Administrator.
    
    It inherits shared functionality (search_customer) from BaseRole.
    
    Intended use:
    - Import this class into your Admin page/module.
    - Instantiate it with a DatabaseManager instance pointing to your JSON database file.
    - Call its methods to perform admin-specific actions (update, add extra info, delete customers, etc.).
    
    Admin responsibilities and capabilities:
    - Search for customers (inherited)
    - Update existing customer information (modify specific fields)
    - Add extra details/metadata to a customer record
    - Delete a customer from the database permanently
    """
    
    def __init__(self, db_manager: DatabaseManager):
        """
        Initialise an Admin instance.
        
        Args:
            db_manager (DatabaseManager): DatabaseManager instance for accessing the customer database.
        
        Example (in your Admin page code):
            >>> from roles import Admin, DatabaseManager
            >>> db = DatabaseManager("user_delivery_data.json")
            >>> admin = Admin(db)
        """
        # Call parent constructor to initialise shared database access
        super().__init__(db_manager)
        
        # Internal counter for generating unique keys for extra details
        # Used by add_extra_details() to create keys like "extra_100245", "extra_100246", etc.
        self._extra_counter = random.randint(100000, 999999)
    
    # --------------------------------------------------------------------------
    # ADMIN-SPECIFIC METHODS
    # --------------------------------------------------------------------------
    
    def update_customer_info(self, customer_id: str, key: str, value: str) -> bool:
        """
        ADMIN METHOD: Update an existing field/value for a specific customer.
        
        This method allows the admin to modify an existing attribute of a customer record.
        It will only update a field if it already exists in the customer's data — 
        it will NOT create a new field if the key is missing.
        
        How to use in your Admin page code:
        - First, search for the customer using search_customer(customer_id) to confirm they exist.
        - Call this method with the customer ID, the field name (key), and the new value.
        - The method returns True if the update was successful, False otherwise.
        
        Args:
            customer_id (str): The unique ID of the customer to update.
            key (str): The name of the existing field to update (e.g., "name", "address", "status").
            value (str): The new value to assign to that field.
        
        Returns:
            bool: True if the customer's information was successfully updated, False if:
                  - the customer was not found, OR
                  - the specified key does not exist in the customer's record.
        
        Example (Admin page logic):
            >>> customer_id = "12345"
            >>> customer = admin.search_customer(customer_id)
            >>> if not customer:
            ...     show_error("Customer not found.")
            ... else:
            ...     success = admin.update_customer_info(customer_id, "status", "Delivered")
            ...     if success:
            ...         show_success("Customer status updated successfully.")
            ...     else:
            ...         show_error("The field you want to update does not exist.")
        
        Database effect:
        - Modifies `data[customer_id][key] = value` in the JSON structure.
        - Persists changes immediately by calling save_data().
        """
        # Retrieve the customer record
        customer = self.search_customer(customer_id)
        
        # Check if customer exists and the key is present
        if customer is None:
            return False
        
        if key not in customer:
            return False
        
        # Perform the update
        customer[key] = value
        
        # Save changes to the database
        self.db.save_data()
        
        return True
    
    def add_extra_details(self, customer_id: str, extra_value: str) -> str:
        """
        ADMIN METHOD: Add extra details/metadata to a customer's record.
        
        This method allows the admin to append additional information to a customer profile
        that wasn't part of the original schema. It generates a unique, randomised key 
        (e.g., "extra_100245") for the new piece of information.
        
        This is useful for storing notes, special instructions, delivery remarks, 
        internal tags, or any other supplementary information.
        
        How to use in your Admin page code:
        - Search for the customer using search_customer(customer_id) to ensure they exist.
        - Collect the extra detail value from an input field (e.g., text entry).
        - Call this method with the customer ID and the value.
        - The method returns the generated key name (e.g., "extra_100245") so you can 
          display it to the admin for future reference, or an empty string if failed.
        
        Args:
            customer_id (str): The unique ID of the customer to add extra details to.
            extra_value (str): The additional information/value to store for the customer.
        
        Returns:
            str: The generated key name (e.g., "extra_100245") if successful, 
                 otherwise an empty string if the customer was not found.
        
        Example (Admin page logic):
            >>> customer_id = "12345"
            >>> extra_info = "Leave package with security guard."
            >>> key_name = admin.add_extra_details(customer_id, extra_info)
            >>> if key_name:
            ...     show_success(f"Extra detail added under '{key_name}'.")
            ... else:
            ...     show_error("Customer not found.")
        
        Database effect:
        - Adds `customer[key_name] = extra_value` (e.g., "extra_100245": "Leave package with security guard")
        - Increments the internal counter for future extra details.
        - Persists changes immediately by calling save_data().
        """
        # Retrieve the customer record
        customer = self.search_customer(customer_id)
        
        if customer is None:
            return ""
        
        # Generate a unique key for this extra detail
        key_name = f"extra_{self._extra_counter}"
        
        # Increment the counter for the next extra detail
        self._extra_counter += 1
        
        # Add the extra detail to the customer record
        customer[key_name] = extra_value
        
        # Save changes to the database
        self.db.save_data()
        
        return key_name
    
    def delete_customer(self, customer_id: str) -> bool:
        """
        ADMIN METHOD: Delete a customer from the database permanently.
        
        This method completely removes a customer profile and all associated data 
        from the JSON database using their customer ID.
        
        ⚠️ This action is irreversible. It is strongly recommended that your Admin page
        prompts for confirmation (e.g., a confirmation dialog/yes-no prompt) before 
        calling this method.
        
        How to use in your Admin page code:
        - Have the admin enter or select a customer ID.
        - Display a confirmation message asking "Are you sure you want to permanently 
          delete customer {customer_id}?".
        - If confirmed, call this method with the customer ID.
        - Check the boolean return value to inform the admin whether deletion succeeded.
        
        Args:
            customer_id (str): The unique ID of the customer to delete from the database.
        
        Returns:
            bool: True if the customer was successfully deleted, False if the customer 
                  was not found in the database.
        
        Example (Admin page logic):
            >>> customer_id = "12345"
            >>> confirmed = show_confirmation(f"Delete customer {customer_id} permanently?")
            >>> if confirmed:
            ...     deleted = admin.delete_customer(customer_id)
            ...     if deleted:
            ...         show_success("Customer has been deleted successfully.")
            ...     else:
            ...         show_error("Customer not found. Could not delete.")
        
        Database effect:
        - Removes the entire customer entry: `del data[customer_id]`.
        - Persists changes immediately by calling save_data().
        """
        # Delegate deletion to the DatabaseManager
        return self.db.delete_customer(customer_id)


class DeliveryBoy(BaseRole):
    """
    DeliveryBoy Role Class
    
    This class contains all methods and operations that are relevant 
    to a Delivery Operator (Delivery Boy).
    
    It inherits shared functionality (search_customer) from BaseRole.
    
    Intended use:
    - Import this class into your Delivery Boy page/module.
    - Instantiate it with a DatabaseManager instance pointing to your JSON database file.
    - Call its methods to perform delivery-related actions (view customer, request status change, etc.).
    
    DeliveryBoy responsibilities and capabilities:
    - Search for customers (inherited) to view their delivery details
    - Request a change in delivery status and generate a verification OTP for the customer
    """
    
    def __init__(self, db_manager: DatabaseManager):
        """
        Initialise a DeliveryBoy instance.
        
        Args:
            db_manager (DatabaseManager): DatabaseManager instance for accessing the customer database.
        
        Example (in your Delivery Boy page code):
            >>> from roles import DeliveryBoy, DatabaseManager
            >>> db = DatabaseManager("user_delivery_data.json")
            >>> delivery_boy = DeliveryBoy(db)
        """
        # Call parent constructor to initialise shared database access
        super().__init__(db_manager)
    
    # --------------------------------------------------------------------------
    # DELIVERY BOY–SPECIFIC METHODS
    # --------------------------------------------------------------------------
    
    def request_delivery_status_change(self, customer_id: str, requested_status: str) -> str:
        """
        DELIVERY BOY METHOD: Request a change in delivery status and generate a verification OTP.
        
        This method allows the delivery boy to initiate a delivery status update request 
        for a specific customer. When called, it:
        - Generates a secure, random 6-digit OTP (One-Time Password).
        - Stores the requested new status as `pending_status` in the customer's record.
        - Stores the generated OTP as `otp` in the customer's record.
        
        The OTP can later be used in your Customer interface (or presented to the customer)
        to verify and confirm the delivery status change before finalising it.
        
        How to use in your Delivery Boy page code:
        - First, search for the customer using search_customer(customer_id) to confirm they exist.
        - Select or enter the new delivery status (e.g., "Delivered", "Returned_To_Hub", "Attempted_Delivery").
        - Call this method with the customer ID and the requested status.
        - The method returns the 6-digit OTP string. You should display this OTP to the delivery boy 
          (or allow them to share it with the customer) so it can be used for verification later.
        
        Args:
            customer_id (str): The unique ID of the customer whose delivery status is being changed.
            requested_status (str): The new delivery status being requested 
                                    (e.g., "Delivered", "Not_delivered", "Returned_To_Hub", 
                                    "Attempted_Delivery", etc.).
        
        Returns:
            str: A 6-digit OTP string (e.g., "482716") if the customer was found and 
                 the request was successfully recorded. Returns an empty string ("") 
                 if the customer was not found.
        
        Example (Delivery Boy page logic):
            >>> customer_id = "12345"
            >>> customer = delivery_boy.search_customer(customer_id)
            >>> if not customer:
            ...     show_error("Customer not found.")
            ... else:
            ...     # Delivery boy selects new status
            ...     new_status = "Delivered"
            ...     otp_code = delivery_boy.request_delivery_status_change(customer_id, new_status)
            ...     if otp_code:
            ...         show_info(f"OTP generated: {otp_code}. Share this with the customer for verification.")
            ...     else:
            ...         show_error("Unable to process status change request.")
        
        Database effect:
        - Adds/updates two fields on the customer's record:
          - `customer["pending_status"] = requested_status`
          - `customer["otp"] = otp_code` (6-digit string)
        - Persists changes immediately by calling save_data().
        
        Notes for integration with Customer interface later:
        - The customer interface should prompt the customer to enter this OTP.
        - Once verified, you can move `pending_status` to `status` and clear/remove `otp` 
          and `pending_status` fields if desired.
        - This class does NOT finalise the status change — it only creates a pending request 
          with OTP for verification.
        """
        # Retrieve the customer record
        customer = self.search_customer(customer_id)
        
        if customer is None:
            return ""
        
        # Generate a random 6-digit OTP for verification
        otp_code = str(random.randint(100000, 999999))
        
        # Record the pending status change request along with the OTP
        customer["pending_status"] = requested_status
        customer["otp"] = otp_code
        
        # Save changes to the database
        self.db.save_data()
        
        return otp_code


# --------------------------------------------------------------------------
# USAGE EXAMPLES (For reference only — not part of the class logic)
# --------------------------------------------------------------------------

# Example: How to import and use in your Admin page
# -------------------------------------------------
# from roles import Admin, DatabaseManager
# 
# # Initialise database manager (point to your JSON file)
# db_manager = DatabaseManager("user_delivery_data.json")
# 
# # Create Admin instance
# admin = Admin(db_manager)
# 
# # Search for a customer
# customer = admin.search_customer("12345")
# 
# # Update customer info
# admin.update_customer_info("12345", "status", "Delivered")
# 
# # Add extra details
# key_generated = admin.add_extra_details("12345", "Handle with care - fragile item")
# 
# # Delete customer
# admin.delete_customer("67890")

# Example: How to import and use in your Delivery Boy page
# ---------------------------------------------------------
# from roles import DeliveryBoy, DatabaseManager
# 
# # Initialise database manager
# db_manager = DatabaseManager("user_delivery_data.json")
# 
# # Create DeliveryBoy instance
# delivery_boy = DeliveryBoy(db_manager)
# 
# # Search for a customer to view delivery details
# customer = delivery_boy.search_customer("12345")
# 
# # Request delivery status change and generate OTP
# otp = delivery_boy.request_delivery_status_change("12345", "Delivered")
# # Display otp to delivery boy so they can share it with the customer