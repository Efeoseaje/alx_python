""" script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb as DB
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    # Create a database connection
    db_connect = DB.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    searched_state = sys.argv[4]

    db_cursor = db_connect.cursor()

    query = ("SELECT * FROM states WHERE name LIKE BINARY %s \
            ORDER BY states.id")

    db_cursor.execute(query, (searched_state,))

    states = db_cursor.fetchall()

    for state in states:
        print(state)
