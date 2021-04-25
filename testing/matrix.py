# Displacement Vectorization Test
# 3/13/21

import numpy as np

src = np.array([    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                    [[20, 21, 22], [23, 24, 25], [26, 27, 28]],
                    [[30, 31, 32], [33, 34, 35], [36, 37, 38]]  ])

dim = np.array([    [10, 11, 12],
                    [20, 21, 22],
                    [30, 31, 32]    ])


shape = (3,3,3)
identity_3d = np.zeros(shape)
idx = np.arange(shape[0])
identity_3d[idx, idx, :] = 1



tm = [[2,0,0], [1,1,2], [2,1,0]]
naught = np.zeros((3,3), int)
ones = np.ones((3,3), int)
twos = 2 * ones
time = [ [[2,0,0],[0,1,2],[0,1,2]], [[1,2,0],[1,2,0],[1,2,0]], [[2,1,0],[2,1,0],[2,1,0]] ]

flat_time_mask =  [[0,1,0], [1,0,0], [2,1,2]]
flat_pixel_mask = [[0,1,2], [0,1,2], [0,1,2]]
flat_x = dim[time_mask, pixel_mask]

time_mask = []
pixel_mask = []
pix = np.repeat(np.arange(shape.width), shape.height).reshape((3, 3))

class shape:
    width = 3
    height = 3
    depth = 3

xx, yy = np.mgrid[0:shape.width, 0:shape.height]

x = src[[naught,ones,twos], xx, yy]
x = src[tm, xx, [0,1,2]]

a = [1,2,3]
b = ["one", "two", "three"]
c = dict(zip(b,a))
