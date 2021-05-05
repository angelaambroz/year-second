
import re
import os
import time
import shutil
import moviepy.editor as mpy
from datetime import datetime, timedelta

## Directories

raw_files_jf = "/Users/angelaambroz/Documents/Personal/Projects/2015raw_janfeb/"	#jan/feb
raw_files = "/Users/angelaambroz/Documents/Personal/Projects/2015raw/"				#everything else
raw_files_last = "/Users/angelaambroz/Documents/Personal/Projects/2015raw_last/"	#nov/dec
DAY_FILES = "/Users/angelaambroz/Documents/Personal/Projects/2015new/"			#ready to concat

def convert_filename(filepath: str, modified_time: bool = False):
	file_array = []

	for item in os.listdir(filepath):
		if item in (".DS_Store", "test.mp4"):
			pass
		else:
			if modified_time:
				modified = time.ctime(os.path.getmtime(filepath + item))
				if modified[4:7]=="Dec":
                                    modified = f"2014 {modified[4:-14]}"
				elif modified[8:9]==" ":
                                    modified = f"2015 {modified[4:7]} {modified[9:10]}"
				else:
                                    modified = f"2015 {modified[4:-14}"
				modified = datetime.strptime(modified, "%Y %b %d")

			else: 
				endie = item[-6:-4]
                                modified = f"2015 {item[8:10]} {item[10:12]}"
				modified = datetime.strptime(modified, "%Y %m %d")

			if modified in file_array:
				print(f"Multiple files for this day: {modified.strftime('%Y %b %d')}")
				#mpy.VideoFileClip(filepath + item).save_frame(DAY_FILES + "../2015edited/multiples/still_" + modified.strftime("%b%d") + "_" + endie + ".jpeg")
				mpy.VideoFileClip(f"{DAY_FILES}DAY_{datetime.stftime(modified, '%B%d')}.mp4").save_frame(f"{DAY_FILES}../2015edited/multiples/still_{modified.strftime('%b%d')}_00.jpeg")

			else: 
				file_array.append(modified)
			
			if ("DAY_" + datetime.strftime(modified, "%B%d") + ".mp4") not in os.listdir(DAY_FILES):
				shutil.copy2(filepath + item, DAY_FILES + "DAY_" + datetime.strftime(modified, "%B%d") + ".mp4")
	
	return file_array
			

def check_missing(array_of_files):
	"""Iterate through file names, parse date, check if missing"""
	date_set = [datetime(2015,1,1) + timedelta(days=364)]

	day_file_dates = []
	for day_file in os.listdir(DAY_FILES):
		day_file_date_string = day_file.split(".")[0].split("DAY_")[-1].split("_m")[0]
		print(day_file_date_string)
		if day_file_date_string:
			day_file_dates.append(datetime.strptime("2015"+day_file_date_string, "%Y%B%d"))

	missing = sorted(set(date_set)-set(day_file_dates))
	for item in missing:
		print("Missing: " + item.strftime("%Y %b %d"))

	return missing

def make_missing(array_of_missing):
	for item in array_of_missing:
		caption = datetime.strftime(item, "%B %d")
		filename = datetime.strftime(item, "%B%d")

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


# last_few_files = convert_filename(raw_files_last)
# missings = check_missing(last_few_files)
# make_missing(missings)


# Looping concatenation


# First, sorting the files...
regex = re.compile("^DAY_(\D*\d+)")

def gettimestamp(thestring):
	if thestring==".DS_Store":
		return datetime.strptime("2014December30", "%Y%B%d")
	else:
		m = regex.search(thestring)
		if m.groups()[0]=="December31":
			return datetime.strptime("2014" + m.groups()[0], "%Y%B%d")
		else:
			return datetime.strptime("2015" + m.groups()[0], "%Y%B%d")


# Second, preparing the base clip and clip arrays.
base_clip = mpy.VideoFileClip(DAY_FILES + "DAY_December31.mp4").set_duration(1)
master_array = [base_clip]
clip_array = []


# Third, looping through the sorted files, appending to the array, concatenating.
#NB: Right now, MoviePy throws an IO error about 'too many open files' if n>66. 
#So I'm manually changing  the first loop's, and going through in 60-clip chunks.

counter = 0

for item in sorted(os.listdir(DAY_FILES), key=gettimestamp)[329:]: #[DON'T RE-DO PARTS 1-6]
	print(`item` + " is the " + `counter` + "th item.")
	counter += 1

	if item==".DS_Store" or item=="DAY_December31.mp4":
		pass	
	else:
		print("Now doing: " + item)
		day_clip = mpy.VideoFileClip(DAY_FILES+item).set_duration(1)
		if item[-6:-4]=="_m":
			clip_array.append(day_clip)
		else:
			caption = datetime.strptime(item[4:-4], "%B%d")
			caption = datetime.strftime(caption, "%B %d")
			txt_clip = mpy.TextClip(caption,fontsize=50,color="white")
			txt_clip = txt_clip.set_pos(("center","bottom")).set_duration(1)
			clip_item = mpy.CompositeVideoClip([day_clip, txt_clip])
			clip_array.append(clip_item)

chunk_video = mpy.concatenate_videoclips(clip_array, method='compose')
chunk_video.write_videofile(DAY_FILES + "../2015edited/clip" + `8` + ".mp4",fps=24)
chunk_clip = mpy.VideoFileClip(DAY_FILES + "../2015edited/clip" + `8` + ".mp4")


# Looping over the master array, concatting the year video itself. 

# dirty_hack = range(1,6)

# for i in dirty_hack:
# 	print(i)
	# chunk_video = mpy.VideoFileClip(DAY_FILES + "../2015edited/clip" + `i` + ".mp4")
	# master_array.append(chunk_video)

# year_video = mpy.concatenate_videoclips(master_array, method='compose')
# year_video.write_videofile(DAY_FILES + "../2015edited/2015 in review.mp4",fps=24)


# Some thoughts on the music:
# - Six Pianos, by Steve Reich (July 26 Angela votes for this)
# - Terry Riley's In C, by Africa Express
# - Terry Riley's In C, on the Master of Minimalism album, from ~3min on (when it gets quiet)
# - Spiegel im Spiegel, by Arvo Part


