import sys
import datetime
import json
import urllib2
import pprint
import os


response = urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?lat=52.1333&lon=-106.6833")

data = response.read().split("\n")

f = open("tempweather.txt", "wr")
for line in data:
	f.write(line)
f.close()

out = open("test.txt", "r")

info = json.load(out)

print "\n\nLocation: " + info['name']
print "Current temperature: {} Celcius".format(info["main"]["temp"] - 273.15)
print info['weather'][0]['description']

a = info['wind']['deg']
direction = "North"
if a >= 330 or a <= 30:
	direction = "North"
elif a > 30 and a < 60:
	direction = "Northeast"
elif a >= 60 and a < 120:
	direction = "East"
elif a >= 120 and a < 150:
	direction = "Southeast"
elif a > 150 and a < 210:
	direction = "South"
elif a > 210 and a < 240:
	direction = "Southwest"
elif a > 240 and a < 300:
	direction = "West"
elif a > 300 and a < 330:
	direction = "Northwest"


print "windspeed: {}Km/h from the {}".format(round(info["wind"]['speed'] * 3600/1000, 2), direction)
print "Sunrise at: {}".format(datetime.datetime.fromtimestamp(info['sys']['sunrise']).strftime('%H:%M:%S'))
print "Sunset at: {}".format(datetime.datetime.fromtimestamp(info['sys']['sunset']).strftime('%H:%M:%S'))

out.close()
os.remove("tempweather.txt")

