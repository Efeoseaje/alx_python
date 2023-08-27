""" script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa.
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

    searched_city = sys.argv[4]

    db_cursor = db_connect.cursor()

    query = (
        "SELECT cities.name \
        FROM cities \
        INNER JOIN states ON states.id = cities.state_id \
        WHERE states.name = %s \
        ORDER BY cities.id;"
    )

    db_cursor.execute(query, (searched_city,))

    cities = db_cursor.fetchall()

    city_list = [city for city in cities]
    print(", ".join(city_list))
