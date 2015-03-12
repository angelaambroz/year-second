#!/usr/bin/env python 

import os
import time
import datetime
import shutil
import moviepy.editor as mpy

## Directories

raw_files = "/Users/angelaambroz/Documents/Personal/Projects/2015 second a day/"
day_files = "/Users/angelaambroz/Documents/Personal/Projects/2015new/"


## Preparing the raw day video files

file_array = []

for item in os.listdir(raw_files):
	if item==".DS_Store" or item=="test.mp4":
		pass
	else:
		modified = time.ctime(os.path.getmtime(raw_files + item))
		if modified[8:9]==" ":
			modified = modified[4:7] + " " + modified[9:10]
		else:
			modified = modified[4:-14]
		file_array.append("2015 " + modified)
		#shutil.copy2(raw_files + item, day_files + "DAY_" + modified[:3]
		 # + modified[4:]  + ".mp4")


## There must be a faster way to do this...

year_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", 
"Aug", "Sep", "Oct", "Nov", "Dec"]
long_months = ["Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"]
short_months = ["Apr", "Jun", "Sep", "Nov"]
year_array = []

print len(year_months)

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

year_days = []
year_files = []

for item in year_array:
	day = datetime.datetime.strptime(item, "%Y %b %d")
	year_days.append(day)

for item in file_array:
	year_file = datetime.datetime.strptime(item, "%Y %b %d")
	year_files.append(year_file)


for item in year_days:
	if item in year_files and item.date() <= datetime.date.today():
		print `item` + ": OK"
	elif item.date() > datetime.date.today():
		print `item` + ": to be completed"
	else: 
		print `item` + ": missing"

print os.getcwd()

## Making the 'FORGOT' clip

testclip = mpy.ColorClip(size=(400,400), col=[0,0,0], duration=1)

forgot_label = mpy.TextClip("forgot. :(", fontsize=70, color="white")
forgot_label = forgot_label.set_pos("center").set_duration(1)


forgot_clip = mpy.CompositeVideoClip([testclip, forgot_label])
forgot_clip.write_videofile(day_files+ "/../test.mp4",fps=24)



## Test run: Making sure MoviePy works

# clip = VideoFileClip(directory + "VID_20150126_085336.mp4").subclip(0,1)

# txt_clip = TextClip("January 26",fontsize=70,color="red")
# txt_clip = txt_clip.set_pos("center").set_duration(1)

# video = CompositeVideoClip([clip, txt_clip])

# video.write_videofile(directory + "test.mp4")

# from moviepy.editor import VideoFileClip, concatenate_videoclips
# clip1 = VideoFileClip("myvideo.mp4")
# clip2 = VideoFileClip("myvideo2.mp4").subclip(50,60)
# clip3 = VideoFileClip("myvideo3.mp4")
# final_clip = concatenate_videoclips([clip1,clip2,clip3])
# final_clip.write_videofile("my_concatenation.mp4")

