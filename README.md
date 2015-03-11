year-second
=======

11 March 2015. AMAZING `Python` is AMAZING. A project to learn this wonderful language. Documenting 2015 via a second-a-day video, except I'm automating the actual selection of each second (for, one hopes, delightful results). Computer art?!

(Idea for next project: use `imageio` to make a photo quilt?)


### To Do
1. ~~Set up `git`, install `moviepy`.~~
2. ~~Test run to see if MoviePy works.~~
3. Check if any day is missing (`os` file meta-data?).
4. Loop through, check that every day has a video.
    * **Idea 1**: ~~Loop through files, pull their date modified. Create array. Check array against full array of days since Jan 1?~~
    * **Idea 2**: Pipe date-modified data out to a text or .csv file, merge, compare?
5. If day is missing, write `error` message to file _and_ use stand-in black box with "Forgot today!" text.
6. If day is present, take 1-second random snip (use video meta-data to make it a `def` (function) of the video time-length).
7. Add text for each day: JANUARY 1. 
8. Stitch all clips together. Ta-da!
9. Make several versions?
10. Final editing polish with music, etc.
11. Can I use `HEX`/`RGB` for font color?
12. ~~If multiple files for a day, randomly pick a 1-second clip from one of them.~~ When I copy/rename them all, they overwrite with the latest one. Not random? Am I OK with this?
13. How to preserve the raw video files?!
14. ~~Should I rename every video by its current (fragile!) data-modified? This would also standardize the file names, at least...~~
15. Redo date arrays using `datetime` instead of `str`.




### Resources

* Inspiration: [Save the Children - "Most Shocking Second a Day Video"](https://www.youtube.com/watch?v=RBQ-IoHfimQ)
* Inspiration: [Cesar Kuriyama - TED Talk](http://www.ted.com/talks/cesar_kuriyama_one_second_every_day?language=en)
* Documentation: [MoviePy](https://zulko.github.io/moviepy/index.html)
* Another worrying sign that I am a complete subconscious slave to fashion/the zeitgeist: [xkcd - Art project](https://xkcd.com/1496/)






