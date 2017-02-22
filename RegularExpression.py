"""This program helps identify the strings on a text file that don't have the code "mod" on them,
and writes them in a new file. The original file was extracted from elan, in which slide changes 
in a video of a lecture were identified. Each string corresponds to a change in the slides and 
records the time of the event in ms, as well as the code assigned to that event. Some of the slide
changes were small modification of the previous slide and were assigned the prefix 'mod'. In order 
to evaluate the performance of an automated method that identifies slide changes, we want only the 
ones that correspond to full modifications of the slides (i.e., the ones without the prefix 'mod'.
This program identifies those cases and produces a text file that can be imported into R."""


import re

file = open('Dan Jurafsky.txt', 'r')
elan_data = file.read()

regex = r'(\d{5,7}\s[^mod]{3}\D+)'

match = re.findall(regex, elan_data)

file.close()

filew = open('JurafskyBigChanges.txt', 'w')

for i in match:
	filew.write(i)

filew.close()