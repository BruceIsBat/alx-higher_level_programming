#!/usr/bin/python3
"""Script that lists all states with a name starting with N from the database
hbtn_0e_0_usa
"""
import MySQLdb
import sys


def list_states_starting_with_n(username, password, database):
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

        # Execute the SQL query to retrieve states starting with N
        query = """SELECT *
        FROM states
        WHERE name LIKE 'N%'
        ORDER BY states.id ASC"""
        cursor.execute(query)

        # Fetch all the rows
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

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
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL credentials from command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to list states starting with N
    list_states_starting_with_n(username, password, database)
