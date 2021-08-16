import os
from os import walk


# (1) Identifier tag to add at beginning of files
# (make it "" if you don't want identifiers in front of file names)
tag = "IRL2"

# (2) Path to the files -- their original location
ogPath = "/home/bymyself/Pictures/Pictures2021/temp"

fileList = []
for (dirpath, dirnames, filenames) in walk(ogPath):
    fileList.extend(filenames)
    break

# (3) Choose Mode
mode = input("[p]icture or [v]ideo wallpaper?\n").lower()
if "p" not in mode:
    import subprocess


    
fileNumberIdentifier = 1
for fName in fileList:
    
    # The Wallpaper Folder being Put in System/Resources
    codeLength = 0
    if "." in str(fName):
        nameParts = fName.split(".")
        codeLength = len(nameParts[len(nameParts)-1])
    nameNoCode = str(fName)[:(-1 * codeLength)]
    folder = tag + "_" + str(fileNumberIdentifier) + "_" + nameNoCode
    folder = folder.replace(" ", "")
    illegalCharacters = ["#", "%", "&", "{", "}", "\\", "<", ">", "*", "?", "/", "$", "ﾉ",\
                         "!", "'", '"', ":", "@", "+", "~", "`", "|", "=", "(", ")", ".", "-"]
    for character in illegalCharacters:
        if character in folder:
            folder = folder.replace(character, "_")
    os.system("mkdir " + folder)
    
    # Config File
    cFileChoice = "configVideo"
    if "p" in mode:
        cFileChoice = "configPicture"
    config = open(cFileChoice, "r")
    lines = config.readlines()
    if "p" not in mode:
        lines[2] = "VideoFileName=" + str(fName) + "\n"
    cLocation = folder + "/" + "config"
    newConfig = open(cLocation, "w")
    for _ in lines:
        newConfig.write(_.strip("\n") + "\n")
    newConfig.close()

    # Copy Original Picture/Video to New BG Folder
    initialLoc = ogPath + "/" + "'" + str(fName) + "'"
    os.system("cp " + initialLoc + " " + folder)
    
    # For Videos: Generate Thumbnail
    if "p" not in mode:
        tempName = "aaaaaaaaaaaaaaa"
        while tempName in fileList:
            tempName += "z"
        tempName += "." + str(nameParts[len(nameParts)-1])
        tempName = tempName.replace(" ","")
        tempCreateCmd = "mv " + folder + "/" + "'" + fName + "'" + " " + folder + "/" + tempName
        os.system(tempCreateCmd)
        video_input_path = folder + "/" + tempName
        img_output_path = folder + "/wallpaper.jpg"
        subprocess.call(['ffmpeg', '-i', video_input_path, '-ss', '00:00:05.000', '-vframes', '1', img_output_path])
        backToOgName = "mv " + video_input_path + " " + folder + "/" + "'" + fName + "'"
        os.system(backToOgName)
        
    # For Pictures: Rename img file to 'wallpaper.jpg' (required)
    if "p" in mode:
        locPic = folder + "/" + "'" + fName + "'"
        filecode = "jpg"
        possibleFilecodes = ["jpg", "png", "tif", "raw", "eps", "gif", "psd", "xcf", \
                             "ai", "cdr", "bmp", "jpeg", "cr2", "nef", "orf", \
                             "sr2", "jpe", "jif", "jfif", "jfi", "webp", "k25", \
                             "nrw", "arw", "dib", "heif", "heic", "ind", "indd", \
                             "indt", "jp2", "j2k", "jpf", "jpx", "jpm", "mj2", \
                             "svg", "svgz"]
        for code in possibleFilecodes:    
            if code in str(fName)[-5:]:
                filecode = code
        if str(fName)[-3:] not in possibleFilecodes and str(fName)[-4:] not in possibleFilecodes and str(fName)[-5:] not in possibleFilecodes:
            print("can't get file type/code in original file for:  " + str(fName))
            print("Make sure it is a picture file")
            quit()
        newName = folder + "/" + "wallpaper." + filecode
        renamePicCommand = "mv " + locPic + " " + newName
        os.system(renamePicCommand)
    
    # Move to Resources System Folder (make sure sudo password check is not enabled)
    mvToSystemCommand = "sudo mv " + folder + " /System/Resources/Komorebi"
    os.system(mvToSystemCommand)
    
    fileNumberIdentifier+=1
    
    ### Uncomment to Delete Original Files
    # os.systemm("sudo rm " + initialLoc)
        

###
### Deleting Folders in System/Resources incase of mistake
### (1) comment out the stuff above EXCEPT the variables "tag" and "ogPath"
### (2) un-comment the stuff below then run
###

# folderID = 1
# for i in fileList
#     folder_name_del = tag + "_" + str(folderID) + "_*"
#     deleteCommand = "sudo rm -r /System/Resources/Komorebi/" + folder_name_del
#     os.system(deleteCommand)
#     folderID += 1

# Delete all quickly: "sudo rm -r $TAGNAME$*"
