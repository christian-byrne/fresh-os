
x = open("/home/bymyself/_BYMYself/bmp/Dl_old/Parse_and_Trim_log.txt", "r").readlines()


r = """------------------------------------------------------------------------------------------
|                                                                                        |
|                             62  a_title_title_title_title_                             |
|                                                                                        |
------------------------------------------------------------------------------------------

|    URL:           |   www.youtube.com/sadfsafdsafdsa   
|    Start Time:    |       3:54       |     End Time:     |       4:23       |
|    Finished On:   |       2021-04-11  23:24:37    
"""

bar = "------------------------------------------------------------------------------------------"


ret = []
switch = 2

for index, _ in enumerate(x):
    try:
        if bar in _ and switch % 2 == 0:
            switch += 1
            bar_count = 0
            i = 0 + index
            temp = []
            while bar_count < 3:
                temp.append(x[i])
                if bar in x[i]:
                    bar_count += 1 
                i += 1
            ret.append(temp)
        elif bar in _ and switch % 2 != 0:
            switch += 1
    except: pass


dic_list = []

for rere in ret:
    dic = {}
    go = "".join(rere)
    #print(go)
    for index, _ in enumerate(go):
        if _.isnumeric():
            i = 5
            while go[i+index] != " ":
                i += 1
            if go[index+1:i+index+5][0].isnumeric():
                if go[index+2:i+index+5][0].isnumeric():
                    if go[index+3:i+index+5][0].isnumeric():
                        out = go[index+1:i+index+5]
                    else:
                        out = go[index+3:i+index+5]

                else:
                    out = go[index+2:i+index+5]
            else:
                out = go[index+1:i+index+5]

            dic["name"] = out.replace(" ","")
            break

    for _ in rere:
        if "Start Time" in _:
            tmp = _.split("|")

            start = tmp[2].replace(" ","")
            end = tmp[4].replace(" ","")

            dic["start f"] = start
            dic["end f"] = end

            start = start.split(":")

            dic["start"] = ( int(start[0]) * 60 + int(start[1]) )
            end = end.split(":")
            dic["end"] = ( int(end[0]) * 60 + int(end[1]) )
    
    dic_list.append(dic)


from moviepy.video.io.VideoFileClip import VideoFileClip

import os
import subprocess

def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)


temp1 = os.listdir()
directory = []
for _ in temp1:
    if ".png" not in _:
        directory.append(_)


counter = 0
shorter_than_desired = []
not_in_dir = []
not_in_log = []
verbose = True
repeats = []
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def ex(vid, start, end):
    try:
        subprocess.call(["ffmpeg", "-i", vid, "-ss", start, "-to", end, "-c", "copy", ("NEW" + vid)])
    except:
        errors.append(vid)

errors = []

for index, _ in enumerate(dic_list):
    che = False
    for x in directory:
        
        if _["name"] in x:

            repeats.append(_["name"])
            counter += 1        
            length = get_length(x)
            
            if verbose:
                print("Current Length:")
                print(length)
                print("Desired Length:")
                print(
                    _["end"] - _["start"]
                )

            if verbose:
                if length < (_["end"] - _["start"]) - 4:
                    print("\nShorter than Desired:\n\n")
                    print(_["name"])
                    print(x)
                    print("Current Length:")
                    print(length)
                    print("Desired Length:")
                    print(
                        _["end"] - _["start"]
                    )



            if length > (_["end"] - _["start"]) + 3:
                print("\nLonger than Desired:\n\n")
                print(_["name"])
                print(x)
                print("Current Length:")
                print(length)
                print("Desired Length:")
                print(
                    _["end"] - _["start"]
                )

                print("\n\n\n\n\n\n")
                print(x)
                print(_["start f"])
                print(_["end f"])
                
                

                ex(x, str(_["start"]), str(_["end"]))

   

                #subprocess.call(["ffmpeg", "-i", x, "-ss", ("00:" + _["start f"]), "-to", ("00:" + _["end f"]), "-c", "copy", "AAAAANWWWWWWWWW.mp4"])



            che = True
    if not che:
        not_in_dir.append(_)  



def write_out():
    fi = open("output.txt", "w")
    fi.write("\n\n\n\n\n\nNOT IN DIR BUT IN LOG FILE\n\n\n\n")

    for _ in directory:
        check = False
        for xi in dic_list:
            if xi["name"] in _:
                check = True
        if not check:
            not_in_log.append(_)

    for _ in not_in_dir:
        fi.write("\n\n\n")
        for key, value in _.items():
            fi.write(str(key))
            fi.write("\n")
            fi.write(str(value))
            fi.write("\n")

    fi.write("\n\n\n\n\n\nNOT IN LOG FILE BUT IN DIRECTORY\n\n\n\n")

    for _ in not_in_log:
        fi.write(str(_))
        fi.write("\n")

    fi.close()

print(errors)