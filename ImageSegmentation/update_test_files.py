import argparse
import csv
import os
from natsort import natsorted


def updateTestFile(updateFile, result):

    test_details = []
    test_results = []

    result_file = open(result, 'r')
    for test in result_file:  # reading from text file (line by line)
        test_details.append(list(test.strip().split(",")))

    for status in test_details:
        #print status
        #print status [2]
        test_results.append(status[2])
    result_file.close()

    f = open(updateFile,'a+')
    f.write("\n")
    f.write("Results")
    f.write("\n")
    f.write("Test #,result")
    f.write("\n")
    output = " "
    for i in range(10):
        output = str(i)+ ', ' +str(test_results[i])
        f.write(output)
        f.write("\n")
    f.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--update_file', type=str)
    parser.add_argument('--result_file', type=str)

    args, unknown = parser.parse_known_args()
    updateTestFile(args.update_file,args.result_file) #, args.group, args.file_type, args.output_path)