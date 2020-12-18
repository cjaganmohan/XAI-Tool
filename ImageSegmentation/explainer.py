import argparse
import argparse
import csv
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
from natsort import natsorted
from skimage.segmentation import mark_boundaries
from skimage.segmentation import slic
from skimage.util import img_as_float

def generate_explaination(testFile):
    file_extension = os.path.splitext(test_file)
    image = cv2.imread('../VGG16/test_dataset/ILSVRC2017_test_00000005.JPEG')
    number_of_segments = 25
    output_directory = '/Users/Jagan/Desktop/BEN_n25/Test_image_5/Images/explainer/'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    if file_extension[1] == '.csv':
        segments_for_each_test_case = read_csv_file(test_file)
        file_name = 'Original_t-way_'
    elif file_extension[1] == '.txt':
        segments_for_each_test_case = read_txt_file(test_file)
        file_name = 'BEN_test_case_'

    # apply segmentation to the source image
    segments = slic(img_as_float(image), n_segments=number_of_segments, sigma=5)
    print(np.unique(segments))  # number of unique segments
    # segments = slic(img_as_float(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), n_segments = number_of_segments, sigma = 5)

    # mask image
    mask = np.zeros(image.shape[:2], dtype='uint8')

    test_counter = 1
    for test_case in segments_for_each_test_case:
        mask = np.zeros(image.shape[:2], dtype='uint8')
        print('testcase:    ', test_case)
        for segment_number in test_case:
            mask[segments == segment_number] = 255
            print(segment_number)
        test_file_name = file_name + str(test_counter) + '_n' + str(number_of_segments) + '.jpg'
        output_file_destination = output_directory + test_file_name
        cv2.imwrite(output_file_destination, cv2.bitwise_and(image, image, mask=mask))
        # cv2.imshow(str(test_case), cv2.bitwise_and(image, image, mask=mask))
        # cv2.waitKey(0)
        print('end of test case', test_counter)
        test_counter = test_counter + 1

def generate_segments():
    core_list = []
    core_test_case = "false , true , false , false , false , false , false , false , true , false , false , false , false , false , false , false , false , false , false , false , false , false , false"
    core_list.append(list(core_test_case.strip().split(",")))

    for i, segement in core_list:
        if segement[i] == ' false ':
            core_list.append[i]
    print core_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_file', type=str)

    args, unknown = parser.parse_known_args()
    #generate_explaination(args.test_file)
    generate_segments()