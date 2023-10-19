import database
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

    driver_option = input("Do you want a driver (Yes/No): ")
    driver_id = None

    if driver_option.lower() == "yes":
        driver.view_drivers()
        driver_id = int(input("Enter the driver id: "))
    else:
        driver_id= None


    # Prompt the user for booking date
    booking_date_start = input("Enter Starting Booking Date (YYYY-MM-DD): ")
    booking_date_end = input("Enter End Date of booking (YYYY-MM-DD): ")

    # Define the SQL statement for inserting a booking
    insert_booking = "INSERT INTO bookings (client_id, car_id, driver_id, booking_date_start, booking_date_end) VALUES (%s, %s, %s, %s, %s)"
    booking_data = (client_id, car_id, driver_id, booking_date_start, booking_date_end)

    # Execute the SQL statement to insert the booking
    cursor = database.execute_query(insert_booking, booking_data)

    # Commit and close the connection
    database.commit_and_close()

    print("Booking added successfully.")

# function for displaying or viewing the booking list
def view_bookings():
    select_bookings = """
     SELECT 
        bookings.booking_id, 
        CASE WHEN bookings.driver_id IS NOT NULL THEN drivers.name ELSE 'No driver' END AS driver_name,
        CASE WHEN bookings.driver_id IS NOT NULL THEN drivers.cnic_no ELSE 'No driver' END AS driver_cnic,
        clients.name AS client_name, 
        clients.cnic AS client_cnic,
        cars.company_name AS car_company,
        cars.reg_number AS car_reg_number,
        bookings.booking_date_start,
        bookings.booking_date_end
    FROM bookings
    INNER JOIN clients ON bookings.client_id = clients.id
    INNER JOIN cars ON bookings.car_id = cars.id
    LEFT JOIN drivers ON bookings.driver_id = drivers.id
    """

    # Execute the query to retrieve bookings with client and car details
    cursor = database.execute_query(select_bookings)

    # Fetch all the bookings with client and car details
    bookings = cursor.fetchall()

    if not bookings:
        print("No Bookings found.")
    else:
        # Convert the booking data to a list of lists
        booking_data = [list(booking) for booking in bookings]

        headers = ["Booking ID", "Driver Name", "Driver CNIC", "Client Name", "Client CNIC", "Car Company", "Car Reg Number", "Booking Date Start", "Booking Date End", "Created", "Updated"]

        # Use tabulate to display the bookings in a tabulated format
        booking_table = tabulate(booking_data, headers, tablefmt="grid")
        print("Booking List with Client and Car Details:")
        print(booking_table)

    # Close the database connection
    database.commit_and_close()
