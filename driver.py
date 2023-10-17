import database
#library for displaying list in table form
from tabulate import tabulate

#list for storing drivers data
drivers = []

#function for adding new driver
def add_driver():
    name = input("Enter your Name:")
    age = int(input("Enter your age:"))
    cnic_no = int(input("Enter your CNIC Number:"))
    license_no = int(input("Enter your License number:"))

# SQL statement for inserting a car
    insert_driver = "INSERT INTO drivers (name,age,cnic_no,license_no) VALUES ( %s, %s,%s,%s)"
    driver_data = (name,age,cnic_no,license_no)

    cursor = database.execute_query(insert_driver, driver_data)
    database.commit_and_close()

    print("Driver added successfully.")

# function for displaying or viewing the driver list
def view_drivers():
    
    select_drivers = "SELECT * FROM drivers"


    cursor = database.execute_query(select_drivers)

    drivers = cursor.fetchall()

    if not drivers:
        print("No Drivers found.")
    else:
        # Convert the driver data to a list of lists
        driver_data = [list(driver) for driver in drivers]

        headers = ["ID","Name","Age","Cnic","license_number", "Created","updated"]

        # tabulate to display the Drivers in a table format
        table = tabulate(driver_data, headers, tablefmt="grid")
        print("Drivers List:")
        print(table)

    # Close the database connection
    database.commit_and_close()