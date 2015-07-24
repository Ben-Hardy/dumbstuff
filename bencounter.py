import urllib2
import re
import sys

# count the number of times my first name is found in a website

response = urllib2.urlopen(sys.argv[1])
txt = response.read()
txt = txt.split("\n")
count = 0

for line in txt:
	words = line.split(" ");
	for w in words:
		if re.search('[Bb]en', w):
			count += 1

print("Ben was found {} times!".format(count))

