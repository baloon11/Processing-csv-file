#####Processing csv file and download images from the url that were found
This script:

- input CSV file,
- filters each line for existence in it url with a certain extension (passed as the second argument to the console),
- and if the line is filtered, then in it:

	- find product SKU,
	- create a directory called SKU of Product,
	- download all images from all links of this line in this folder.

Usage
-----
	python pic_from_url.py image_path.csv .ashx?la=en

	where:
		image_path.csv -name of .csv file
		.ashx?la=en  - end of the url on which we filter lines


Script uses standard python library
and does not need additional packages.
Python version 2.7

It has been tested on Ubuntu 12.04.
but it will work on a higher version.

-----------------------------------------

This script solves a very narrow problem , it is associated with a form of csv file.
But it can be the basis to create other scripts for the csv file of another type.
