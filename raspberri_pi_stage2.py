#By: Marcus Chan
#The goal for this program will be to collect the data from the github account
#If possible then also send the data to the mysql server
# eventually will have to incorporate threading into the program for optimization
# but try to get a working version first single threaded

#!/usr/bin/env python
import MySQLdb
import yfinance as yf

ticker_names = []

#This version is tested now the mariadb connection works now
#however this only works with python 2.7 version, mariadb not supported with
#python 3
# Open database connection
db = MySQLdb.connect("localhost","administrator","password","temps" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

def enterData(entry,n)
    ticker_names.append(entry)
    ticker_names[n] = yf.Ticker(entry) #sets the ticker_names element to the data collected from yfinance
    
    

def collectData()
    # this function will show collect the data from yahoo finance
    # will have to collect the company names in a text file
    companies = open('dataEntry.txt', 'r')
    n=0
    for entry in companies
        try:
            enterData(entry, n)
            n=n+1
        except:
            print "the company doesn't exist and we cannot enter its data"
            
    



# execute SQL query using execute() method.
#the execute command runs a sql command, format has to be in a string
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()

