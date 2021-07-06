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
        if connection != None:
            print("connection to DB ok ! yay")
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

adverts=f"""
INSERT INTO 
    adverts (name, description, picture, date_ad, duration, user_id)
VALUES 
(
    \"{fk.text(max_nb_chars=20)}\", 
    \"{fk.paragraph()}\",
    \"{fk.image_url()}\",
    \"{fk.date_this_decade()}\",
    {r.randint(1, 15)},
    {r.randint(850, 1000)}
);
"""

transaction=f""""
INSERT INTO 
    transactions (name, price)
VALUES 
(
    \"{fk.text(max_nb_chars=40)}\",
    {round(r.uniform(1.99, 200), 2)}
);
"""

area=f"""
INSERT INTO 
    area (name, price)
VALUES 
(
    \"{fk.text(max_nb_chars=40)}\",
    {round(r.uniform(1.99, 200), 2)}
);
"""

screen=f"""
INSERT INTO 
    screen (name, ip_addr, area_id)
VALUES
(
    \"{fk.text(max_nb_chars=30)}\",
    \"{fk.ipv4()}\",
    {r.randint(1, 15)}
);
"""

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
connection = create_conn("localhost", "root", "phplord")



query(connection, users)
query(connection, area)
query(connection, screen)
query(connection, transaction)
query(connection, adverts)