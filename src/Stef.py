#!/usr/bin/env python

# https://stackoverflow.com/questions/56905592
# Automatic contrast and brightness adjustment of a color photo of a sheet of paper with OpenCV

import sys

if len(sys.argv) != 3:
  print(f"usage: {sys.argv[0]} inputPath outputPath")
  sys.exit(1)

inputPath = sys.argv[1]
outputPath = sys.argv[2]

# Stef
# https://stackoverflow.com/a/57116646/10440128

import cv2, numpy as np

image = cv2.imread(inputPath)

# make mask and inverted mask for colored areas
b,g,r = cv2.split(cv2.blur(image,(5,5)))
np.seterr(divide='ignore', invalid='ignore') # 0/0 --> 0
m = (np.fmin(np.fmin(b, g), r) / np.fmax(np.fmax(b, g), r)) * 255
_,mask_inv = cv2.threshold(np.uint8(m), 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
mask = cv2.bitwise_not(mask_inv)

# local thresholding of grayscale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
text = cv2.ximgproc.niBlackThreshold(gray, 255, cv2.THRESH_BINARY, 41, -0.1, binarizationMethod=cv2.ximgproc.BINARIZATION_NICK)

# create background (text) and foreground (color markings)
bg = cv2.bitwise_and(text, text, mask = mask_inv)
fg = cv2.bitwise_and(image, image, mask = mask)

out = cv2.add(cv2.cvtColor(bg, cv2.COLOR_GRAY2BGR), fg)



cv2.imwrite(outputPath, out)
