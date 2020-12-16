#reference : https://www.pyimagesearch.com/2014/12/29/accessing-individual-superpixel-segmentations-python/
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from skimage.segmentation import felzenszwalb, slic, quickshift, watershed
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float

img_old = plt.imread('../VGG16/mug.jpg')

print(type(img_old))

segments_slic = slic(img_old, n_segments=50, compactness=10, sigma=1)
#segments_felzenszwalb= felzenszwalb(img_old, scale=100, sigma=0.5, min_size=50)

plt.imshow(img_old)
plt.waitforbuttonpress(0)

plt.imshow(segments_slic)
plt.waitforbuttonpress(0)

plt.imshow(mark_boundaries(img_old,segments_slic))
plt.waitforbuttonpress(0)

modified_image = mark_boundaries(img_old,segments_slic)
plt.imshow(modified_image)
plt.waitforbuttonpress(0)

