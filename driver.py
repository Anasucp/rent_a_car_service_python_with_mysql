import database
#library for displaying list in table form
from tabulate import tabulate

#list for storing drivers data
drivers = []

#function for adding new driver
def add_driver():
    name = input("Enter your Name:")
    age = int(input("Enter your age:"))
    while True:
        cnic_no = input("Enter your 13 Digit CNIC Number:" )
        if len(cnic_no)==13:
            break
        else:
            print("Invalid Cnic")
    while True:
        license_no = input("Enter your License number:")
        if len(license_no)==13:
            break
        else:
            print("Invalid license_no")
    price_per_day=int (input("Eneter the per day price of Driver:"))

# SQL statement for inserting a car
    insert_driver = "INSERT INTO drivers (name,age,cnic_no,license_no,price_per_day) VALUES ( %s, %s,%s,%s,%s)"
    driver_data = (name,age,cnic_no,license_no,price_per_day)

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

        headers = ["ID","Name","Age","Cnic","license_number","Driver pay/Day", "Created","updated"]

        # tabulate to display the Drivers in a table format
        table = tabulate(driver_data, headers, tablefmt="grid")
        print("Drivers List:")
        print(table)

    # Close the database connection
    database.commit_and_close()

def delete_driver():

    view_drivers()

    driver_delete_id = int(input("Eneter id to delete the driver:"))

    select_driver_delete = "DELETE FROM drivers WHERE id = %s"

    cursor = database.execute_query(select_driver_delete,(driver_delete_id,))
    database.commit_and_close()
    print("driver deleted successfully.")


def update_driver():

    view_drivers()

    driver_update_id = int(input("Enter Driver ID to Update:"))

    update_name = input("Enter your Name:")
    update_age = int(input("Enter your age:"))
    while True:
        update_cnic_no = input("Enter your 13 Digit CNIC Number:" )
        if len(update_cnic_no)==13:
            break
        else:
            print("Invalid Cnic")
    while True:
        update_license_no = input("Enter your License number:")
        if len(update_license_no)==13:
            break
        else:
            print("Invalid license_no")
    update_price_per_day=int (input("Eneter the per day price of Driver:"))



    select_driver_update = "UPDATE drivers SET name=%s,age=%s,cnic_no=%s,license_no=%s,price_per_day=%s WHERE id=%s"
    update_data = (update_name,update_age,update_cnic_no,update_license_no,update_price_per_day,driver_update_id)
    cursor = database.execute_query(select_driver_update,update_data)

    database.commit_and_close()


    print("Driver Data update successfully.")


    