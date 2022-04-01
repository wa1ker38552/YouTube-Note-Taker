# YouTube-Note-Taker
The program prints out a list of facts/notes from a certain YouTube video if you don't want to watch a video and just want to read out the main points of the video.

**Setup:**
The program work by finding key words in the description of the YouTube video and indexing sentences from the transcript of the video to find sentences that contain the keywords. The program finds sentences by ". " so decimal points are not counted as a sentence. There are 2 options for the key words, you can either input the keywords manually by editing the list ```keywords = []``` if the description of the video is vague or there is none. Also make sure to comment out the line
```keyterms = get_facts(text)``` on line 44. If you want the program to index based off of the description, just leave the program as is, since the description searcher automatically overrides the keyterm list. Key terms are found in the description by removing any common words in the description and then removing any word not found in the dictionary which usually is a website name or link. The program then removes words under 3 characters so that uncommon words like "ing" are not included. The result is a list of terms that the video is mostly about!

**Examples:**
