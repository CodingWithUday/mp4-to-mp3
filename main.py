#PYTHON MP4 TO MP3 CONVERTER
#Coded By Coding With Uday 
#Website -> https://dev-uday.cf

# Make Sure To SUBSCRIBE!


from moviepy.editor import *

vid_file = "song.mp4"

song_file_name = "music.mp3"

VideoClip = VideoFileClip(vid_file)

audioclip = VideoClip.audio

audioclip.write_audiofile(song_file_name)

audioclip.close()
VideoClip.close()

# DONE!