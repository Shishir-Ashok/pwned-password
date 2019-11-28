#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:21:32 2019

@author: Shishir Ashok
"""


import hashlib
import getpass
import requests
import time

start_time = time.time()
url = 'https://api.pwnedpasswords.com/range/'
string = getpass.getpass('Enter Password: ')


print("Reading the data if any :\n\
<SHA1 hash of entered password> : <Number of people who have used it>\n")

def search(first_half,second_half):
	flag = 0
	sum = 0
	result = []
	file = open("pwned.txt","r")
	lines = file.readlines()
	for line in lines:
		result.append(line.rstrip().split(':'))
		sum=sum+1
	for i in result:
		if(i[0]==second_half):
			flag = flag + 1
			print(first_half+i[0],":",i[1])
	if(flag==0):
		print("\nNo hashes matched\n")
	print("Processed through {} similar hashes".format(sum))


def write(data):	
	file = open("pwned.txt","w")
	file.write(data)
	file.close()

string = hashlib.sha1(string.encode()).hexdigest()
string = string.upper()
first_half = string[:5]
second_half = string[5:]

content = requests.get(url=url+first_half)
data = content.text
write(data)
search(first_half,second_half)


print("Processing time --- %s seconds ---" % (time.time() -start_time))

