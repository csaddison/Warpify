#
# Slit-Scan Compositing
# 4/26/20

###############################################################################

# Imports
import cv2
import numpy as np
import os
from os.path import isfile, join
import time
from benchmark import Timer
# from PIL import Image

# Initializing global variables
source = './sources/swan.mp4'
displacement = 60
warpRows = True

filename = 'test.avi'
fps = 60

###############################################################################

# Opening source file and importing frames
def import_frames(video):
    cap = cv2.VideoCapture(video)
    frames = []
    current_frame = 0
    while(True): 
        ret, frame = cap.read()
        # Continues creating frames if more remain
        if ret:
            frames.append(frame)
            current_frame += 1
        else: 
            break
    # Releases file once complete
    cap.release() 
    cv2.destroyAllWindows()
    return frames

###############################################################################

image_sequence = import_frames(source)
video_height = int(image_sequence[0].size / (3 * ( image_sequence[0][0].size / 3 )))
video_width = int(( image_sequence[0][0].size / 3 ))
size = (video_width, video_height)

# Slicing image
def noScopeSlice():
    for current_frame, _ in enumerate(image_sequence):
        if warpRows:
            for row in range(video_height):
                reference_frame = int(current_frame + ( (row / video_height) * displacement ))

                if reference_frame >= len(image_sequence):
                    break
                    # image_sequence[current_frame][row] = image_sequence[-1][row]
                else:
                    image_sequence[current_frame][row] = image_sequence[reference_frame][row]
        else:
            for column in range(video_height):
                reference_frame = int(current_frame + ( (column / video_width) * displacement ))

                if reference_frame >= len(image_sequence):
                    break
                    # image_sequence[column][current_frame] = image_sequence[column][-1]
                else:
                    # print(column, current_frame, reference_frame)
                    image_sequence[current_frame][:][column] = image_sequence[reference_frame][:][column]

###############################################################################

t1 = time.time()
noScopeSlice()
t2 = time.time()
print("runtime is" + str(t2-t1))
out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for frame in image_sequence:
    # writing to a image array
    out.write(frame)
out.release()