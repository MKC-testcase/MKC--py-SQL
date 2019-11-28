#!/usr/bin/env python
import MySQLdb

#This version is tested now the mariadb connection works now
#however this only works with python 2.7 version, mariadb not supported with
#python 3
# Open database connection
db = MySQLdb.connect("localhost","administrator","password","temps" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
#the execute command runs a sql command, format has to be in a string
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()
