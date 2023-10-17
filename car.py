import database
#library for displaying list in table form
from tabulate import tabulate

#list for storing cars data
cars = []

#function for adding new car
def add_car():
    company_name = input("Enter Company Name:")
    model_number = input("Enter Model Number:")
    reg_number = int(input("Enter Registration Number:"))

# SQL statement for inserting a car
    insert_car = "INSERT INTO cars (company_name, model_number, reg_number) VALUES ( %s, %s, %s)"
    car_data = (company_name, model_number, reg_number)

    cursor = database.execute_query(insert_car, car_data)
    database.commit_and_close()

    print("Car added successfully.")
# function for displaying or viewing the car list
def view_cars():
   
    select_cars = "SELECT * FROM cars"


    cursor = database.execute_query(select_cars)

    cars = cursor.fetchall()

    if not cars:
        print("No Cars found.")
    else:
        # Convert the car data to a list of lists
        car_data = [list(car) for car in cars]

        headers = ["ID", "Company_Name", "Model_Number", "REG_Number", "Created","updated"]

        # tabulate to display the cars in a table format
        table = tabulate(car_data, headers, tablefmt="grid")
        print("Car List:")
        print(table)

    # Close the database connection
    database.commit_and_close()