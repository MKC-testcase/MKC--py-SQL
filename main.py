#Program by: Marcus Chan
#Disclaimer: This project was desdigned to extract and process data that come in a csv format
#The types of input this program takes is either as a txt or csv file(csv format)

import csv
import sys
class array:
	colNames = [] # this element should hold strings values of the column names if given
	rowNames = [] # this element should hold strings values of the row names if given
	data = [] #hold the data of the array
	

def determine_names (listoflist):
	colname = []
	rowname = []
	for i in len(listoflist):
		for j in len(i):
			if i == 0:
				#check for column names
				colname.append(listoflist[i][j])
			elif j == 0:
				# check for row names
				rowname.append(listoflist[i][j])
			else:
				continue
	return [colname, rowname]
	
rowData  = []
array = []
print('Please enter the type of input for this program')
print('press 1 and and enter if your file is a .csv file')
print('press 2 and and enter if your file is a .txt file')
type = input("Enter here: ")

# need to check the proper syntax of input for a .csv file reading
# keep in mind that the values checked should be strings I think
if type == "1":
        filename = input('Please enter the filename that you want to have extracted: ')
        with open(filename + '.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter= ',')
                #this prints the output for the .csv file 
                for row in csv_reader:
                        #this should be literally row by row
                        print(row)
elif type == "2":
        filename = input('Please enter the filename that you want to have extracted; ')
        text = open(filename+".txt" , "r")
else:
        print('You have not input a correct value')
        sys.exit() # this works like the return 0 in C++


if type == "1":
        print('reached here')
elif type == "2":
        #the lines below are just prints the contents of the csv file
        lines = text.readlines()
        for txt in lines:
                # the lines below should split the row in the elements 
                row = txt.split(',')
                data.append(row)
                row = []
                print(txt)
                
	

