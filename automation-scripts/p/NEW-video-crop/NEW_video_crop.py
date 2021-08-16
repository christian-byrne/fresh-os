import os
from os import walk
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def timecode_to_sec(time_code):
    seconds = 1
    t = time_code.split(":")
    seconds += int(int(t[0]) * 60) + int(t[1])
    return seconds

os.chdir("/home/bymyself/a/p/NEW-video-crop")

file_name = input("file name?\n")

if os.path.isfile(f"{os.getcwd}/{file_name}"):
    quit("file not found, quitting.")

if ".mkv" in file_name:
    try:
        os.system(
            f"ffmpeg -i {file_name} -codec copy '{file_name.split('.')[0]}.mp4'")
        file_name = file_name.split(".")[0] + ".mp4"
    except:
        quit("couldn't convert all videos to mp4 before attempting crop")


# File Code
filecode = ".mp4"

new_name = f"cropped-{file_name}"


# Start & End Times
start_time = timecode_to_sec(input("Start time in formate mm:ss\n"))
end_time = timecode_to_sec(input("End time in formate mm:ss\n"))

# Crop
ffmpeg_extract_subclip(file_name, start_time, end_time, targetname=new_name)