#!/usr/bin/env python3
import csv
import json
import numpy as np
import pandas as pd

def extraction(infile, data_count):
    file = open(infile, encoding='utf-8')
    json_list = []
    for i in range(data_count):
        json_list.append(json.loads(file.readline()))

    file.close()
    df = pd.DataFrame(json_list)
    return df

counter = 0
attempt = 0
while counter < 10:
    counter += 1
    if attempt == 0:
        print()
        infile = input("Please enter the JSON file name : ")
        data_count = int(input("Please enter the number of data you want to extract : "))
        print()
        print(infile, data_count, counter, attempt)
        attempt += 1
        main_dataframe = extraction(infile, data_count)
        print()
        print("Your DataFrame Shape : ", main_dataframe.shape)
    else:
        print()
        check = input("Do you want to extract another JSON file (Y/N) : ")
        if check == "Y":
            print()
            infile = input("Please enter the JSON file name : ")
            data_count = int(input("Please enter the number of data you want to extract : "))
            print()
            print(infile, data_count, counter, attempt)
            attempt += 1
            next_dataframe = extraction(infile, data_count)
            print("Your DataFrame Shape : ", next_dataframe.shape)
            main_dataframe = main_dataframe.append(next_dataframe)
        else:
            print()
            print("Your Final DataFrame Shape : ", main_dataframe.shape)
            print()
            check = input("Do you want to save your DataFrame into CSV file (Y/N) : ")
            if check == "Y":
                print()
                csv_outfile = input("Please Enter CSV file name : ")
                main_dataframe.to_csv(csv_outfile)
                print()
                print("Done !! Thank You!!")
                print()
                counter = 10
                break
            else:
                print()
                print("Thank You !!!")
                counter = 10
                break
