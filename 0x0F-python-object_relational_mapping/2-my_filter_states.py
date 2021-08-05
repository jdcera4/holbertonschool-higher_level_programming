#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa with a
given name and is safe from MySQL injections
"""
import MySQLdb
from sys import argv

argument = argv[4]
conn = MySQLdb.connect(host="localhost", port=3306, user="root",
                            passwd="root", db="hbtn_0e_0_usa", charset="utf8")
cur = conn.cursor()

# HERE I have to know SQL to grab all states in my database
cur.execute("SELECT * FROM states where name = %s ORDER BY id ASC;",(argument, ))
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
