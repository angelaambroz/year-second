#!/usr/bin/env python 

import os
import time
import datetime
import shutil
import moviepy.editor as mpy
import re


## Directories

raw_files_jf = "/Users/angelaambroz/Documents/Personal/Projects/2015raw_janfeb/"	#jan/feb
raw_files = "/Users/angelaambroz/Documents/Personal/Projects/2015raw/"				#everything else
day_files = "/Users/angelaambroz/Documents/Personal/Projects/2015new/"				#ready to concat



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
		file_array.append(modified)
		if "DAY_" + datetime.datetime.strftime(modified, "%B%d") + ".mp4" not in os.listdir(day_files):
			shutil.copy2(raw_files_jf + item, day_files + "DAY_" + datetime.datetime.strftime(modified, "%B%d") + ".mp4")


for item in os.listdir(raw_files):
	
	if item==".DS_Store":
		pass

	else:
		endie = item[-6:-4]
		modified = "2015 " + item[8:10] + " " + item[10:12]
		modified = datetime.datetime.strptime(modified, "%Y %m %d")

		if modified in file_array:
			print "Multiple files for this day: " + modified.strftime("%Y %b %d")
			mpy.VideoFileClip(raw_files + item).save_frame(day_files + "../2015edited/multiples/still_" + modified.strftime("%b%d") + "_" + endie + ".jpeg")
			mpy.VideoFileClip(day_files + "DAY_" + datetime.datetime.strftime(modified, "%B%d") + ".mp4").save_frame(day_files + "../2015edited/multiples/still_" + modified.strftime("%b%d") + "_00.jpeg")

		else: 
			file_array.append(modified)
		
		if ("DAY_" + datetime.datetime.strftime(modified, "%B%d") + ".mp4") not in os.listdir(day_files):
			shutil.copy2(raw_files + item, day_files + "DAY_" + datetime.datetime.strftime(modified, "%B%d") + ".mp4")
		
			
file_array.append(datetime.datetime.now())


## Checking whether a day-video is missing

date_set = set(file_array[0]+datetime.timedelta(x) for x in range((file_array[-1]-file_array[0]).days))

missing = sorted(date_set-set(file_array))

for item in missing:
	print "Missing: " + item.strftime("%Y %b %d")


# Making the 'FORGOT' clip

for item in missing:
	caption = datetime.datetime.strftime(item, "%B %d")
	filename = datetime.datetime.strftime(item, "%B%d")
	if ("DAY_" + filename + ".mp4") in os.listdir(day_files):
		pass
	elif ("DAY_" + filename + "_m.mp4") not in os.listdir(day_files):
		txt_clip = mpy.TextClip(caption,fontsize=50,color="white")
		txt_clip = txt_clip.set_pos(("center","bottom")).set_duration(1)
		forgot_label = mpy.TextClip("forgot. :(", fontsize=70, color="white")
		forgot_label = forgot_label.set_pos("center").set_duration(1)
		testclip = mpy.ColorClip(size=(400,400), col=[0,0,0], duration=1)
		forgot_clip = mpy.CompositeVideoClip([testclip, forgot_label, txt_clip])
		forgot_clip.write_videofile(day_files + "DAY_" + filename + "_m.mp4",fps=24)


# Looping concatenation


# First, sorting the files...
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


# Second, preparing the base clip and clip arrays.
base_clip = mpy.VideoFileClip(day_files + "DAY_December31.mp4").set_duration(1)
master_array = [base_clip]
clip_array = []


# Third, looping through the sorted files, appending to the array, concatenating.
#NB: Right now, MoviePy throws an IO error about 'too many open files' if n>66. 
#So I'm manually changing  the first loop's, and going through in 60-clip chunks.

for item in sorted(os.listdir(day_files), key=gettimestamp)[121:]: #[DON'T RE-DO PARTS 1-3]
	if item==".DS_Store" or item=="DAY_December31.mp4":
		pass	
	else:
		print "Now doing: " + item
		day_clip = mpy.VideoFileClip(day_files+item).set_duration(1)
		if item[-6:-4]=="_m":
			clip_array.append(day_clip)
		else:
			caption = datetime.datetime.strptime(item[4:-4], "%B%d")
			caption = datetime.datetime.strftime(caption, "%B %d")
			txt_clip = mpy.TextClip(caption,fontsize=50,color="white")
			txt_clip = txt_clip.set_pos(("center","bottom")).set_duration(1)
			clip_item = mpy.CompositeVideoClip([day_clip, txt_clip])
			clip_array.append(clip_item)

chunk_video = mpy.concatenate_videoclips(clip_array, method='compose')
chunk_video.write_videofile(day_files + "../2015edited/clip" + `3` + ".mp4",fps=24)
chunk_clip = mpy.VideoFileClip(day_files + "../2015edited/clip" + `3` + ".mp4")


# Looping over the master array, concatting the year video itself. 

dirty_hack = range(1,6)

# for i in dirty_hack:
# 	print i
	# chunk_video = mpy.VideoFileClip(day_files + "../2015edited/clip" + `i` + ".mp4")
	# master_array.append(chunk_video)

# year_video = mpy.concatenate_videoclips(master_array, method='compose')
# year_video.write_videofile(day_files + "../2015edited/2015 in review.mp4",fps=24)


# Some thoughts on the music:
# - Terry Riley's In C, by Africa Express
# - Six Pianos, by Steve Reich


