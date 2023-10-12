from client import add_client, view_clients 
from car  import add_car, view_cars
from driver import add_driver, view_drivers
from booking import add_booking, view_bookings
import database
import mysql.connector


conn = database.connect_to_database()

database.commit_and_close(conn)

# main menu function
def main_menu():
    print("/------------Welcome to Rent a Car service------------/")





    print("Main menu.")
    print("1.Add client")
    print("2.view client")
    print("3.Add Car")
    print("4.view Car")
    print("5.Add Driver")
    print("6.view Driver")
    print("7.Make Booking")
    print("8.view Bookings")
    print("9.Exit")

while True:
    main_menu()

    choice = input("Enter Your Choice:")

    if choice == "1":
        add_client()
    elif choice == "2":
        view_clients()
    elif choice == "3":
    	add_car()
    elif choice == "4":
    	view_cars()
    elif choice == "5":
    	add_driver()
    elif choice == "6":
    	view_drivers()
    if choice == "7":
        add_booking()
    elif choice == "8":
        view_bookings()
    elif choice == "9":
    	print("Thanks for choosing Our reant a car service :)")
    	break
