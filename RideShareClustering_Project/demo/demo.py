#!/usr/bin/env python3

import csv
import numpy as np
from democlustfunc import * 
import sys


masterlist = 'SampleDatMasterList.csv'
loc_file = 'SampleDatLocations.csv'



########################################################################
########													   #########
######## This is a demo version of the code for your enjoyment #########
########													   #########
########################################################################

# All code comments for the primary code are in main.py and clusterfunc.py



							##### STEP 1 #####


#########	  Make Rider and Driver and Location  dictionaries	  ############

clus_size = input("What max group size do you want for this demo?" \
					"\n(enter any number > 1) ")
while clus_size.isdigit() is False or int(clus_size) < 2:
	clus_size = input("Please enter a valid input: ")
clus_size = int(clus_size)
		
with open(masterlist) as f1:
	readCSV1 = csv.reader(f1,delimiter=',')

	riders = []
	drivers = []
	nocount = 0
	yescount = 0	
	for rider in readCSV1:
		if rider[5]=='No':

			riders.append({'name':rider[2],'y':float(rider[3]),'x':float(rider[4]),'email':rider[1].lower()})
			nocount += 1
	
		elif rider[5]=='Yes':

			drivers.append({'name':rider[2],'y':float(rider[3]),'x':float(rider[4]),'email':rider[1].lower()})
			yescount += 1
	
	for rider in riders:
		name = rider['name']
		vars()[name] = rider
	for driver in drivers:
		name = driver['name']
		vars()[name] = driver


###################		Make Pickup Point Dictionaries	   ##################

with open(loc_file) as f2:
	readCSV2 = csv.reader(f2,delimiter=',')

	locations = []

	for location in readCSV2:
	
		locations.append({'name':location[0],'y':float(location[1]),'x':float(location[2])})

	for location in locations:
		name = location['name']
		vars()[name] = location



#### STEP 2 ####
# Apply cluster riders
# Match that rider group to nearest pickup point
# Match nearest driver to that pickup point
# Plot

clustodrive = yescount - np.ceil(nocount/clus_size)
if clustodrive >= 0:

	adj = adjaceancy(riders)

	cluster = cluster(adj,riders,clus_size)

	Groups = LocGrpMatch(cluster,locations)

	Groups, UnmatchedDrivers = DriverToGrp(drivers,Groups)


	for Group in Groups:
		print("pickup Location:",Group[-2]['name'])
		print("Driver:",Group[-1]['name'])
		print("Riders:")
		for i in Group[0:-2]:
			print("   ",i['name'])
		print()

	if len(UnmatchedDrivers) == 0:
		print("Perfect! No Unmatched Drivers!")
	else:
		print("Unmatched Drivers:")
		for i in UnmatchedDrivers:
			print(i['name'])


	clusterdraw(Groups,UnmatchedDrivers)

	LocMap(Groups,UnmatchedDrivers)

	plt.show()


else:
	print("Not enough drivers, find more drivers and try again\n", file=sys.stderr)


