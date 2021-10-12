#!/usr/bin/env python

# https://stackoverflow.com/questions/56905592
# Automatic contrast and brightness adjustment of a color photo of a sheet of paper with OpenCV

import sys

if len(sys.argv) != 3:
  print(f"usage: {sys.argv[0]} inputPath outputPath")
  sys.exit(1)

inputPath = sys.argv[1]
outputPath = sys.argv[2]

# fireant
# https://stackoverflow.com/a/57067002/10440128

from skimage.filters import threshold_yen
from skimage.exposure import rescale_intensity
from skimage.io import imread, imsave

img = imread(inputPath)

yen_threshold = threshold_yen(img)
bright = rescale_intensity(img, (0, yen_threshold), (0, 255))

imsave(outputPath, bright)
