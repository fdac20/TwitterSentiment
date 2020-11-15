import os
import glob
import pandas as pd

os.chdir("../Datasets/Non-University/csv/FilteredSet")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

#export to csv
combined_csv.to_csv("combinedNonUni_csv.csv", index = False)

