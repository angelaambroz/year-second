#!/usr/bin/env python 

import os
import time
import datetime
import shutil
import moviepy.editor as mpy


## Directories

raw_files_jf = "/Users/angelaambroz/Documents/Personal/Projects/2015raw_janfeb/"
raw_files = "/Users/angelaambroz/Documents/Personal/Projects/2015raw/"
day_files = "/Users/angelaambroz/Documents/Personal/Projects/2015new/"


## Preparing the raw day video files

file_array = []

for item in os.listdir(raw_files_jf):
	if item==".DS_Store" or item=="test.mp4":
		pass
	else:
		modified = time.ctime(os.path.getmtime(raw_files_jf + item))
		if modified[4:7]=="Dec":
			modified = "2014 " + modified[4:-14]
		elif modified[8:9]==" ":
			modified = "2015 " + modified[4:7] + " " + modified[9:10]	
		else:
			modified = "2015 " + modified[4:-14]
		modified = datetime.datetime.strptime(modified, "%Y %b %d")
		shutil.copy2(raw_files_jf + item, day_files + "DAY_" + datetime.datetime.strftime(modified, "%B%d") + ".mp4")
		file_array.append(modified)

for item in os.listdir(raw_files):
	if item==".DS_Store":
		pass
	else:
		modified = "2015 " + item[8:10] + " " + item[10:12]
		modified = datetime.datetime.strptime(modified, "%Y %m %d")
		shutil.copy2(raw_files + item, day_files + "DAY_" + datetime.datetime.strftime(modified, "%B%d") + ".mp4")
		file_array.append(modified)

file_array.append(datetime.datetime.now())


## Checking whether a day-video is missing

date_set = set(file_array[0]+datetime.timedelta(x) for x in range((file_array[-1]-file_array[0]).days))

missing = sorted(date_set-set(file_array))

for item in missing:
	print "Missing: " + item.strftime("%Y %b %d")


## Making the 'FORGOT' clip

# testclip = mpy.ColorClip(size=(400,400), col=[0,0,0], duration=1)

# forgot_label = mpy.TextClip("forgot. :(", fontsize=70, color="white")
# forgot_label = forgot_label.set_pos("center").set_duration(1)

# forgot_clip = mpy.CompositeVideoClip([testclip, forgot_label])


## Looping concatenation

base_clip = mpy.VideoFileClip(day_files + "DAY_December31.mp4").set_duration(1)
clip_array = [base_clip]

sorted_files = os.listdir(day_files)

# need to change this - can i ADD a date-modified attribute to the files? 
sorted_files.sort(key=lambda x: os.stat(os.path.join(day_files, x)).st_mtime)

# for item in sorted_files:
# 	if item==".DS_Store" or item=="DAY_Dec31.mp4":
# 		pass	
# 	else:
# 		print "Now doing: " + item
# 		day_clip = mpy.VideoFileClip(day_files+item).set_duration(1)
# 		txt_clip = mpy.TextClip(item[4:7] + " " + item[7:9],fontsize=50,color="white")
# 		txt_clip = txt_clip.set_pos(("center","bottom")).set_duration(1)
# 		clip_item = mpy.CompositeVideoClip([day_clip, txt_clip])
# 		clip_array.append(clip_item)

# year_video = mpy.concatenate_videoclips(clip_array, method='compose')
# year_video.write_videofile(day_files + "../2015edited/2015 in review.mp4",fps=24)






