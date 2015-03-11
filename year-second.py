#!/usr/bin/env python 

import os
import time
from moviepy.editor import *

directory = "/Users/angelaambroz/Documents/Personal/Projects/2015 second a day/"

for item in os.listdir(directory):
	if item==".DS_Store": 
		print "skipping ds store"
	else:
		print "last modified: %s" % time.ctime(os.path.getmtime(directory + item))



## Test run: Making sure MoviePy works

# clip = VideoFileClip(directory + "VID_20150126_085336.mp4").subclip(0,1)

# txt_clip = TextClip("January 26",fontsize=70,color="red")
# txt_clip = txt_clip.set_pos("center").set_duration(1)

# video = CompositeVideoClip([clip, txt_clip])

# video.write_videofile(directory + "test.mp4")

