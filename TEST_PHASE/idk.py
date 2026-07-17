import random 
import json
def request_delivery_status_change( customer_id, requested_status):


        data = {
            "12345": {
        "name": "Ronaldo",
        "street": "123 Main St",
        "city": "Anytown",
        "zip_code": "12345",
        "phone": "9514521452",
        "email": "idk@gmail.com",
        "status": "Not_delivered",
        "time": "Evening",
        "contact_method": "Email"
         }
        }

        if customer_id not in data:
            return None


        otp = str(random.randint(100000, 999999))

        data[customer_id]["request"]={}
        data[customer_id]["request"]["pending_status"] = requested_status
        data[customer_id]["request"]["otp"] = otp

        # Save the updated database.
        with open("/home/coder/Documents/DSML-LEARNING/TEST_PHASE/user_delivery_data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return otp
    


request_delivery_status_change("12345","delivered")

