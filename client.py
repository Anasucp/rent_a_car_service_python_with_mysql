import database
#library for displaying list in table form
from tabulate import tabulate

#list for storing clients data
clients = []


#function for adding new client
def add_client():
    name = input("Enter your Name:")
    age = int(input("Enter your age:"))
    while True:
        cnic = input("Enter your 13 Digit CNIC Number:")
        if len(cnic)==13:
            break
        else:
            print("Invalid Cnic")
    while True:
        phone_number =input("Enter your phone number:")
        if len(phone_number)==11:
            break
        else:
            print("Enter Valid phone_number")

    # SQL statement for inserting a client
    insert_client = "INSERT INTO clients (name, age, cnic, phone_number) VALUES (%s, %s, %s, %s)"
    client_data = (name, age, cnic, phone_number)

    cursor = database.execute_query(insert_client, client_data)
    database.commit_and_close()

    print("Client added successfully.")

   


def view_clients():

    select_clients = "SELECT * FROM clients"


    cursor = database.execute_query(select_clients)

    clients = cursor.fetchall()

    if not clients:
        print("No Clients found.")
    else:
        # Convert the client data to a list of lists
        client_data = [list(client) for client in clients]

        headers = ["Client ID", "Name", "Age", "CNIC Number", "Phone Number","Created","updated"]

        # tabulate to display the clients in a table format
        table = tabulate(client_data, headers, tablefmt="grid")
        print("Client List:")
        print(table)

    # Close the database connection
    database.commit_and_close()