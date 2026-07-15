from customer_roles import DeliveryBoy

delivery_boy = DeliveryBoy("/path/to/user_delivery_data.json")

if delivery_boy.search_customer(customer_id):
    details = delivery_boy.view_customer_details(customer_id)
    otp = delivery_boy.request_status_change(customer_id, "Delivered")