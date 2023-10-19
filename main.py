from client import add_client,view_clients,delete_client
from car  import add_car,view_cars,delete_car
from driver import add_driver,view_drivers,delete_driver
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
    print("10.Update or Delete data.")
    print("11.Exit")

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
        def update_del_menu():
            print("1.Update client")
            print("2.Delete client")
            print("3.Update Car")
            print("4.Delete Car")
            print("5.Update Driver")
            print("6.Delete Driver")
            print("7.Get back to main menu.")
        while True:
            clear_screen()
            update_del_menu()
            
            choice_2 = input("Enter your choice:")

            if choice_2 == "1":
                clear_screen()
            elif choice_2 == "2":
                clear_screen()
                delete_client()
            elif choice_2 == "3":
                clear_screen()
            elif choice_2 == "4":
                clear_screen()
                delete_car()
            elif choice_2 == "5":
                clear_screen()
            elif choice_2 == "6":
                clear_screen()
                delete_driver()
            elif choice_2 == "7":
                clear_screen()
                break

    elif choice == "11":
        clear_screen()
        print("Thanks for choosing Our reant a car service :)")
        break


