#
# Main app module
# 4/23/21

###############################################################################\

import numpy as np
from slitScan import Mask, SlitScan
from timer import Timer, TimeThis
import sys
from pyfiglet import Figlet

###############################################################################\

def PrintTitle(title):
    print(Figlet(font='chunky').renderText(title))

def FormatFolderInput(input):
    if not input[-1] == "\\":
        return input + "\\"
    else:
        return input

def Launch():

    source_folder = FormatFolderInput(input("What is the source folder?\n"))
    source_file = input("Pick the file you want to warp:\n")
    # warp = SlitScan(source)
    warp = TimeThis(SlitScan, source_folder + source_file)

    while True:
        displacement = int(input("Set displacement (in # of frames):\n"))
        reverse = input("Reverse time: yes, no?\n")
        if reverse == 'yes':
            warp.ReverseTime()

        style = input("Warp style: horizontal, vertical, perlin?\n")
        if style == "perlin":
            print("Video resolution is " + str(warp.width) + "x" + str(warp.height))
            scale = int(input("Set maximum number of noise nodes:\n"))
            mask = warp.GeneratePerlinMask(displacement, scale)
        else:
            mask = warp.GenerateLinearMask(displacement, style)

        print("Begining slit-scan time-warp...")
        # warp.Slice(mask)
        TimeThis(warp.Slice, mask)

        fps = int(input("Set output fps:\n"))
        filename = "warp.avi"
        # warp.Render(filename, fps)
        TimeThis(warp.Render, filename, fps)
        
        will_continue = input("Continue: yes, no?\n")
        if will_continue == 'no':
            print("Slit-scan over, shutting down...")
            break

        change = input("Change source: file, folder, none?\n")
        if change == "none":
            continue
        else:
            if change == "folder":
                source_folder = FormatFolderInput(input("New folder?\n"))
            source_file = input("New file?\n")
            warp = TimeThis(SlitScan, source_folder + source_file)
    sys.exit()


if __name__ == "__main__":
    PrintTitle("Warpify")
    Launch()

