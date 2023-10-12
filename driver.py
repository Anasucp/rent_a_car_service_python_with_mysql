#library for displaying list in table form
from tabulate import tabulate

#list for storing drivers data
drivers = []

#function for adding new driver
def add_driver():
    name = input("Enter your Name:")
    age = int(input("Enter your age:"))
    cnic = int(input("Enter your CNIC Number:"))
    phone_number = int(input("Enter your phone number:"))
    license_number = int(input("Enter your License number:"))

    driver = {
        "Name": name,
        "Age": age,
        "Cnic": cnic,
        "phone_number": phone_number,
        "license_number": license_number
    }

    # add driver in the drivers list
    drivers.append(driver)
    print("driver added")

# function for displaying or viewing the driver list
def view_drivers():
    if not drivers:
        print("No Drivers found.")
    else:
        table = tabulate(drivers, headers="keys", tablefmt="grid")
        print("Drivers List:")
        print(table)