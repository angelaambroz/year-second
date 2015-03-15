year-second
=======

11 March 2015. AMAZING `Python` is AMAZING. A project to learn this wonderful language. Documenting 2015 via a second-a-day video, except I'm automating the actual selection of each second (for, one hopes, delightful results). Computer art?!

(Idea for next project: use `imageio` to make a photo quilt?)
(Idea for next project: looping GIF tapestry of day clips - clickable, pulls up details, special days highlighted in yellow border)


### To Do
1. ~~Set up `git`, install `moviepy`.~~
2. ~~Test run to see if MoviePy works.~~
3. ~~Check if any day is missing (`os` file meta-data?).~~
4. ~~Loop through, check that every day has a video.~~
    * **Idea 1**: ~~Loop through files, pull their date modified. Create array. Check array against full array of days since Jan 1?~~
    * **Idea 2**: Pipe date-modified data out to a text or .csv file, merge, compare?
5. ~~If day is missing, write `error` message to file _and_ use stand-in black box with "forgotten." text.~~
6. ~~If day is present, take 1-second random snip (use video meta-data to make it a `def` (function) of the video time-length).~~
7. ~~Add text for each day: JANUARY 1.~~ 
8. ~~Stitch all clips together. Ta-da! Use MoviePy's concatenation for this: `final_clip = concatenate_videoclips([clip1,clip2,clip3])`.~~
9. Make several versions?
10. Final editing polish with music, etc.
11. ~~Can I use `HEX`/`RGB` for font color?~~ Yes, I think RGB is kosher.
12. ~~If multiple files for a day, randomly pick a 1-second clip from one of them.~~ When I copy/rename them all, they overwrite with the latest one. Not random? Am I OK with this?
13. ~~How to preserve the raw video files?!~~
14. ~~Should I rename every video by its current (fragile!) data-modified? This would also standardize the file names, at least...~~
15. ~~Redo date arrays using `datetime` instead of `str`.~~ Totally inefficient, but it's working now.
16. Make a list of notable days, and highlight them in some way. (e.g. Color mask?)
17. ~~How to only pull the _last_ 1-2 seconds from a clip?~~
18. ~~Need to progressively concatenate.~~
19. ~~Make day-text a function of day-filename.~~
20. ~~Sort the files so they run in chrono order.~~
21. ~~Problem: it is EXTREMELY SLOW. What can I do?~~ Instead of writing a video file iteratively, put everything in an array and concat. Also, [0,-1] was super slow.
22. ~~How to deal with `fps` issue in both phone videos and webcam videos?~~ Wasn't fps, but size of the clip!
23. Slot in the 'forgot.' video into final year video. 
24. Add a countdown: how many days left to make videos?
25. Anything after March 15: instead of sorting/organizing/naming by date-modified, need to do it all by filename. 


### Resources

* Inspiration: [Save the Children - "Most Shocking Second a Day Video"](https://www.youtube.com/watch?v=RBQ-IoHfimQ)
* Inspiration: [Cesar Kuriyama - TED Talk](http://www.ted.com/talks/cesar_kuriyama_one_second_every_day?language=en)
* Q&A: [StackOverflow - Missing dates in a sorted list](https://stackoverflow.com/questions/2315032/how-do-i-find-missing-dates-in-a-list-of-sorted-dates)
* Documentation: [MoviePy](https://zulko.github.io/moviepy/index.html)
* Another worrying sign that I am a complete subconscious slave to fashion/the zeitgeist: [xkcd - Art project](https://xkcd.com/1496/)

