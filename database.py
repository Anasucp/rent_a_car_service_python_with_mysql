import mysql.connector

def connect_to_database():

    conn = mysql.connector.connect(
        host="localhost",
        user="ans",
        password="ans",
        database="rent_a_car_service"
    )
    return conn

def execute_query(connection, query, data=None):

    cursor = connection.cursor()
    cursor.execute(query, data)
    return cursor

def commit_and_close(connection):

    connection.commit()
    connection.close()
