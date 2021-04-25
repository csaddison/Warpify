#
# 3/23/21

import cv2
import glob

directory = r'./images/'
reel = [cv2.imread(file) for file in glob.glob(directory + '*.png')]
reel = sorted(reel)

height, width, layers = reel[0].shape
size = (width,height)
fps = 30

out = cv2.VideoWriter('test.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
for frame in reel:
    out.write(frame)

out.release()