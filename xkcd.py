
import sys
import os
import urllib2
import random
import io

# A stupid script that scrapes XKCD and fetches a random comic.

# find out what the latest comic is since they are added to the site in sequential order
response = urllib2.urlopen("http://www.xkcd.com")
data = response.read().split("\n")

for line in data:
	if line.find("Permanent link") != -1: #obviously, if their page changes, I'll have to update this. But it hasn't changed in years so I'm not worried
		max_comic = int(line.split(" ")[5].split("/")[3]) 
		#           ^^ splits up the line with the most recent comic's URL, then gets the url from that list, then splits the url up and gets the number, then makes it an int

		# get a random number between 1 and the current newest comic's number
		rnd_comic = random.randint(1, max_comic)

		# fetch the comic's webpage
		newresponse = urllib2.urlopen("http://www.xkcd.com/" + str(rnd_comic))
		dat = newresponse.read().split("\n")
		for l in dat:
			if l.find("Image URL") != -1:
				if not os.path.exists("xkcdcomics"):
					os.makedirs("xkcdcomics")
				f = open("xkcdcomics/" + str(rnd_comic) + ".jpg", "wb")
				img = l.split(" ")[4]
				imglnk = urllib2.urlopen(img)
				f.write(imglnk.read())
				f.close()
				if sys.platform == "darwin":
					os.system("open xkcdcomics/" + str(rnd_comic) + ".jpg")





