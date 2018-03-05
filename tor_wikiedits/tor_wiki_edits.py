import csv
import os
from datetime import *
directory = 'C:/Users/Red Viper/Downloads/exit-list-2010-02/22'
dict1 = {}
new_data = []
with open ('tor_exit_list_20170128.csv', 'r') as file1, open('tor_wikipedia_edits-20180215.tsv', 'r') as file2, open('tor_wikipedia_edits-20180218.tsv',  'w') as file3:
	for line in file1:
		li = line.split(",")
		ip = li[0]
		date = li[1]
		dict1[ip] = date
	for line in file2:
		li = line.split()
		ip = li[1]

		revision_date = li[2]
		try:
			revision_date = datetime.strptime(revision_date, '%Y-%m-%d')
		except:
			print("can't convert to datetime")
		#print(revision_date)
		published_date = dict1.get(ip)
		try:
			published_date = published_date.split()
			published_date = datetime.strptime(published_date[0], '%Y-%m-%d')
		except:
			print("can't convert to datetime")
		try:
			delta = revision_date - published_date
			li[2] = li[2] + ' ' + li[3]
			li[3] = li[4]
			li[4] = delta.days
		except:
			li.append('DaysSincePublished')
		new_data.append(li)
	#print(new_data)
	for item in new_data:
		
		string = ""
		for x in range(4):
			string += str(item[x]) + '\t'
		string += str(item[4]) + '\n'
		file3.write(string)

