# reference - http://datahacker.rs/how-to-access-and-edit-pixel-values-in-opencv-with-python/

import cv2
import matplotlib.pyplot as plt
import numpy as np

#display image
img = cv2.imread('mug.jpg',1)
cv2.imshow(' ',img)
cv2.waitKey(0)

print(img.shape)
#modify a part of image -- gray out a specific area
img[40:80, 140:340] = [0,0,0]
cv2.imwrite('modified8_masked.jpg',img)
img[60:250, 80:120] = [0,0,0]  # length, width
cv2.imwrite('modified10_masked.jpg',img)
cv2.imshow('Modified Image',img)
cv2.waitKey(0)