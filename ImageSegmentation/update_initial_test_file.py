import argparse
import csv
import os
from natsort import natsorted

def update_initial_test_file(number_of_segments):


    print ("Parameters:")
    relation_text = "[2, ("
    for i in range(number_of_segments):
        print '"S_'+str(i)+':[true, false]"'
        relation_text = relation_text + "S_" + str(i) +","
    relation_text = relation_text.rstrip(',') + ')]"'

    print("\n")
    print ("Relations:")
    print(relation_text)
    print("\n")
    print("Tests")

    print("\n")
    print("Results")
    #print("\n")
    print("Test #,result")
    output = " "
    for i in range(12):
        output = str(i) + ', fail'
        print(output)
        #print("\n")



    # with open('/Users/Jagan/Desktop/ImageSegmentation_n21-initial-output.csv', 'rb') as input_file, open('/Users/Jagan/Desktop/ImageSegmentation_n21-image519-initial-input-BENmodified.csv', 'ab') as output_csv_file:
    #     inputCSV = csv.reader(input_file, delimiter=',', quotechar='|')
    #     #writeCSV = csv.writer(output_csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #     writeCSV = csv.writer(output_csv_file)
    #
    #     header_info=[]
    #     test_info = []
    #     parameters_info = []
    #     relation_info = []
    #
    #     test_info.append(["Tests"])
    #     counter = 1
    #
    #     for row in inputCSV:
    #         if counter < 7:
    #             header_info.append(row)
    #         else:
    #             test_info.append(row)
    #         counter = counter + 1
    #
    #
    #     parameters_info.append(["Parameters:"])
    #     relation_text = "[2, ("
    #     for i in range(21):
    #         parameters_info.append(['"S_' + str(i) + ':[true, false]"'])
    #         relation_text = relation_text + "S_" + str(i) + ","
    #     relation_text = relation_text.rstrip(',') + ')]"'
    #     #
    #     # writeCSV.writerow("\n")
    #     relation_info.append(["Relations:"])
    #     relation_info.append([relation_text])
    #     # writeCSV.writerow("\n")
    #     # writeCSV.writerow("Tests")
    #
    #
    #     print header_info
    #     print parameters_info
    #     print relation_info
    #     print test_info
    #
    #
    #     # writing to the BEN input csv file
    #     # header info
    #     for hitem in header_info:
    #         writeCSV.writerow(hitem)
    #
    #
    #     # parameter and relation info
    #     for pitem in parameters_info:
    #         writeCSV.writerow(pitem)
    #
    #
    #     for ritem in relation_info:
    #         writeCSV.writerow(ritem)
    #
    #
    #     # test info
    #     for test in test_info:
    #         writeCSV.writerow(test)
    #
    #



        # next(inputCSV)
        # next(inputCSV)
        # next(inputCSV)
        # next(inputCSV)
        # next(inputCSV)
        # next(inputCSV)
        # writeCSV.writerow("Parameters:")
        # relation_text = "[2, ("
        # for i in range(21):
        #     print
        #     '"S_' + str(i) + ':[true, false]"'
        #     relation_text = relation_text + "S_" + str(i) + ","
        # relation_text = relation_text.rstrip(',') + ')]"'
        #
        # writeCSV.writerow("\n")
        # writeCSV.writerow("Relations:")
        # writeCSV.writerow(relation_text)
        # writeCSV.writerow("\n")
        # writeCSV.writerow("Tests")
        #
        #

    # test_details = []
    # test_results = []
    #
    # result_file = open(result, 'r')
    # for test in result_file:  # reading from text file (line by line)
    #     test_details.append(list(test.strip().split(",")))
    #
    # for status in test_details:
    #
    #     test_results.append(status[2])
    # result_file.close()
    #
    # f = open(updateFile,'a+')
    # f.write("\n")
    # f.write("Results")
    # f.write("\n")
    # f.write("Test #,result")
    # f.write("\n")
    # output = " "
    # for i in range(10):
    #     output = str(i)+ ', ' +str(test_results[i])
    #     f.write(output)
    #     f.write("\n")
    # f.close()




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--segments', type=int)

    args, unknown = parser.parse_known_args()
    update_initial_test_file(args.segments) #, args.group, args.file_type, args.output_path)