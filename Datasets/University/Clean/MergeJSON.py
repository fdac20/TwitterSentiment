# Run this script in directory with JSON

import json

# files = ['clean_DondePlowman.json', 'clean_randyboyd.json', 'clean_tucarpenter.json', 'clean_UTIA_SVP.json', 'clean_KC4UTM.json', 
#               'clean_utknoxville.json', 'clean_utk_tce.json', 'clean_utkdos.json', 'clean_ut_admissions.json', 'clean_utk_asc.json', 'clean_UTKCEHHS.json',
#               'clean_utk_cfs.json', 'clean_UTKStudentLife.json', 'clean_UTKCoAD.json', 'clean_UTKSOM.json', 'clean_tennalum.json', 'clean_utknursing.json', 'HaslamUT.json']

# dondeplowman and haslamut broken
files = ['clean_randyboyd.json', 'clean_tucarpenter.json', 'clean_UTIA_SVP.json', 'clean_KC4UTM.json', 
              'clean_utknoxville.json', 'clean_utk_tce.json', 'clean_utkdos.json', 'clean_ut_admissions.json', 'clean_utk_asc.json', 'clean_UTKCEHHS.json',
              'clean_utk_cfs.json', 'clean_UTKStudentLife.json', 'clean_UTKCoAD.json', 'clean_UTKSOM.json', 'clean_tennalum.json', 'clean_utknursing.json']


head = []
with open("combined_uni_data.json", "w") as outfile:
    for f in files:
        with open(f, 'rb') as infile:
            file_data = json.load(infile)
            head += file_data
    json.dump(head, outfile)