How to use this demo folder:



Run DatGen.py and follow the prompting to generate data to your whim



Run demo.py to implement the clustering and see the results




NOTE: as mentioned in the accompanying pdf, the labeling of the 2nd plot isn't
	ideal due to overlapping when the data size is large or the points are too
	close. We found a library that fixes this problem, but it corrupts the 
	numpy/matplotlib library when imported on the RaspberryPi 
	(as it has been configured by default)
