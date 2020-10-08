import csv

with open('./Datasets/output_got.csv', 'r') as userFile:
    userFileReader = csv.reader(userFile)

    for row in userFileReader:
        print (row)