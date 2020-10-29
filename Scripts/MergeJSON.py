import json

file_list = ['dondeplowman.json']

head = []
with open("result.json", "w") as outfile:
    for f in file_list:
        with open(f, 'rb') as infile:
            file_data = json.load(infile)
            head += file_data
    json.dump(head, outfile)