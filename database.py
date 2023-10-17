import mysql.connector
from config.db import conn

def execute_query(query, data=None):

    cursor = conn.cursor()
    cursor.execute(query, data)
    return cursor

def commit_and_close():

    conn.commit()
    conn.close()


# DRY => Don't Repeat Yourself