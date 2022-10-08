#!/usr/bin/python3
'''database connection script'''
from sys import argv
import MySQLdb

'''connection Setup'''
if __name__ == '__main__':
    connection = MySQLdb.connect(
        host="localhost",
        port=3306, user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    db = connection.cursor()
    db.execute("SELECT cities.name FROM cities" +
               " INNER JOIN states ON cities.state_id = states.id" +
               " WHERE states.name LIKE %s;", [argv[4]])
    query_rows = db.fetchall()
    print(', '.join(map(lambda x: x[0], query_rows)))

    db.close()
    connection.close()
