#
# Benchmarking Performance with Time Slicing Options
# Project ID -040221

###############################################################################\

import numpy as np
from slitScan import Mask, SlitScan
from PIL import Image, ImageFilter
# import noise
from timer import Timer
import IPython

###############################################################################\

def UsePerlin(displacement, style, texture):
    print("USING " + style + " NOISE...")
    tex = Image.open(texture).convert('L')
    xx, yy = np.mgrid[0:tex.height, 0:tex.width]
    mask = np.asarray(tex)
    mask = (mask - np.amin(mask)) / (np.amax(mask) - np.amin(mask))
    mask = np.floor(mask * displacement).astype('int')
    print("DONE")
    return Mask(displacement, mask, xx, yy)

@Timer
def SLICE(video, indexing):
    video.Slice(indexing)

###############################################################################\

source = './sources/Untitled.mp4'
displacement = 12 #frames
direction = "vertical"
# fileA = "slice.avi"
# fileB = "swap.avi"
filename = "warp.avi"
isHD = True
isFk = False
fps = 60
style = "surf"


print("\n")
print("Begining slit-scan time-warp...")
warp = SlitScan(source)
# warp.frames = np.flipud(warp.frames) # Reversing time for this example
if style == "perlin":
    if isFk:
        mask = UsePerlin(displacement, style, "4k.png")
    else:
        mask = UsePerlin(displacement, style, "tex-1080-3.png" if isHD else "tex480.png")
elif style == "surf":
    mask = UsePerlin(displacement, style, "noiseTexture.png")
else:
    mask = warp.GenerateLinearMask(displacement, direction)
SLICE(warp, mask)
warp.Render(filename, fps)

# IPython.embed()

###############################################################################\

# print("\n")
# print("Timing for-loop method...")
# Timer(warp.Swap(mask))
# warp.Render(fileB, fps)

# perl = noise.Perlin(2, 1024)
# img = Image.fromarray(perl, 'L')
# img = img.filter(ImageFilter.GaussianBlur(3))
# img.save('noise.png')
# img.show()

# print(
#     sys.getsizeof(warp),
#     sys.getsizeof(warp.frames),
#     sys.getsizeof(warp.warped),
#     sys.getsizeof(mask)
# )