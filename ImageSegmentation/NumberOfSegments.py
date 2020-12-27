import argparse
import csv
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from natsort import natsorted
from skimage.segmentation import mark_boundaries
from skimage.segmentation import slic
from skimage.util import img_as_float
reload(sys)
sys.setdefaultencoding('ISO-8859-1')




def print_segments(image_path, file_name, output_path):

    test_images = []
    for root, sub_dirs, files in os.walk(image_path):
        for f in files:
            if '.jpg' in f or '.png' in f or '.JPEG' in f:
                test_images.append(os.path.join(root, f))

    test_images = natsorted(test_images)

    txt_filename = str(file_name) + '_segments' + '.txt'
    save_segment_info = str(output_path) + txt_filename
    print save_segment_info
    sys.stdout = open(save_segment_info, 'w')

    for image in test_images:
        img = cv2.imread(image)
        segments = slic(img_as_float(img), n_segments=25, sigma=5)
        print image, ',' , len(np.unique(segments)), ',' , np.unique(segments)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_location', type=str)
    parser.add_argument('--file_name', type=str)  # { name of the console output }
    parser.add_argument('--output_path', type=str)

    args, unknown = parser.parse_known_args()

    print_segments(args.image_location, args.file_name, args.output_path) #, args.group, args.file_type, args.output_path)