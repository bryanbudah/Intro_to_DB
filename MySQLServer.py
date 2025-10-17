#!/usr/bin/env python3
"""
MySQLServer.py

A simple Python script to create a MySQL database named 'alx_book_store'.
If the database already exists, the script will not fail.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    """Creates the 'alx_book_store' database if it doesn't already exist."""
    connection = None
    try:
        # Connect to MySQL server (update credentials as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # Replace with your actual MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            # Optional message (useful for debugging)
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
