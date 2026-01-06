# MySQLServer.py
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust host, user, password as needed)
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="yourpassword"   # replace with your root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensure resources are closed properly
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Optional: confirm closure
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()

