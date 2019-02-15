#!/usr/bin/env python

import os
import argparse
import numpy as np
# import pandas as pd
parser = argparse.ArgumentParser()
parser.add_argument("path_to_data")
args = parser.parse_args()

myfilename = args.path_to_data

if os.path.isfile(myfilename):
    print("Yes, you have a file")
    new_lists = []
    print('PART 1')
    with open(myfilename, 'r') as file_handle:
        for line in file_handle.readlines():
            # line_clean = line.replace('   ', ' ').replace('  ', ' ')
            # line_clean = line_clean.strip()
            # values = line_clean.split(' ')
            values = line.split(',')
            print(values)
            casted_lines = []
            for value in values:
                if value == '?':
                    print('missing value, replace by 0')
                    value = 0
                elif '.' not in value:
                    print('{0} will be casted to integer'.format(type(value)))
                    value = int(value)
                else:
                    print('{0} will be casted to float'.format(type(value)))
                    value = float(value)
                casted_lines.append(value)
            print(casted_lines)
            new_lists.append(casted_lines)

    print('PART 2')
    num_of_cols = len(new_lists[0])
    columns =[]
    for i in range(num_of_cols):
        col_i = []
        for row in new_lists:
            col_i.append(row[i])
        columns.append(col_i)

    # display on screen
    for i in range(num_of_cols):
        # to view better, print 10 first values of each column:
        print('column {0} is {1}'.format(i+1, columns[i][0:10]))
        # print whole columns
        # print('column {0} is {1}'.format(i + 1, columns[i]))
    # print('finished!')

##### this is solution for class 4 #####
    print(20*'*')
    print('PARTS FOR CLASS 04')
    print(20*'*')
    new_array = np.array(new_lists)
    num_of_samples, num_of_features = new_array.shape
    print('Summary: number of samples is {0} and number of features is {1}'.format(num_of_samples, num_of_features))
    # compute mean and standard deviation of each features:
    for feature_id in range(1,num_of_features):
        feature = new_array[:, feature_id]
        print('feature {0:2d}: mean = {1:2.3f}, standard deviation = {2:2.3f}'.format(feature_id, feature.mean(), feature.std()))
else:
  print ('Boo, no files for you')
print('FINISHED')

