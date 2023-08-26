""" script that lists all cities from the database hbtn_0e_0_usa """

import MySQLdb as DB
import sys

if __name__ == "__main__":
    db_connect = DB.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT cities.id, cities.name, states.name \
        FROM cities \
        LEFT JOIN states ON states.id = cities.state_id \
        ORDER BY cities.id;"
    )

    cities = db_cursor.fetchall()

    for city in cities:
        print(city)
