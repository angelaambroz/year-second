#!/usr/bin/env python 

import os
import time
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
		file_array.append(modified)
		#shutil.copy2(raw_files + item, day_files + "DAY_" + modified[:3] + modified[4:]  + ".mp4")


## There must be a faster way to do this...

year_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
long_months = ["Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"]
short_months = ["Apr", "Jun", "Sep", "Nov"]
year_array = []

for x in year_months:
	if x in long_months:
		for i in range(1,32):
			year_array.append(x + " " + `i`)
	elif x in short_months:
		for j in range(1,31):
			year_array.append(x + " " + `j`)
	elif x=="Feb":
		for k in range(1,29):
			year_array.append(x + " " + `k`)




## Checking whether a day-video is missing

# Only check stuff from before today...


for item in year_array:
	if item in file_array:
		print "fine! " + item + " is here."
	else:
		print "uh oh, looks like " + item + " is missing."
	


## Test run: Making sure MoviePy works

# clip = VideoFileClip(directory + "VID_20150126_085336.mp4").subclip(0,1)

# txt_clip = TextClip("January 26",fontsize=70,color="red")
# txt_clip = txt_clip.set_pos("center").set_duration(1)

# video = CompositeVideoClip([clip, txt_clip])

# video.write_videofile(directory + "test.mp4")

