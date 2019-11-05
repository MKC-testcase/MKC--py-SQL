#By: Marcus Chan
#The goal for this program will be to collect the data from the github account
#If possible then also send the data to the mysql server
# eventually will have to incorporate threading into the program for optimization
# but try to get a working version first single threaded

import git
import time
import os
import threading

#The command below makes the gitcmd variable act like the input line for the git cmd
gitcmd = git.cmd.Git(home/pi/Desktop/python/MKC--py-SQL)
#variable below will be to keep track of the time
localtime = time.asctime(time.localtime(time.time()))
dataCols = []

def Collect_data(interger):
    #extracts data from github then opens the dataEntry.txt file from the current folder
    gitcmd.pull
    location = os.getcwd() + "\\dataEntry.txt"
    # confirm that each line will be a data entry
    data = open(location, "r")
    for lines in data.readline():
        Data_Prepare()
    

def Data_Prepare():
    #This function seperates the single string


    Send(dataCols)


def Send(dataCols):
    #this function will send the data into the mysql server
    # the try and except are for when the cols in the dataCols table don't match the size
    # parameters in the sql table
    for element in dataCols:
        print("reached send")
    #try
        
    #except: 

#Counters(test) to run for 1 day for every hour
counterhrs = 24
x = 0
backup = 100
# the way it will be formatted will be it will start the 
while x < counterhrs
    if localtime == localtime.replace(hour=x, minute = 0, second = 0, microsecond = 0)
        #this pull request should happen every hour to check for updates
        Collect_data(x)
        x = x++
    else
        if localtime == localtime.replace(minute = %5, second = 0, microsecond = 0)
        continue
