#library for displaying list in table form
from tabulate import tabulate

#list for storing cars data
cars = []

#function for adding new car
def add_car():
    company_name = input("Enter Company Name:")
    model_number = input("Enter Model Number:")
    reg_number = int(input("Enter Registration Number:"))

    car = {
        "Company Name": company_name,
        "Model Number": model_number,
        "Reg Number" : reg_number
    }

    # add car in the cars list
    cars.append(car)
    print("car added")

# function for displaying or viewing the car list
def view_cars():
    if not cars:
        print("No cars found.")
    else:
        table = tabulate(cars, headers="keys", tablefmt="grid")
        print("cars List:")
        print(table)