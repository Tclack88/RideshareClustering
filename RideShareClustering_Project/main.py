#!/usr/bin/env python3

import csv
import numpy as np
from clustfunc import * 
import sys

# filename variables so it's simpler to change which files are read in.
# Between different events 'attending_file' and 'loc_file' are likely to change
# but not masterlist.
masterlist = 'MasterList.csv'
attending_file = 'going.csv'
loc_file = 'Locations.csv'
clus_size = 3




							##### STEP 1 #####
# Function: converts two csv files into three separate lists of dictionaries
# These dictionaries are assigned to the variable name
# Input: two csv files stored in current directory
# Output: three lists of dictionaries, for all riders and for all drivers
#	the other is each location
#		ex: [a,b,c,d,e,f,g]		[A,B,C,D]
#	 rider names (lowercase)   Location names (Upper Case)



#########	  Make Rider and Driver and Location  dictionaries	  ############
with open(attending_file) as f0:
	readCSV0 = csv.reader(f0,delimiter=',')

	riding = []
	driving = []
	nocount = 0
	yescount = 0
	
	for line in readCSV0:
		if line[2]=='Yes' and line[3]=='No':
			riding.append(line[1].lower())
			nocount += 1

		if line[2]=='Yes' and line[3]=='Yes':
			driving.append(line[1].lower())
			yescount += 1

with open(masterlist) as f1:
	readCSV1 = csv.reader(f1,delimiter=',')

	riders = []
	drivers = []	
	for rider in readCSV1:
		if rider[1].lower() in riding:
					# use of .lower() is to remove discontinuity in typing 
					# emails (which are not case sensitive)

			riders.append({'name':rider[2],'y':float(rider[3]),'x':float(rider[4]),'email':rider[1].lower()})

		if rider[1].lower() in driving:

			drivers.append({'name':rider[2],'y':float(rider[3]),'x':float(rider[4]),'email':rider[1].lower()})
	
	for rider in riders:
		name = rider['name']
		vars()[name] = rider
	for driver in drivers:
		name = driver['name']
		vars()[name] = driver
					# assigns the variable 'name' of the dictionary to the dict.



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

clustodrive = yescount - np.ceil(nocount/3)
if clustodrive >= 0:

	adj = adjaceancy(riders)

	cluster = cluster(adj,riders)

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

