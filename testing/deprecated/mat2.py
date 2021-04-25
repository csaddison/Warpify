# 3/23/21

import numpy as np

class shape:
    width = 2
    height = 3
    depth = 3

src = np.array([    [[[10, 2], 11, 12], [13, 14, 15], [16, 17, 18]],
                    [[20, 21, 22], [23, 24, 25], [26, 27, 28]],
                    [[30, 31, 32], [33, 34, 35], [36, 37, 38]]
])

dim = np.array([    [[10, 11], [13, 14], [16, 17]],
                    [[20, 21], [23, 24], [26, 27]],
                    [[30, 31], [33, 34], [36, 37]]
])                   

wipeHorizontal = True
wipeVertical = False

# wipeVertical = True
# wipeHorizontal = False

xx, yy = np.mgrid[0:shape.height, 0:shape.width]
images = []
displacement = 1

if wipeHorizontal:
    coords = yy
elif wipeVertical:
    coords = xx

# (index / width) * displacement
warp_mask = np.round((coords / (shape.width - 1)) * displacement).astype(int)

for frame in range(len(src) - displacement):
    print("---- NEW FRAME -----")
    time = np.add(warp_mask, frame)
    print(time)
    x = src[time, xx, np.arange(shape.width)]
    print(x)
    images.append(x)
