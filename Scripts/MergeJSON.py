import json
import glob

result = []
for f in glob.glob("*.json"):
    with open(f, "rb") as infile:
        result.append(json.load(infile))

with open("merged_file.json", "wb") as outfile:
     json.dump(result, outfile)