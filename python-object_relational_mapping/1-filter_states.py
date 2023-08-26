""" script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb as DB
import sys

if __name__ == "__main__":
    # Create a database connection
    db_connect = DB.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor to enable SQL queries
    db_cursor = db_connect.cursor()

    # Execute SQL code
    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE %N \
            ORDER BY states.id")

    # Fetch data from cursor object
    states_with_N = db_cursor.fetchall()

    # Access list of states starting with N
    for state in states_with_N:
        print(state)
