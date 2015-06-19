import urllib2
import re
import sys

response = urllib2.urlopen(sys.argv[1])
txt = response.read()
txt = txt.split("\n")
i = 1
for line in txt:
	if re.search('[Bb]en', line):
		print i
	i = i + 1

