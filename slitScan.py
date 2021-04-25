#
# Slit-Scan Compositor v2
# 10/3/20

###############################################################################

# Imports
import cv2
import numpy as np
import os
from os.path import isfile, join
import sys
import noisify

###############################################################################\

class Mask:
    def __init__(self, displacement, mask, xx, yy):
        self.displacement = displacement
        self.mask = mask
        self.xx = xx
        self.yy = yy
        
###############################################################################\

class SlitScan:
    def __init__(self, source):
        print("INITIALIZING VIDEO...")
        # Opening source file and importing frames
        vcap = cv2.VideoCapture(source)
        self.frames = []
        while(True): 
            ret, frame = vcap.read()
            # Continues creating frames if more remain
            if ret:
                self.frames.append(frame)
            else: 
                break
        # Getting resolution information
        self.width = int(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))      # width
        self.height = int(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))        # height
        self.depth = int(vcap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = round(vcap.get(cv2.CAP_PROP_FPS))
        # Releases file once complete
        vcap.release()
        cv2.destroyAllWindows()
        self.frames = np.array(self.frames)
        print("DONE")
        print("Video is " + str(self.depth) + " frames before warp.")
    
    def ReverseTime(self):
        self.frames = np.flipud(self.frames)

    def GenerateLinearMask(self, displacement, wipe="horizontal"):
        print("GENERATING MASK...")
        xx, yy = np.mgrid[0:self.height, 0:self.width]
        if wipe == "horizontal":
            mask = np.round((xx / (self.width - 1)) * displacement).astype(int)
        elif wipe == "vertical":
            mask = np.round((yy / (self.width - 1)) * displacement).astype(int)
        else:
            raise Exception("Mask can only be horizontal or vertical wipe.")
        print("DONE")
        print("Mask gradient direction: " + str(wipe))
        return Mask(displacement, mask, xx, yy)

    def GeneratePerlinMask(self, displacement, nodes):
        print("USING PERLIN NOISE...")
        xx, yy = np.mgrid[0:self.height, 0:self.width]
        mask = noisify.Perlin(self.height, self.width).Smoothify(nodes)
        # return Mask(displacement, mask, xx, yy)
        return True

    def Slice(self, mask):
        print("STARTING SLICE...")
        span = np.arange(self.width)
        self.warped = []
        for frame in range(self.depth - (mask.displacement + 1)):
            time = np.add(mask.mask, frame)
            warped_frame = self.frames[time, mask.xx, span]
            self.warped.append(warped_frame)
            # cv2.imwrite('./images/frame' + str(frame) + '.png', warped_frame)
        print("DONE")

    def Render(self, filename, fps, save_frames=False):
        print("CONVERTING FILE...")
        size = (self.width, self.height)
        video = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
        if save_frames:
            frame_num = 0
            for frame in self.warped:
                cv2.imwrite('./images/frames/frame' + str(frame_num) + '.png', frame)
                frame_num += 1
        else:
            for frame in self.warped:
                video.write(frame)
        video.release()
        print("DONE")