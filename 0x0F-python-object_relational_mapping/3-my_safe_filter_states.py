#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa with a
given name and is safe from MySQL injections
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    argument = argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3],
                           charset="utf8")
    cur = conn.cursor()

    # HERE I have to know SQL to grab all states in my database
    cur.execute("SELECT * FROM states where name LIKE %s ORDER BY id ASC;",
                (argument, ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
