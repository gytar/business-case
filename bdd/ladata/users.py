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

users=f"""
INSERT INTO 
    users (`last_name`, `first_name`, `email`, `password`, `phone`, `is_admin`)
VALUES
(
    \"{fk.last_name()}\",
    \"{fk.first_name()}\",
    \"{fk.free_email()}\",
    \"{fk.bothify(text='??#?###??##??##??###?###')}\",
    \"{fk.numerify(text='+33 6 ## ## ## ##')}\",
    {r.randint(0,1)}

);
"""

query(connection, users)