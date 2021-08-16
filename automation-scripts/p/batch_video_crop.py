import os
from os import walk
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


# (2) Path to the files -- their original location
ogPath = "/home/bymyself/d"



fileList = []
for (dirpath, dirnames, filenames) in walk(ogPath):
    fileList.extend(filenames)
    break


try:
    os.system(
        "for i in *.mkv; do ffmpeg -i '$i' -codec copy '${i%.*}.mp4'; done")
    os.system(
        "for i in *.webm; do ffmpeg -i '$i' -codec copy '${i%.*}.mp4'; done")
except:
    print("couldn't convert all videos to mp4 before attempting crop")

for fName in fileList:
    
    # File Code
    filecode = ".mp4"
    if "." in str(fName):
        nameParts = fName.split(".")
        filecode = "." + str(nameParts[len(nameParts)-1])
     
    # Rename original file without spaces
    OGfile = ogPath + "/" + "'" + fName + "'"
#     legalName = fName
#     legalName = legalName.replace(" ","")
#     replaceWunderscore = ["&", "{", "}", "\\", "<", ">", "*", "/", "ﾉ",\
#                           ":", "+", "|", "=", "(", ")"]
#     replaceN = ["#", "%", "{", "}", "?", "$", "!", "'", '"', ":", "@", "+",\
#                 "`", "|", "=", "(", ")"]
#     for x, y in zip(replaceWunderscore, replaceN):
#         if x in legalName:
#             legalName = legalName.replace(x, "_")
#         if y in legalName:
#             legalName = legalName.replace(y, "")
    tempName2 = "bbbbbbbbbbbbb"
    while tempName2 in fileList:
        tempName2 += "z"
    tempName2 += filecode
    tempName2 = tempName2.replace(" ","")
    legalFPath = ogPath + "/" + tempName2
    os.system("sudo mv " + OGfile + " " + legalFPath)

    # Start & End Times
    start_time = 0
    end_time = 20
    
    # Output File Name
    tempName = "aaaaaaaaaaaaaaa"
    while tempName in fileList:
        tempName += "z"
    tempName += filecode
    tempName = tempName.replace(" ","")
    
    # Crop
    ffmpeg_extract_subclip(legalFPath, start_time, end_time, targetname=tempName)
    
    # Delete Original File
    rmCommand = "sudo rm " + legalFPath
    os.system(rmCommand)
  
    # Move Cropped Vid to OG Location
    replaceCmd = "sudo mv " + tempName + " " + ogPath + "/" + "'" + str(fName) + "'"
    os.system(replaceCmd)