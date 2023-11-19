#!/usr/bin/python3
"""Script that displays all values in the states table where name matches the provided argument (safe from MySQL injection)
"""
import MySQLdb
import sys

def search_states(username, password, database, search_name):
    """
    Search for states in the specified database whose names match the provided search term (safe from MySQL injection).

    Args:
        username (str): MySQL username
        password (str): MySQL password
        database (str): MySQL database name
        search_name (str): The state name to search for

    Returns:
        None: Displays the search results

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

        # Use parameterized query to prevent MySQL injection
        query = """SELECT *
        FROM states
        WHERE name
        LIKE %s
        ORDER BY states.id ASC"""
        cursor.execute(query, (search_name,))

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
    if len(sys.argv) != 5:
        print(f"""Usage: {sys.argv[0]} <username>
                 <password> <database> <search_name>""")
        sys.exit(1)

    # Get MySQL credentials and search name from command line arguments
    username, password = sys.argv[1], sys.argv[2]
    database, search_name = sys.argv[3], sys.argv[4]

    # Call the function to search for states
    search_states(username, password, database, search_name)
