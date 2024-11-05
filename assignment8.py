# CREATE DATABASE Assignment8;

# USE Assignment8;

# CREATE TABLE users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     email VARCHAR(100) NOT NULL UNIQUE
# );

# select * from users;

import mysql.connector
from mysql.connector import Error

# Establish the connection
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',            # Your MySQL server host
            user='root',                 # Replace with your MySQL username
            password='sachin_sql3059',   # Replace with your MySQL password
            database='Assignment8'        # Your database name
        )
        print("Connected to MySQL database.")
    except Error as e:
        print(f"Error: {e}")
    return connection

# Execute a generic query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully.")
    except Error as e:
        print(f"Error: {e}")

# CREATE - Add a new user
def add_user(connection, name, email):
    query = "INSERT INTO users (name, email) VALUES (%s, %s);"
    cursor = connection.cursor()
    try:
        cursor.execute(query, (name, email))
        connection.commit()
        print(f"User '{name}' added successfully.")
    except Error as e:
        print(f"Error: {e}")

# READ - Fetch all users
def read_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users;")
    return cursor.fetchall()

# UPDATE - Update user details
def update_user_email(connection, user_id, new_email):
    query = "UPDATE users SET email = %s WHERE id = %s;"
    cursor = connection.cursor()
    try:
        cursor.execute(query, (new_email, user_id))
        connection.commit()
        print(f"User with ID {user_id} updated successfully.")
    except Error as e:
        print(f"Error: {e}")

# DELETE - Remove a user
def delete_user(connection, user_id):
    query = "DELETE FROM users WHERE id = %s;"
    cursor = connection.cursor()
    try:
        cursor.execute(query, (user_id,))
        connection.commit()
        print(f"User with ID {user_id} deleted successfully.")
    except Error as e:
        print(f"Error: {e}")

# Display menu and handle user input
def menu():
    print("\nMenu:")
    print("1. Add User")
    print("2. View Users")
    print("3. Update User Email")
    print("4. Delete User")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

if __name__ == "__main__":
    conn = create_connection()
    if conn:
        while True:
            choice = menu()

            if choice == '1':
                name = input("Enter user name: ")
                email = input("Enter user email: ")
                add_user(conn, name, email)

            elif choice == '2':
                users = read_users(conn)
                print("\nUsers in the database:")
                for user in users:
                    print(user)

            elif choice == '3':
                user_id = int(input("Enter user ID to update: "))
                new_email = input("Enter new email: ")
                update_user_email(conn, user_id, new_email)

            elif choice == '4':
                user_id = int(input("Enter user ID to delete: "))
                delete_user(conn, user_id)

            elif choice == '5':
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please enter a valid option.")

        # Close the connection
        conn.close()


# step2: pip install mysql-connector-python


# Step4: python file_name.py
