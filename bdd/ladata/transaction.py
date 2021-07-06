from faker import Faker
import random as r
import mysql.connector
from mysql.connector import Error

fk = Faker()


def create_conn(hostname, username, passwd):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=passwd,
            database="PiCom"
        )
    except Error as e:
        print(f"the error {e} occured")
    return connection


def query(connection, query):
    cursor = connection.cursor()
    try:
        res = cursor.execute(query)
        connection.commit()
        print(cursor.rowcount)
        print("Query executed!")
    except Error as e:
        print(f"The error '{e}' occurred")
    

connection = create_conn("localhost", "root", "phplord")

transaction=f"""
INSERT INTO 
    transactions (name, price)
VALUES 
(
    \"{fk.text(max_nb_chars=40)}\",
    {round(r.uniform(1.99, 200), 2)}
);
"""

# print(transaction)
query(connection, transaction)