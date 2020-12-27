import fnmatch
import glob
import math
import os
import re
import shutil
from shutil import copyfile

source_location = '/Volumes/Jagan-SSD/Research-work/ImageNetDataset_2017/ILSVRC/Data/DET/test/'
destination_location = '/Users/Jagan/Desktop/XAI_Tool_Project/RandomlySelectedImages/'

fileName_part1 = 'ILSVRC2017_test_0000'
fileName_extension = ".JPEG"

inputFile = '/Users/Jagan/Desktop/XAI_Tool_Project/random_selection.txt'


# read from the randomly selected image list
randomly_selected_images = open(inputFile, 'r')
for image in randomly_selected_images:  # reading from text file (line by line)
    fileName_part2 = image.strip()
    source_file = source_location+fileName_part1 + fileName_part2.zfill(4)+fileName_extension
    destination_file =  destination_location + fileName_part1 + fileName_part2.zfill(4)+fileName_extension
    #print(source_file)
    #print (destination_file)
    shutil.copyfile(source_file, destination_file)


