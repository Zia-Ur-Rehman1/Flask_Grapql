import os
import pg8000.dbapi
from pg8000.dbapi import DatabaseError

connection = None
user = os.getenv("PGUSER")
password = os.getenv("PGPASSWORD")
host = os.getenv("PGHOST")
port = os.getenv("PGPORT")
database = os.getenv("PGDATABASE")


def create_connection():
    global connection, user, password

    try:
        connection = pg8000.dbapi.connect(
            user=user, password=password, host=host, port=port, database=database
        )
        return connection
    except DatabaseError as e:
        print(f"An error occurred: {e}")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except DatabaseError as e:
        connection.rollback()
        print(f"An error occurred: {e}")


def execute_read_query(connection, query, params=()):
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        records = cursor.fetchall()

        keys = [k[0] for k in cursor.description]
        return [dict(zip(keys, row)) for row in records]
    except DatabaseError as e:
        print(f"An error occurred: {e}")
