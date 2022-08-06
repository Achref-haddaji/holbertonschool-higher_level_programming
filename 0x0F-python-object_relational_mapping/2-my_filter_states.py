#!/usr/bin/python3
""" states module"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ connect to the database"""
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    )
    """ i didnt assgin the *host value and the *port value in the arguments
    cuz they will be ther bye default """
cursor = db.cursor()
cursor.execute("SELECT * FROM states".format(argv[4]))
result = cursor.fetchall()
for i in result:
    if i[1] == argv[4]:
        """ print the once that starts with *N """
        print(i)
cursor.close()
""" close the cursor"""
db.close()
""" close the database"""
