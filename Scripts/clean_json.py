# Run this script in directory with JSON

files = ['DondePlowman.json', 'randyboyd.json', 'tucarpenter.json', 'UTIA_SVP.json', 'KC4UTM.json', 
              'utknoxville.json', 'utk_tce.json', 'utkdos.json', 'ut_admissions.json', 'utk_asc.json', 'UTKCEHHS.json',
              'utk_cfs.json', 'UTKStudentLife.json', 'UTKCoAD.json', 'UTKSOM.json', 'tennalum.json', 'utknursing.json', 'HaslamUT.json']

lastline = None

for file in files:

    with open(file,"r") as f:
        lineList = f.readlines()
        lastline=lineList[-1]

    with open(file,"r") as f, open("clean_" + file,"w") as g:
        for i,line in enumerate(f,0):
            if i == 0:
                line = "["+str(line)+","
                g.write(line)
            elif line == lastline:            
                g.write(line)
                g.write("]")
            else:
                line = str(line)+","
                g.write(line)