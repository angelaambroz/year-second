#!/usr/bin/env python

import moviepy.editor as mpy

# Refs

DIR = "/Users/angelaambroz/Desktop/pemba/"


# The good stuff

clip1 = mpy.VideoFileClip(DIR + "GOPR1329.MP4").subclip(3, 5)
clip1.write_videofile(DIR + "VID_20150404_080940.mp4", fps=24)


clip2 = mpy.VideoFileClip(DIR + "GOPR1334.MP4").subclip(17, 19)
clip2.write_videofile(DIR + "VID_20150405_080940.mp4", fps=24)

TA = 15 * 60 + 7
TB = TA + 2

clip3 = mpy.VideoFileClip(DIR + "150406_dive1_pmb_DFMalanWall_2.MP4").subclip(TA, TB)
clip3.write_videofile(DIR + "VID_20150406_080940.mp4", fps=24)
