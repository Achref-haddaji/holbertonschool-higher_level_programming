#!/usr/bin/python3
""" states module """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """connect to the database"""
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    """ i didnt declare the *host and the *port arguments
    cuz they will be ther bye default """
cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id")
result = cursor.fetchall()
for i in result:
    """ loop the states"""
    print(i)
cursor.close()
""" close the cursor"""
db.close()
""" close the database"""
