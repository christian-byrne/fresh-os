
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def timecode_to_sec(time_code):
    seconds = 1
    t = time_code.split(":")
    seconds += int(int(t[0]) * 60) + int(t[1])
    return seconds



videos = {
    "137450.mp4" : {
        "start" : "5:55",
        "end" : "8:58",
        "title" : "temptitle"
    },
    "161806.mp4" : {
        "start" : "0:23",
        "end" : "12:38",
        "title" : "btemp"
    },
    "191328.mp4" : {
        "start" : "0:06",
        "end" : "13:10",
        "title" : "teereea"

    }
}
    

def crop():
    for vid in videos:
        ffmpeg_extract_subclip(
            vid,
            timecode_to_sec(videos[vid]["start"]),
            timecode_to_sec(videos[vid]["end"]),
            targetname=(videos[vid]["title"] + "_________temp.mp4")
        )
        os.remove(
            vid
        )
        os.rename(
            videos[vid]["title"] + "_________temp.mp4",
            vid
        )

crop()