#!/usr/bin/env python 

import os
import time
import datetime
import shutil
import moviepy.editor as mpy
import re


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
		#shutil.copy2(raw_files_jf + item, day_files + "DAY_" + datetime.datetime.strftime(modified, "%B%d") + ".mp4")
		file_array.append(modified)

for item in os.listdir(raw_files):
	if item==".DS_Store":
		pass
	else:
		modified = "2015 " + item[8:10] + " " + item[10:12]
		modified = datetime.datetime.strptime(modified, "%Y %m %d")
		#shutil.copy2(raw_files + item, day_files + "DAY_" + datetime.datetime.strftime(modified, "%B%d") + ".mp4")
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


#First, sorting the files...
regex = re.compile("^DAY_(\D*\d+)")

def gettimestamp(thestring):
	if thestring==".DS_Store":
		return datetime.datetime.strptime("2014December30", "%Y%B%d")
	else:
		m = regex.search(thestring)
		if m.groups()[0]=="December31":
			return datetime.datetime.strptime("2014" + m.groups()[0], "%Y%B%d")
		else:
			return datetime.datetime.strptime("2015" + m.groups()[0], "%Y%B%d")


#Second, preparing the base clip and clip arrays.
base_clip = mpy.VideoFileClip(day_files + "DAY_December31.mp4").set_duration(1)
master_array = [base_clip]
clip_array = []


# Third, looping through the sorted files, appending to the array, concatenating.
# all_days = len(file_array)

# #This becomes a problem when all_days is a prime. :/ 
# for i in range(1,10):
# 	if all_days % i == 0:
# 		step = i

# print "Number of files: ", all_days
# print "Chunk size: ", step

#Test chase
step = 44
all_days = 88


for i in range(2+step,all_days,step):
	print "Iteration: ", i
	print clip_array
	for item in sorted(os.listdir(day_files), key=gettimestamp)[i-step:i]:
		if item==".DS_Store" or item=="DAY_December31.mp4":
			pass	
		else:
			print "Now doing: " + item
			day_clip = mpy.VideoFileClip(day_files+item).set_duration(1)
			caption = datetime.datetime.strptime(item[4:-4], "%B%d")
			caption = datetime.datetime.strftime(caption, "%B %d")
			txt_clip = mpy.TextClip(caption,fontsize=50,color="white")
			txt_clip = txt_clip.set_pos(("center","bottom")).set_duration(1)
			clip_item = mpy.CompositeVideoClip([day_clip, txt_clip])
			clip_array.append(clip_item)
			# del day_clip
			# del clip_item
	chunk_video = mpy.concatenate_videoclips(clip_array, method='compose')
	chunk_video.write_videofile(day_files + "../2015edited/clip" + `i` + ".mp4",fps=24)
	chunk_clip = mpy.VideoFileClip(day_files + "../2015edited/clip" + `i` + ".mp4")
	master_array.append(chunk_clip)
	# and then close all the chunk_array clips? how?
	print clip_array
	del clip_array[:]

year_video = mpy.concatenate_videoclips(master_array, method='compose')
year_video.write_videofile(day_files + "../2015edited/2015 in review.mp4",fps=24)



