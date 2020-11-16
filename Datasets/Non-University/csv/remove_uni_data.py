#importing pandas module 
import pandas as pd 
  
# making data frame from csv file 
data = pd.read_csv("uniKnox_uf.csv", index_col = "username") 

# # dropping passed values 
#data.drop(["DondePlowman", "randyboyd", "tucarpenter", "UTIA_SVP", "KC4UTM", "utknoxville", "utk_tce", "utkdos", "ut_admissions", 
#"utk_asc", "utk_cfs", "UTKCEHHS", "UTKStudentLife", "UTKCoAD", "UTKSOM", "tennalum", "utknursing", "HaslamUT"],  inplace = True) 

data.drop(["DondePlowman"], inplace = True)
data.drop(["randyboyd"], inplace = True)
data.drop(["tucarpenter"], inplace = True)
data.drop(["UTIA_SVP"], inplace = True)
data.drop(["KC4UTM"], inplace = True)
data.drop(["utknoxville"], inplace = True)
data.drop(["utk_tce"], inplace = True)
data.drop(["utkdos"], inplace = True)
data.drop(["ut_admissions"], inplace = True)
data.drop(["utk_asc"], inplace = True)
data.drop(["utk_cfs"], inplace = True)
data.drop(["UTKCEHHS"], inplace = True)
data.drop(["UTKStudentLife"], inplace = True)
data.drop(["UTKCoAD"], inplace = True)
data.drop(["UTKSOM"], inplace = True)
data.drop(["tennalum"], inplace = True)
data.drop(["utknursing"], inplace = True)
data.drop(["HaslamUT"], inplace = True)

# display 
print(data)
data.to_csv("filtered_utk.csv") 
