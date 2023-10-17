import database
import datetime
import car
import client 
import driver
#library for displaying list in table form
from tabulate import tabulate



# Function to fetch and display available cars
def add_booking():

    client.view_clients()
     # Prompt the user for client ID
    client_id = int(input("Enter Client ID: "))

    car.view_cars()
    # Prompt the user for car ID
    car_id = int(input("Enter Car ID: "))

    driver_option=input("Do you want driver Yes/No:")
    driver_id=None

    if driver_option=="Yes":
        driver.view_drivers()
        driver_id=input("Enter the driver id:")

    # Prompt the user for booking date
    booking_date = input("Enter Booking Date (YYYY-MM-DD): ")

    # Define the SQL statement for inserting a booking
    insert_booking = "INSERT INTO bookings (client_id, car_id,driver_id, booking_date) VALUES (%s, %s, %s)"
    booking_data = (client_id, car_id,driver_id, booking_date)

    # Execute the SQL statement to insert the booking
    cursor = database.execute_query(insert_booking, booking_data)

    # Commit and close the connection
    database.commit_and_close()

    print("Booking added successfully.")


# function for displaying or viewing the booking list
def view_bookings():
    select_bookings = "SELECT * FROM bookings"

    # Execute the query to retrieve bookings with client and car details
    cursor = database.execute_query( select_bookings)

    # Fetch all the bookings with client and car details
    bookings = cursor.fetchall()

    if not bookings:
        print("No Bookings found.")
    else:
        # Convert the booking data to a list of lists
        booking_data = [list(booking) for booking in bookings]

        headers = ["Booking ID", "Client ID","Car ID","Driver ID", "Booking Date"]

        # Use tabulate to display the bookings in a tabulated format
        booking_table = tabulate(booking_data, headers, tablefmt="grid")
        print("Booking List with Client and Car Details:")
        print(booking_table)

    # Close the database connection
    database.commit_and_close()