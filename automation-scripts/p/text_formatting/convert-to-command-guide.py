thisString = """animehd
animemoon
megashots
megaanime
mega2"""

newString = thisString.split("\n")

part1 = "sudo cp -r "
part2 = " /System/Resources/Komorebi;"

part3 = "cd ..; cd "
part4 = "; sudo mv thumb.jpg wallpaper.jpg;"

import os

for _ in newString:
    print(part3 + _ + part4)
#     print(part3 + _ + part4)
    