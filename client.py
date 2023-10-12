import database
#library for displaying list in table form
from tabulate import tabulate
import mysql.connector

#list for storing clients data
clients = []


#function for adding new client
def add_client():
    name = input("Enter your Name:")
    age = int(input("Enter your age:"))
    cnic = int(input("Enter your CNIC Number:"))
    phone_number = int(input("Enter your phone number:"))

    # Connect to the database
    conn = database.connect_to_database()

    # SQL statement for inserting a client
    insert_client = "INSERT INTO clients (name, age, cnic, phone_number) VALUES (%s, %s, %s, %s)"
    client_data = (name, age, cnic, phone_number)

    cursor = database.execute_query(conn, insert_client, client_data)

    database.commit_and_close(conn)

    print("Client added successfully.")

   


def view_clients():
    conn = database.connect_to_database()

    select_clients = "SELECT * FROM clients"


    cursor = database.execute_query(conn, select_clients)

    clients = cursor.fetchall()

    if not clients:
        print("No Clients found.")
    else:
        # Convert the client data to a list of lists
        client_data = [list(client) for client in clients]

        headers = ["Client ID", "Name", "Age", "CNIC Number", "Phone Number"]

        # tabulate to display the clients in a table format
        table = tabulate(client_data, headers, tablefmt="grid")
        print("Client List:")
        print(table)

    # Close the database connection
    database.commit_and_close(conn)