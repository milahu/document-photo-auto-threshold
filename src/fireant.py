# fireant
# https://stackoverflow.com/a/57067002/10440128


from skimage.filters import threshold_yen
from skimage.exposure import rescale_intensity
from skimage.io import imread, imsave

img = imread('mY7ep.jpg')

yen_threshold = threshold_yen(img)
bright = rescale_intensity(img, (0, yen_threshold), (0, 255))

imsave('out.jpg', bright)
