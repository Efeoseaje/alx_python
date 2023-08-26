""" script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb as DB
import sys

if __name__ == "__main__":
    # Create a database connection
    db_connect = DB.connect(
        host='localhost',
        port=3306,
        user=sys.argv[0],
        passwd=sys.argv[1],
        db=sys.argv[2]
    )

    # Create a cursor to enable SQL queries
    db_cursor = db_connect.cursor()

    # Execute SQL code
    db_cursor.execute("SELECT * FROM states")

    # Fetch data from cursor object
    states = db_cursor.fetchall()

    # Access list of states
    for state in states:
        print(state)
