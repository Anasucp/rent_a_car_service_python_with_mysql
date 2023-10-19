import database
import booking

def calculate_bill():
    booking.view_bookings()

    # Prompt the user to enter a booking ID
    booking_id = int(input("Enter Booking ID to calculate the bill: "))

    # Query to retrieve booking details
    select_booking = "SELECT car_id, driver_id, booking_date_start, booking_date_end FROM bookings WHERE booking_id = %s"
    cursor = database.execute_query(select_booking, (booking_id,))
    booking_info = cursor.fetchone()

    if booking_info:
        # Extract booking details
        car_id, driver_id, booking_date_start, booking_date_end = booking_info

        # Calculate the number of days
        num_days = (booking_date_end - booking_date_start).days

        # Query  car price
        select_car_price = "SELECT price_per_day FROM cars WHERE id = %s"
        cursor = database.execute_query(select_car_price, (car_id,))
        car_price = cursor.fetchone()[0]
        print("Car rent per day:",car_price)

        # Query driver price (if driver is selected)
        if driver_id:
            select_driver_price = "SELECT price_per_day FROM drivers WHERE id = %s"
            cursor = database.execute_query(select_driver_price, (driver_id,))
            driver_price = cursor.fetchone()[0]
            print("Driver pay per day:",driver_price)
        else:
            driver_price = None

        if driver_price is not None:
            total_cost = (car_price + driver_price) * num_days
        else:
            total_cost = car_price * num_days

        # Display the total bill
        print("Total Bill for Booking ID {}: ${:.2f}".format(booking_id, total_cost))

        # Insert billing data into the 'billings' table
        insert_billing = "INSERT INTO billings (booking_id, total_cost) VALUES (%s, %s)"
        billing_data = (booking_id, total_cost)
        cursor = database.execute_query(insert_billing, billing_data)

        # Commit and close the connection
        database.commit_and_close()
    else:
        print("Booking not found.")
