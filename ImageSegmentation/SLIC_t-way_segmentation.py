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

input_test_file = '/Users/Jagan/Desktop/XAI_Tool_Project/test_files/ImageSegmentation-n25.csv'
#input_test_file = '/Users/Jagan/Desktop/XAI_Tool_Project/test_files/ImageSegmentation-n20.csv'
#input_test_file = '/Users/Jagan/Desktop/BEN_n25/core_dervied_minimal.csv'
segments_for_each_test_case = []

def read_csv_file(test_file):
    test_cases = []
    with open(test_file) as input_csv_file:
        readCSV = csv.reader(input_csv_file, delimiter=',')
        counter = 1
        ''' to skip first seven rows in ACTS file, calling next() for seven times'''
        next(readCSV)  # skip a row in input CSV file
        next(readCSV)  # skip a row in input CSV file
        next(readCSV)  # skip a row in input CSV file
        next(readCSV)  # skip a row in input CSV file
        next(readCSV)  # skip a row in input CSV file
        next(readCSV)  # skip a row in input CSV file
        next(readCSV)
        for row in readCSV:
            print(row)
            test_cases.append(row)

        output_true = []
        for tc in test_cases:
            temp_list = []
            for i, e in enumerate(tc):
                if e == 'false':
                    temp_list.append(i)
            output_true.append(temp_list)
        return output_true


def read_txt_file(testfile):
    test_cases_from_txt_file = []
    final_test_cases = []

    input_file = open(testfile,"r")  # open the text file

    for i in range(3):
        next(input_file)  # skip first two lines
    for line in input_file: #  reading from text file (line by line)
        test_cases_from_txt_file.append(list(line.strip().split(",")))

    for test in test_cases_from_txt_file:
        final_test_cases.append(test[1: -1])
    input_file.close()

    # check for masking segments
    output_false = []
    for tc in final_test_cases:
        temp_list = []
        for i, e in enumerate(tc):
            print e
            if e == ' false ':
                temp_list.append(i)
        output_false.append(temp_list)
        print(temp_list)
    return output_false
    #print(output_false)


# segments_for_each_test_case = read_csv_file(input_test_file)


# image = cv2.imread('../VGG16/test_dataset/ILSVRC2017_test_00000008.JPEG')
# number_of_segments = 25
#
# # apply segmentation to the source image
# segments = slic(img_as_float(image), n_segments = number_of_segments, sigma = 5)
# print(np.unique(segments)) # number of unique segments
# #segments = slic(img_as_float(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), n_segments = number_of_segments, sigma = 5)
#
# # mask image
# mask = np.zeros(image.shape[:2], dtype = 'uint8')
#
# test_counter=1
# for test_case in segments_for_each_test_case:
#     mask = np.zeros(image.shape[:2], dtype='uint8')
#     print('testcase:    ', test_case)
#     for segment_number in test_case:
#         mask[segments == segment_number] = 255
#         print(segment_number)
#     file_name = 'Original_t-way_'+str(test_counter)+'_n'+str(number_of_segments)+'.jpg'
#     #file_name = 'test_case_' + str(test_counter) + '_n' + str(number_of_segments) + '.jpg'
#     #output_file_destination = '/Users/Jagan/Desktop/XAI_Tool_Project/segment_size_25/test_images/core_dervied_minimal'+file_name
#     output_file_destination = '/Users/Jagan/Desktop/BEN_n25/Test_image_8/images/'+file_name
#     cv2.imwrite(output_file_destination, cv2.bitwise_and(image, image, mask=mask))
#     #cv2.imshow(str(test_case), cv2.bitwise_and(image, image, mask=mask))
#     #cv2.waitKey(0)
#     print('end of test case', test_counter)
#     test_counter = test_counter + 1

def generate_testcase(test_file):

    file_extension = os.path.splitext(test_file)
    image = cv2.imread('../VGG16/test_dataset/ILSVRC2017_test_00000008.JPEG')
    number_of_segments = 25
    output_directory = '/Users/Jagan/Desktop/BEN_n25/Test_image_8/images/iteration1/'
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
        test_file_name = 'file_name' + str(test_counter) + '_n' + str(number_of_segments) + '.jpg'
        # file_name = 'test_case_' + str(test_counter) + '_n' + str(number_of_segments) + '.jpg'
        # output_file_destination = '/Users/Jagan/Desktop/XAI_Tool_Project/segment_size_25/test_images/core_dervied_minimal'+file_name
        output_file_destination = output_directory + test_file_name
        cv2.imwrite(output_file_destination, cv2.bitwise_and(image, image, mask=mask))
        # cv2.imshow(str(test_case), cv2.bitwise_and(image, image, mask=mask))
        # cv2.waitKey(0)
        print('end of test case', test_counter)
        test_counter = test_counter + 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_file', type=str)

    args, unknown = parser.parse_known_args()
    generate_testcase(args.test_file)