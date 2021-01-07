import argparse
import csv
import os
import pandas as pd
import pdb
import shutil
import sys
from skimage.util import img_as_float

#from collections import OrderedDict

failure_inducing_combo = 'S_3=true, S_15=true'
failure_inducing_combo.replace(" ","")
segments_list = failure_inducing_combo.strip(' ').split(", ")

failure_inducing_combinations = {}
segments_to_check = []

core_member = []
derived_members =[]
core_and_derived_members = []

for segment in segments_list:
    segId =  segment.split("=")[0]
    masking = segment.split("=")[1]
    failure_inducing_combinations [segId] = [masking]


#print (failure_inducing_combinations ['S_2'])
#print failure_inducing_combinations ['S_3']

for inducing_segment in failure_inducing_combinations:
    segments_to_check.append(inducing_segment.replace("S_",""))



def generate_core_derived(testfile):
    # this is an initial version -- this implementation will work only for test files with 10 testscase.
    # ******* needs refactoring in future release   *****
    # reference - https://stackoverflow.com/questions/2081836/reading-specific-lines-only

    test_cases_from_txt_file = []
    final_test_cases = []

    input_file = open(testfile, "r")  # open the text file
    for i in range(2):
        next(input_file)  # skip first two lines
    for line in input_file:  # reading from text file (line by line)
        if line == '\n':
            break
        test_cases_from_txt_file.append(list(line.strip().split(",")))

    for i, test in enumerate(test_cases_from_txt_file):
        if i == 0:
            final_test_cases.append(test)
        else:
            final_test_cases.append(test[:-1])
    input_file.close()


   # select core member
    core_member_found = False
    for test in final_test_cases:
        if (core_member_found == 0):
            if ((test[2] == ' true ') & (test[3] == ' true ') & (test[4] == ' true ')):
                print test
                core_member_found = True
                core_member = test[:]
                core_member.insert(len(core_member),'core')  # appending the member info
                core_and_derived_members.append(core_member)
    print core_member

    derived_members =[]
    # derived members
    print failure_inducing_combinations
    for susSegments in failure_inducing_combinations:
        temp_list = core_member[:]
        index = int(susSegments.replace("S_","")) + 1
        print temp_list
        print index
        if (temp_list[index]) == ' true ':
            temp_list[index] = ' false '
        elif (temp_list[index]) == ' false ':
            temp_list[index] = ' true '
        print 'Updated for .... index   ', index
        print temp_list
        temp_list[len(temp_list)-1] = 'derived' # appending the member info
        derived_members.append(temp_list)
        core_and_derived_members.append(temp_list)


    # print ('--------------------')
    # print (core_member)
    # print (derived_members)
    #
    # print( "   -      -----------------------        -")
    # for item in core_and_derived_members:
    #     print item
    coreDerived = '/Users/Jagan/Desktop/BEN_n25/Test_image_1950/core-derived.txt'
    f = open(coreDerived, 'w')
    f.write("Phase II ")
    f.write("\n")
    f.write("Core and derived test cases")
    f.write("\n")
    f.write("Test #,result")
    f.write("\n")
    for item in core_and_derived_members:
        output = str(item).strip('[]')
        print output
        #f.write("%s\n" % item)
        f.write(output)
        f.write("\n")
    f.close()




    #
    # # writing test to a csv file
    # with open('/Users/Jagan/PycharmProjects/XAI-Tool/ImageSegmentation/generating-core.csv','w',0) as csvfile:
    #     writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #     #writer.writerow(['File_name', 'Predicted_steering_angle'])
    #     for test in final_test_cases:
    #         writer.writerow(test)
    #
    # print (pd.__version__)
    # df = pd.read_csv('/Users/Jagan/PycharmProjects/XAI-Tool/ImageSegmentation/generating-core.csv', skipinitialspace=True)
    # print (df.head(3))
    #
    # c2 = str(df['S_2']).strip()
    #
    # print (c2)
    # #print df.query( str(df['S_2']).strip() ==  txt)
    # if c2 == ' false ':
    #     print '********'
    # # elif c2 == ' true ':
    # #     print '--------'
    # # print type (c2)
    # #
    # # datatypes = df.dtypes
    # # print datatypes
    #
    # # print ( df[
    # #             (df['S_2'] == 'false') & (df['S_5'] == 'true')
    # #         ])
    # #identify_core(temp_csv_file)

#generate_core_derived(testFile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_file', type=str)

    args, unknown = parser.parse_known_args()
    generate_core_derived(args.test_file)
