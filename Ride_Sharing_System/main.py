from vehicles import Bike, Car
from decorators import ride_logger
from exceptions import InvalidRatingError, NegativeDistanceError, RideFileError



@ride_logger
def book_ride(vehicle):
    fare = vehicle.calculate_fare()
    return fare


def save_ride(driver, vtype, distance, fare):
    try:
        f = open("/home/coder/Documents/DSML-LEARNING/Ride_Sharing_System/ride_history.txt", "a")
        f.write("Driver: " + driver + "\n")
        f.write("Vehicle: " + vtype + "\n")
        f.write("Distance: " + str(distance) + " km\n")
        f.write("Fare: Rs. " + str(fare) + "\n")
        f.write("-----------------------------\n")
        f.close()
    except:
        raise RideFileError("Error while writing to file")




try:
  while True:

    vtype = input("\nEnter Vehicle Type: ")
    driver = input("Enter Driver Name: ")
    rating = float(input("Enter Rating: "))
    distance = float(input("Enter Distance: "))


    if rating < 1 or rating > 5:
        raise InvalidRatingError


    if distance < 0:
        raise NegativeDistanceError

    if vtype.lower() == "car":
     v = Car("Car", driver, distance, rating)  
    elif vtype.lower() == "bike":
        v = Bike("Bike", driver, distance, rating) 
    else:
        print("Vehicle type not supported")

        

    fare = book_ride(v)


    
    print("Driver:", driver)
    print("Vehicle:", vtype)
    print("Distance:", distance, "km")
    print("Fare: Rs.", fare)


    save_ride(driver, vtype, distance, fare)
    con = input("\nDo you want to book another ride? (yes/no): \n")
    if con.lower() != "yes":
        print("\nThank you for using our ride sharing service!")
        break

except InvalidRatingError as e:
    print("Invalid Rating Error:", e)
except NegativeDistanceError as e:
    print("Negative Distance Error:", e)
except RideFileError as e:
    print("File Error:", e)
except ValueError as e:
    print("Value Error:", e)
except Exception as e:
    print("Something went wrong:", e)




