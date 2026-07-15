from roles import DeliveryBoy

DATA_FILE = "/home/coder/Documents/DSML-LEARNING/Project_1/user_delivery_data.json"

delivery_boy = DeliveryBoy(DATA_FILE)

# Search for a customer
customer = delivery_boy.search_customer("12345")

# Display customer details
details = delivery_boy.view_customer_details("12345")

# Request a status change and generate an OTP
otp = delivery_boy.request_delivery_status_change(
    "12345",
    "Delivered"
)

if otp is not None:
    print("Give this OTP to the customer:", otp)