from client import add_client,view_clients  
from car  import add_car,view_cars
from driver import add_driver,view_drivers
from booking import add_booking,view_bookings
from billing import calculate_bill
import subprocess

# Function to clear the terminal screen on Linux
def clear_screen():
    subprocess.run(["clear"])


# main menu function
def main_menu():
    print("/------------Welcome to Rent a Car service------------/")
    print("Main menu.")
    print("1.Add client")
    print("2.View client")
    print("3.Add Car")
    print("4.View Car")
    print("5.Add Driver")
    print("6.View Driver")
    print("7.Make Booking")
    print("8.View Bookings")
    print("9.View Total Bill")
    print("10.Exit")

while True:
    main_menu()

    choice = input("Enter Your Choice:")

    if choice == "1":
        clear_screen()
        add_client()
    elif choice == "2":
        clear_screen()
        view_clients()
    elif choice == "3":
        clear_screen()
        add_car()
    elif choice == "4":
        clear_screen()
        view_cars()
    elif choice == "5":
        clear_screen()
        add_driver()
    elif choice == "6":
        clear_screen()
        view_drivers()
    elif choice == "7":
        clear_screen()
        add_booking()
    elif choice == "8":
        clear_screen()
        view_bookings()

    elif choice == "9":
        clear_screen()
        calculate_bill()

    elif choice == "10":
        clear_screen()
        print("Thanks for choosing Our reant a car service :)")
        break


