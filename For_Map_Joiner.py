#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:10:41 2022

@author: jacquelinewitwicki
"""


import pandas as pd

#Of the three lists of files below, only one can be used/active at a time.
#files contains a list of input files produced by DF_OUTPUT_EDIT.py
#The files list should include only files with coincidences calculated using 
#the same key1 country_of_interest in DF_OUTPUT_EDIT.py.
#Files should span the time period that the user is interested in tracking 
#coincidences accross.
#files lists with Russia, China, and The US as the key1 country from 1992-2022 
#are listed below for user convenience.



#files=["2022_RUSSIAN_FEDERATION_For_Map.csv","2021_RUSSIAN_FEDERATION_For_Map.csv",
#       "2020_RUSSIAN_FEDERATION_For_Map.csv","2019_RUSSIAN_FEDERATION_For_Map.csv",
#       "2018_RUSSIAN_FEDERATION_For_Map.csv","2017_RUSSIAN_FEDERATION_For_Map.csv",
#       "2016_RUSSIAN_FEDERATION_For_Map.csv","2015_RUSSIAN_FEDERATION_For_Map.csv",
#       "2014_RUSSIAN_FEDERATION_For_Map.csv","2013_RUSSIAN_FEDERATION_For_Map.csv",
#       "2012_RUSSIAN_FEDERATION_For_Map.csv","2011_RUSSIAN_FEDERATION_For_Map.csv",
#       "2010_RUSSIAN_FEDERATION_For_Map.csv","2009_RUSSIAN_FEDERATION_For_Map.csv",
#       "2008_RUSSIAN_FEDERATION_For_Map.csv","2007_RUSSIAN_FEDERATION_For_Map.csv",
#       "2006_RUSSIAN_FEDERATION_For_Map.csv","2005_RUSSIAN_FEDERATION_For_Map.csv",
#       "2004_RUSSIAN_FEDERATION_For_Map.csv","2003_RUSSIAN_FEDERATION_For_Map.csv",
#       "2002_RUSSIAN_FEDERATION_For_Map.csv","2001_RUSSIAN_FEDERATION_For_Map.csv",
#       "2000_RUSSIAN_FEDERATION_For_Map.csv","1999_RUSSIAN_FEDERATION_For_Map.csv",
#       "1998_RUSSIAN_FEDERATION_For_Map.csv","1997_RUSSIAN_FEDERATION_For_Map.csv",
#       "1996_RUSSIAN_FEDERATION_For_Map.csv","1995_RUSSIAN_FEDERATION_For_Map.csv",
#       "1994_RUSSIAN_FEDERATION_For_Map.csv","1993_RUSSIAN_FEDERATION_For_Map.csv",
#       "1992_RUSSIAN_FEDERATION_For_Map.csv",]

#%%


#files=["2022_CHINA_For_Map.csv","2021_CHINA_For_Map.csv","2020_CHINA_For_Map.csv",
#       "2019_CHINA_For_Map.csv","2018_CHINA_For_Map.csv","2017_CHINA_For_Map.csv",
#       "2016_CHINA_For_Map.csv","2015_CHINA_For_Map.csv","2014_CHINA_For_Map.csv",
#       "2013_CHINA_For_Map.csv","2012_CHINA_For_Map.csv","2011_CHINA_For_Map.csv",
#       "2010_CHINA_For_Map.csv","2009_CHINA_For_Map.csv","2008_CHINA_For_Map.csv",
#       "2007_CHINA_For_Map.csv","2006_CHINA_For_Map.csv","2005_CHINA_For_Map.csv",
#       "2004_CHINA_For_Map.csv","2003_CHINA_For_Map.csv","2002_CHINA_For_Map.csv",
#       "2001_CHINA_For_Map.csv","2000_CHINA_For_Map.csv","1999_CHINA_For_Map.csv",
#       "1998_CHINA_For_Map.csv","1997_CHINA_For_Map.csv","1996_CHINA_For_Map.csv",
#       "1995_CHINA_For_Map.csv","1994_CHINA_For_Map.csv","1993_CHINA_For_Map.csv",
#       "1992_CHINA_For_Map.csv",]

#%%


files=["2022_UNITED_STATES_For_Map.csv","2021_UNITED_STATES_For_Map.csv",
       "2020_UNITED_STATES_For_Map.csv","2019_UNITED_STATES_For_Map.csv",
       "2018_UNITED_STATES_For_Map.csv","2017_UNITED_STATES_For_Map.csv",
       "2016_UNITED_STATES_For_Map.csv","2015_UNITED_STATES_For_Map.csv",
       "2014_UNITED_STATES_For_Map.csv","2013_UNITED_STATES_For_Map.csv",
       "2012_UNITED_STATES_For_Map.csv","2011_UNITED_STATES_For_Map.csv",
       "2010_UNITED_STATES_For_Map.csv","2009_UNITED_STATES_For_Map.csv",
       "2008_UNITED_STATES_For_Map.csv","2007_UNITED_STATES_For_Map.csv",
       "2006_UNITED_STATES_For_Map.csv","2005_UNITED_STATES_For_Map.csv",
       "2004_UNITED_STATES_For_Map.csv","2003_UNITED_STATES_For_Map.csv",
       "2002_UNITED_STATES_For_Map.csv","2001_UNITED_STATES_For_Map.csv",
       "2000_UNITED_STATES_For_Map.csv","1999_UNITED_STATES_For_Map.csv",
       "1998_UNITED_STATES_For_Map.csv","1997_UNITED_STATES_For_Map.csv",
       "1996_UNITED_STATES_For_Map.csv","1995_UNITED_STATES_For_Map.csv",
       "1994_UNITED_STATES_For_Map.csv","1993_UNITED_STATES_For_Map.csv",
       "1992_UNITED_STATES_For_Map.csv",]

#%%

#The below loop creates a dataframe (df), containing the Code, Country, Year,
# and Coincidence for each of the files given in the files list.
#The information is appended, keeping the same 4 original columns

df = pd.DataFrame()
for file in files:
    text=pd.read_csv(file,dtype=str)
    dfx=pd.DataFrame(text,columns=["Code","Country","Year","Coincidence"])
   
    df = df.append(dfx)

print(df)
df.to_csv("UNITED_STATES_For_Map.csv",index=True,header=True) 

#Above, df, containing country names, voting coincidences, the year, and 
#country codes for the files in files is saved to a CSV file and printed.
#This CSV file will be joined with the IPUMS shape file to produce color coded 
#maps, based on coincidence.
#This CSV file can also be used to create bar graphs, tracking coincidences 
#between countries and the key1 country, over time.
#Be sure to name this CSV file appropriately, cointainking the key1 country. 
#Details on naming can be found in the README.md file.
    


