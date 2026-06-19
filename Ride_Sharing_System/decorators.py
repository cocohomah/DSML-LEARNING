
def ride_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("\nRide booked successfully!\n")
        return result
    return wrapper
