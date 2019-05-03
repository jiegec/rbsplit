#!/usr/bin/env python3
from PIL import Image
import sys
import numpy as np
import scipy.misc

diff = 2
im = Image.open(sys.argv[1])
data = im.load()
(width, height) = (im.size[0], im.size[1])

rgb = np.zeros((width, height, 3), dtype=np.uint8)
for i in range(width):
    for j in range(height):
        r, g, b, _ = data[i, j]
        rgb[i][j][0] = r
        rgb[i][j][1] = g
        rgb[i][j][2] = b

new_rgb = np.zeros((height, width - 2 * diff, 3), dtype=np.uint8)
for i in range(width - 2*diff):
    for j in range(height):
        new_rgb[j][i][0] = rgb[i][j][0]
        new_rgb[j][i][1] = rgb[i+2*diff][j][1]
        new_rgb[j][i][2] = rgb[i+2*diff][j][2]

scipy.misc.imsave('output.png', new_rgb)

