# Import Library

import psycopg2
from psycopg2 import Error


def getConnection():
    connection = psycopg2.connect(
        host='localhost', user='postgres', password='password', database='postgres')
    return connection


def closeConnection(connection):
    connection.close()
    print("Connection is Closed")


def getCustomer(customer_id):
    try:
        connection = getConnection()
        cursor = connection.cursor()

        query = "SELECT * FROM CUSTOMER WHERE customer_id = %s"
        cursor.execute(query, (customer_id,))
        records = cursor.fetchall()
        print("Printing Records")
        for row in records:
            print("Customer ID", row[0])
            print("Store ID", row[1])
            print("First Name", row[2])
            print("Last Name", row[3])
            print("Email", row[4])
            print("Address ID", row[5])
            print("Active Status", row[6])
            print("Create Date", row[7])
            print("Last Update", row[8])
            print("Active", row[9], '\n')
        closeConnection(connection)
    except Error as e:
        print("Error: Reading Record")


getCustomer(34)
