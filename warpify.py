#
# Main app module
# 4/23/21

###############################################################################\

from sys import exit
from os import startfile
from time import sleep
import math

from pyfiglet import Figlet

from dependencies.slitscan import SlitScan
from dependencies.timer import TimeThis

###############################################################################\

def _FindLargerTexture_(size):
    return int(math.pow(2, math.ceil(math.log(size)/math.log(2))))

def _PrintTitle_(title):
    print(Figlet(font='chunky').renderText(title))

def _FormatFolderInput_(input):
    if not input[-1] == "\\":
        return input + "\\"
    else:
        return input

def _Launch_():

    delay = 0.7

    source_folder = _FormatFolderInput_(input("What is the source folder?\n"))
    source_file = input("Pick the file you want to warp:\n")
    print("\n")
    sleep(delay)
    warp = SlitScan(source_folder + source_file)
    sleep(delay)

    while True:
        print("\n")
        displacement = int(input("Set displacement (in # of frames):\n"))
        reverse = input("Reverse time: yes, no?\n")
        if reverse == 'yes':
            warp.ReverseTime()

        print("\n")
        style = input("Warp style: horizontal, vertical, perlin?\n")
        if style == "perlin":
            print("\n")
            print(f"Video resolution is {warp.width}x{warp.height}")
            next_size = _FindLargerTexture_(max(warp.width, warp.height))
            print(f"Texture size generated is {next_size}x{next_size}")
            sleep(delay)
            scale = int(input("Set maximum number of noise nodes:\n"))
            print("\n")
            mask = warp.GeneratePerlinMask(displacement, scale)
        else:
            print("\n")
            mask = warp.GenerateLinearMask(displacement, style)

        sleep(delay)
        print("\n")
        print("Begining slit-scan time-warp...")
        print("\n")
        sleep(delay)
        TimeThis(warp.Slice, mask)
        sleep(delay)
        print("\n")
        print("Warp complete, rendering results to video...")
        print("\n")
        sleep(delay)

        fps = int(input("Set output fps:\n"))
        filename = input("Set destination file:\n") + ".avi"
        print(f"File will be saved as {filename} in this script's root folder\n")
        sleep(delay)
        warp.Render(filename, fps)
        sleep(delay)
        print("\n")
        print("Video complete!")
        will_view = input("Would you like to view your video: yes, no?\n")
        if will_view == "yes":
            startfile(filename)
        
        print("\n")
        sleep(delay)
        will_continue = input("Warp again: yes, no?\n")
        if will_continue == 'no':
            print("Slit-scan over, shutting down...")
            sleep(2)
            break

        else:
            print("\n")
            change = input("Change source: file, folder, none?\n")
            if change == "none":
                continue
            else:
                if change == "folder":
                    source_folder = FormatFolderInput(input("New folder?\n"))
                source_file = input("New file?\n")
                warp = TimeThis(SlitScan, source_folder + source_file)


if __name__ == "__main__":
    _PrintTitle_("Warpify")
    _Launch_()
    exit()

