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

# Temp broken: need to sort out (and clean up) the date comparisons. Everything after Mar 15 needs to 
# be named after its filename, not its date-modified.

file_array = []

for item in os.listdir(raw_files):
	if item==".DS_Store" or item=="test.mp4":
		pass
	else:
		modified = time.ctime(os.path.getmtime(raw_files + item))
		print item 
		print modified
		if datetime.datetime.strptime(item, "%Y %b %d")(time.ctime(os.path.getmtime(raw_files + item))) < datetime.date.today():
			if modified[8:9]==" ":
				modified = modified[4:7] + " " + modified[9:10]
			else:
				modified = modified[4:-14]
			file_array.append("2015 " + modified)
		elif datetime.datetime.strptime(item, "%Y %b %d")(time.ctime(os.path.getmtime(raw_files + item))) >= datetime.date.today():
			print "Testing this now."
		#shutil.copy2(raw_files + item, day_files + "DAY_" + modified[:3] + modified[4:]  + ".mp4")


## There must be a faster way to do this...

year_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", 
"Aug", "Sep", "Oct", "Nov", "Dec"]
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

year_days = []
year_files = []

for item in year_array:
	day = datetime.datetime.strptime(item, "%Y %b %d")
	year_days.append(day)

for item in file_array:
	year_file = datetime.datetime.strptime(item, "%Y %b %d")
	year_files.append(year_file)


for item in year_days:
	if item in year_files and item.date() <= datetime.date.today() or item.date() > datetime.date.today():
		pass
	else: 
		print item.strftime("%b%d") + ": missing"


## Making the 'FORGOT' clip

# testclip = mpy.ColorClip(size=(400,400), col=[0,0,0], duration=1)

# forgot_label = mpy.TextClip("forgot. :(", fontsize=70, color="white")
# forgot_label = forgot_label.set_pos("center").set_duration(1)

# forgot_clip = mpy.CompositeVideoClip([testclip, forgot_label])


## Looping concatenation

base_clip = mpy.VideoFileClip(day_files + "DAY_Dec31.mp4").set_duration(1)
clip_array = [base_clip]

sorted_files = os.listdir(day_files)

sorted_files.sort(key=lambda x: os.stat(os.path.join(day_files, x)).st_mtime)

# for item in sorted_files:
# 	if item==".DS_Store" or item=="DAY_Dec31.mp4":
# 		pass	
# 	else:
# 		print "Now doing: " + item
# 		day_clip = mpy.VideoFileClip(day_files+item).set_duration(1)
# 		#day_clip = day_clip.subclip(int(day_clip.duration)-5,int(day_clip.duration)-4)

# 		txt_clip = mpy.TextClip(item[4:7] + " " + item[7:9],fontsize=50,color="white")
# 		txt_clip = txt_clip.set_pos(("center","bottom")).set_duration(1)

# 		clip_item = mpy.CompositeVideoClip([day_clip, txt_clip])

# 		clip_array.append(clip_item)


# year_video = mpy.concatenate_videoclips(clip_array, method='compose')
# year_video.write_videofile(day_files + "../2015edited/2015 in review.mp4",fps=24)






