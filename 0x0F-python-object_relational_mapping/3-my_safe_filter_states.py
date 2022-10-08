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
    db.execute("SELECT * FROM states WHERE" +
               " CAST(name AS BINARY) LIKE" +
               " %s ORDER BY id ASC;", [argv[4]])
    query_rows = db.fetchall()

    for row in query_rows:
        print(row)

    db.close()
    connection.close()
