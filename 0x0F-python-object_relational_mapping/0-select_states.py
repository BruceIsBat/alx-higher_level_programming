#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys


db = MySQLdb.connect(host="localhost",
                                port=3306,
                                user=sys.argv[1],
                                password=sys.argv[2],
                                database=sys.argv[3])
try:
    db = MySQLdb.connect(host="localhost",
                                port=3306,
                                user=sys.argv[1],
                                password=sys.argv[2],
                                database=sys.argv[3])
    cursor = db.cursor()

    cursor.execute("""SELECT * FROM states ORDER BY states.id ASC""")

    states = cursor.fetchall()

    for state in states:
        print((int(state[0].decode('utf-8')), state[1].decode('utf-8')))
except MySQLdb.Error as e:
    print("MySQL Error {}: {}".format(e.args[1], e.args[3]))
finally:
    if db:
        db.close()


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
