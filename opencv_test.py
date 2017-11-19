from __future__ import print_function
import numpy as np
import matplotlib
from matplotlib import image
from matplotlib import pyplot as plt
import cv2

import numpy as np
import argparse
import cv2

def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")

	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)

# construct the argument parse and parse the arguments

# load the original image
# a = image.imread('frame-000022.png')
# b = image.imread('frame-000023.png')






image = 'frame-000023.jpg'

original = cv2.imread(image)

# loop over various values of gamma


	# apply gamma correction and show the images

adjusted = adjust_gamma(original, gamma=0.8)
cv2.imwrite('frame-0000233.jpg' , adjusted)
# cv2.imshow("Images", np.hstack([original, adjusted]))



