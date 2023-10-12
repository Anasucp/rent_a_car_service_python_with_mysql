#library for displaying list in table form
from tabulate import tabulate
import datetime
#list for storing bookings data
bookings = []

#function for adding new booking
def add_booking():
    car_Name = input("Enter Car Name:")
    booking_date_input = input("Enter booking date (YYYY-MM-DD): ")
    booking_date = datetime.datetime.strptime(booking_date_input, "%Y-%m-%d").date()

    booking = {
        "Car Name": car_Name,
        "Booking Date": booking_date
    }

    # add booking in the bookings list
    bookings.append(booking)
    print("Booking added")

# function for displaying or viewing the booking list
def view_bookings():
    if not bookings:
        print("No booking found.")
    else:
        table = tabulate(bookings, headers="keys", tablefmt="grid")
        print("Bookings List:")
        print(table)