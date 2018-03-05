import sys
import csv
import os
from datetime import *
#directory = 'C:/Users/Red Viper/Downloads/exit-list-2010-02/22'
tup = {}
#parse all the files
for filename1 in os.listdir(sys.argv[1]):
	#go through each line of the tor exist list and convert data into a table
	with open(filename1, 'r') as file1:
		days_active = 1
		number_of_nodes = 1
		exit_address = None
		exit_node = None
		exit_node_list = []
		published = None
		last_status = None
		for line in file1:
			file_name = filename1
			li = line.split()
			if (li != [] and li[0] == 'ExitNode'):
				exit_node = li[1]
			if (li != [] and li[0] == 'Published'):
				published = li[1]
				published+= " " + li[2]
			if (li != [] and li[0] == 'LastStatus'):
				last_status = li[1]
				last_status += " " + li[2]
			if (li != [] and li[0] == 'ExitAddress' and exit_node != None):
				exit_address = li[1]
			
			if (exit_address !=None and exit_node != None and published != None and last_status != None):
				#if the exit address is new, create a new record
				if exit_address not in tup:
					exit_node_list.append(exit_node)
					tup[exit_address] = [published, last_status, days_active, exit_node_list, number_of_nodes, file_name]
				#if the exit address already exists, update the record to relfect the last status
				else:
					new_date = last_status.split(" ")
					new_date = datetime.strptime(new_date[0], '%Y-%m-%d')
					#new_last_status = datetime.strptime(last_status,'%Y-%m-%d %H:%M:%S')
					array = tup.get(exit_address)
					old_date = array[1].split(" ")
					old_date = datetime.strptime(old_date[0], '%Y-%m-%d')
					if (new_date - old_date>= timedelta(days=1)):
						array[2] = int(array[2])+ 1
					if (exit_node not in array[3]):
						array[3].append(exit_node)
						array[4] = int(array[4])+ 1
					array[1] = last_status
					tup[exit_address] = array
				exit_node = None
				exit_address = None
				published = None
				last_status = None
				days_active = 1
				number_of_nodes = 1 
				exit_node_list = []
				
	#except:
	#	print("Cannot open this file: " + filename1)
	#	continue
#write the table into a file
filename2 = "data.csv"
with open(filename2, 'w') as file2:
	writer = csv.writer(file2)
	mydata = [['ExitAddress', 'Published', 'LastStatus', 'DaysActive', 'ExitAddress', 'NumberOfExitNodes', 'FileName']]
	writer.writerow(mydata)
	for key, value in tup.items():
		string = ""
		for x in range(len(value[3])-1):
			string += value[3][x] + ", "
		string += value[3][len(value[3])-1]
		data = [key, value[0], value[1],  value[2], string, value[4], value[5]]
		writer.writerow(data)
	

			
