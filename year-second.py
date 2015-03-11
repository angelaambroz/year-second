#!/usr/bin/env python 

import os
import time
import datetime
import shutil
from moviepy.editor import *

## Directories

raw_files = "/Users/angelaambroz/Documents/Personal/Projects/2015 second a day/"
day_files = "/Users/angelaambroz/Documents/Personal/Projects/2015new/"


## Preparing the raw day video files

file_array = []

for item in os.listdir(raw_files):
	if item==".DS_Store" or item=="test.mp4":
		print "skipping ds store, test"
	else:
		modified = time.ctime(os.path.getmtime(raw_files + item))
		if modified[8:9]==" ":
			modified = modified[4:7] + " " + modified[9:10]
		else:
			modified = modified[4:-14]
		file_array.append("2015 " + modified)
		#shutil.copy2(raw_files + item, day_files + "DAY_" + modified[:3] + modified[4:]  + ".mp4")


## There must be a faster way to do this...

year_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
long_months = ["Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"]
short_months = ["Apr", "Jun", "Sep", "Nov"]
year_array = []

for x in year_months:
	if x in long_months:
		for i in range(1,32):
			year_array.append("2015 " + x + " " + `i`)
	elif x in short_months:
		for j in range(1,31):
			year_array.append("2015 " + x + " " + `j`)
	elif x=="Feb":
		for k in range(1,29):
			year_array.append("2015 " + x + " " + `k`)




## Checking whether a day-video is missing

# this is not working - i can't datetime-ify the strings. why?
for item in year_array:
	item = datetime.datetime.strptime(item, "%Y %b %d")

for item in file_array:
	item = datetime.datetime.strptime(item, "%Y %b %d")

# Only check stuff from before today...
today = datetime.date.today()
today = today.strftime("%Y %b %d")

print year_array
print file_array

for item in year_array:
	if item.date() > datetime.today().date():
		print item + " is the future."
	elif item.date() == datetime.today().date() :
		print item + " is today."
	else:
		print item + " is the past."


# for item in year_array:
# 	if item in file_array:
# 		print "fine! " + item + " is here."
# 	elif item > today: #this isn't working - how to check 
# 		print "ooh " + item + " is in the future"
# 	else: 
# 		print "uh oh, looks like " + item + " is missing."


## Test run: Making sure MoviePy works

# clip = VideoFileClip(directory + "VID_20150126_085336.mp4").subclip(0,1)

# txt_clip = TextClip("January 26",fontsize=70,color="red")
# txt_clip = txt_clip.set_pos("center").set_duration(1)

# video = CompositeVideoClip([clip, txt_clip])

# video.write_videofile(directory + "test.mp4")

