import argparse
import csv
import os
#from natsort import natsorted

input_test_file = '/Users/Jagan/Desktop/XAI_Tool_Project/test_files/ImageSegmentation-n50.csv'

test_cases = []

with open(input_test_file) as input_csv_file:
    readCSV = csv.reader(input_csv_file, delimiter=',')
    counter = 1
    ''' to skip first seven rows in ACTS file, calling next() for seven times'''
    next(readCSV) # skip a row in input CSV file
    next(readCSV) # skip a row in input CSV file
    next(readCSV) # skip a row in input CSV file
    next(readCSV) # skip a row in input CSV file
    next(readCSV) # skip a row in input CSV file
    next(readCSV) # skip a row in input CSV file
    next(readCSV)
    for row in readCSV:
        test_cases.append(row)

    n = test_cases.__len__()
    print(n)

    output_true = {new_list: [] for new_list in range(n)}
    output_false = {new_list: [] for new_list in range(n)}

    # Get True Count
    for i, tc in enumerate(test_cases):
        a= []
        for j, e in enumerate(tc):
            if e == 'true':
               a.append(j)
        output_true[i].append(a)

    print("True Values =")
    print(output_true)

    #export True count
    for i in range(len(output_true)):
        result_file = open('true.csv', 'a')
        result_file.write("{}{}".format(output_true[i], '\n'))

    print("\n\n")

    # Get False Cout
    for i, tc in enumerate(test_cases):
        a = []
        for j, e in enumerate(tc):
            if e == 'false':
                a.append(j)
        output_false[i].append(a)

    print("False Values = ")
    print(output_false)



    # for tc in test_cases:
    #     val = ""
    #     for i, e in enumerate(tc):
    #         if e == 'false':
    #             val = val + str(i) + ","
    #     output_false.append(val)

    #export False Count
    for i in range(len(output_false)):
        result_file = open('false.csv', 'a')
        result_file.write("{}{}".format(output_false[i], '\n'))
