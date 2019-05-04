#!/usr/bin/env python3

import numpy as np
from numpy.random import random as rng
import os
from matplotlib.pyplot import *

################### Get Input and Clear Old Data (TempDat) ###################

riders=input("\nThe purpose of this is to generate sample data\n" \
    "How many riders do you want? ")

while riders.isdigit() is False or int(riders) < 1: 
	riders=input("Please enter a valid input: ")
riders = int(riders)



pickup = input("\nHow many pickup locations do you want? ")

while pickup.isdigit() is False or int(pickup) < 1:        
    pickup = input("Please enter a valid input: ")
pickup = int(pickup)




drivers = input("\n How many drivers should there be? ")
while drivers.isdigit() is False or int(drivers) < 1:
    drivers = input("Please enter a valid input: ")
drivers = int(drivers)


os.system("rm SampleDat* -f")

##############################################################################
################          Creating Rider File              ###################
##############################################################################


riders_file = 'SampleDatMasterList.csv'

riders_name = []
riders_email = []

for i in range(riders):
	riders_name.append(str(i))
	riders_email.append("gary"+str(i)+"@MikaylaSmells.com")
riders_x = 10*rng(riders)
riders_y = 10*rng(riders)

drivers_name = []
drivers_email = []
for i in range(drivers):
    drivers_name.append(str(i))
    drivers_email.append("driver"+str(i)+"@MikaylaSmells.com")
drivers_x = 10*rng(drivers)
drivers_y = 10*rng(drivers)


for i in range(riders):

	newline = 'echo '+'SomeTimeStamp,'+str(riders_email[i])+','+str(riders_name[i])+','+str(riders_x[i])+','+str(riders_y[i])+',No'+' >> '+riders_file
	os.system(newline)

for i in range(drivers):
	newline = 'echo '+'SomeTimeStamp,'+str(drivers_email[i])+','+str(drivers_name[i])+','+str(drivers_x[i])+','+str(drivers_y[i])+',Yes'+' >> '+riders_file
	os.system(newline)

##############################################################################
################         Creating Pickup File              ###################
##############################################################################

pickup_file = 'SampleDatLocations.csv' 

pickup_name = []
for i in range(pickup):
        pickup_name.append(str(i))
pickup_x = 10*rng(pickup)
pickup_y = 10*rng(pickup)


for i in range(pickup):		
        newline = 'echo '+str(pickup_name[i])+','+str(pickup_x[i])+','+str(pickup_y[i])+' >> '+pickup_file
        os.system(newline)


print("\nData files have been saved in this directory")

##############################################################################
################              Creating Plot                ###################
##############################################################################

fig,ax = subplots()
ax.scatter(riders_x,riders_y,c='b',marker='.',linestyle='None',label='Rider')
ax.scatter(drivers_x,drivers_y,c='k',marker='^',linestyle='None',label='Driver')
ax.scatter(pickup_x,pickup_y,c='r',marker='s',linestyle='None',label='Location')
ax.legend(loc=0)

for i in range(riders):
    ax.annotate(riders_name[i],(riders_x[i],riders_y[i]))
for i in range(drivers):
    ax.annotate(drivers_name[i],(drivers_x[i],drivers_y[i]))
for i in range(pickup):
    ax.annotate(pickup_name[i],(pickup_x[i],pickup_y[i]))


title("Sample Data")
fig.show()

input("Showing temporary data, (not automatically saved) \n" \
		"Try and guess which points will be clustered\n press <enter> to exit")

