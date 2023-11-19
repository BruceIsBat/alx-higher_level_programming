#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def list_cities(username, password, database):
    """
    Lists all cities from the specified database.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): MySQL database name

    Returns:
        None: Displays the list of cities

    Raises:
        MySQLdb.Error: If there is an error in MySQL database interaction
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to retrieve all cities
        query = "SELECT * FROM cities ORDER BY cities.id ASC"
        cursor.execute(query)

        # Fetch all the rows
        cities = cursor.fetchall()

        # Display the results
        for city in cities:
            print(city)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))

    finally:
        # Close the cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <username> <password> <database>")
        sys.exit(1)

    # Get MySQL credentials and database name from command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to list cities
    list_cities(username, password, database)
