#!/usr/bin/python3

import MySQLdb
from sys import argv

conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                            passwd=argv[2], db=argv[3], charset="utf8")
cur = conn.cursor()
# HERE I have to know SQL to grab all states in my database
cur.execute("SELECT * FROM states where name regexp '^N.' ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
