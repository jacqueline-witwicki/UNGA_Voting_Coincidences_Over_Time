#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:32:56 2022

@author: jacquelinewitwicki
"""


#NOTE: THE YEAR ASSOCIATED WITH THE INPUT FILE, USED IN THE COINCIDENCE FUNCTION 
#IN LINE 103, AND USED TO LABEL THE OUTPUT FILE SHOULD ALL BE THE SAME.

import pandas as pd

#The input file should contain an output from text_parser.py. This input can be
# changed based on your analysis.

df=pd.read_csv("2022_RAW_COIN.csv")


#Vote list contains a list of dictionaries
#Each dictionary corresponds with a resolution that came to a vote in the year 
#associated with the input file.
#Each dictionary contains countries matched with their corresponding vote

vote_list=df.to_dict("records")

#The function getList produces a list of keys from a given dictionary. 
#This is used to produce a list of countries in line 25.
#This list of countries is used in a loop below that calculates voting 
#coincidences for one member state and all other countries.

def getList(dict):
    return dict.keys()
countries=(getList(vote_list[0]))

#sum_votes calculates the number of resolutions that came to a vote in the year
# associated with the input file.
#sum_votes is the denominator in calculating coincidences between UNGA member 
#states, for the given year.

sum_votes = len([ele for ele in vote_list if isinstance(ele, dict)])
sum_votes=sum_votes-1

#print(sum_votes)  #<Deleting the first # in this line will print the total 
#number of resolutions that came to a vote in the year.

#%%

#The coincidence function accepts the inputs of two different country names and
# a year.
#The vote coincidence is calculated for the two countries given. The year is 
#used for later calculations and should be the same as the year associated with
# the input file. 

coin_list=[]

#^coin_list will contain a list of dictionaries produced by the coincidence 
#function.

def coincidence(key1,key2,year):
   
    val=0
    same=0
    partial=0
    
#^While the same and partial totals are not used for calculations in this 
#project, they can be used for other calculations, depending on user focus.    
#The below loop calculates the numerator of the coincidence score by adding 1 
#point when states vote functionally the same, and half a point when they vote 
#partially in line.
#No points are added to the coincidence score (numerator of percent coincidence)
# when states vote in opposition.

    for resvts in vote_list:
        if resvts[key1]=="Y" and (resvts[key2] == "Y"):
            val=val+1 
            same=same+1
        elif (resvts[key1] =="N") and (resvts[key2] =="N"):
             val=val+1
             same=same+1
        elif (resvts[key1] =="A") and (resvts[key2] =="A"):
             val=val+1
             same=same+1
        elif (resvts[key1] =="A") and (resvts[key2] =="X"):
              val=val+1 
              same=same+1
        elif (resvts[key1] =="X") and (resvts[key2] =="A"):
               val=val+1  
               same=same+1
        elif (resvts[key1] =="X") and (resvts[key2] =="X"):
             val=val+1
             same=same+1
        elif (resvts[key1] == "Y") and (resvts[key2] == "A"):
            val=val+.5
            partial=partial+1
        elif (resvts[key1] == "A") and (resvts[key2] == "Y"):
            val=val+.5
            partial=partial+1
        elif (resvts[key1] == "N") and (resvts[key2] == "A"):
            val=val+.5
            partial=partial+1
        elif (resvts[key1] == "A") and (resvts[key2] == "N"):
            val=val+.5
            partial=partial+1
        elif (resvts[key1] == "Y") and (resvts[key2] == "X"):
             val=val+.5
             partial=partial+1
        elif (resvts[key1] == "N") and (resvts[key2] == "X"):
             val=val+.5  
             partial=partial+1
        elif (resvts[key1] == "X") and (resvts[key2] == "Y"):
             val=val+.5
             partial=partial+1
        elif (resvts[key1] == "X") and (resvts[key2] == "N"):
             val=val+.5
             partial=partial+1
             
    coincidence=val/sum_votes
    
    coin_dict={"Country":key2,"Coincidence":coincidence,"Year":year}
    coin_list.append(coin_dict)
    
#^The above two lines produce a dictionary containing the second input (country)
# in the coincidence function, the decimal coincidence score, and the year 
#given in the function.   
#This dictionary is then appended to coin_list so that coincidences for multiple
# countries can be stored for later use.
#%%

for country in countries:
   run=coincidence("UNITED STATES",country,"2022")
   
#^The above loop calculates coincidences for each country in the countries list
# with the United States.
#To calculate coincidences between all countries in the list and any other
# country, UNITED STATES can be replaced with that country's name, as it 
#appears in the countries list.
#My outputs for this project focus on UNITED STATES, RUSSIAN FEDERATION, 
#and CHINA.


dfc = pd.DataFrame.from_dict(coin_list)

#print(dfc)  #<Deleting the first # in this line will print dataframe dfc 
#containing all countries represented in the input file, their voting 
#coincidence with the key1 input in the coincidence function, and the year.



count_list = []
with open("Country_Code_index.txt") as file:
 for line in file:
    line=line.strip("\n")
    count={"Country":str(line).split("\t")[0],"Code":str(line).split("\t")[1]}
    count_list.append(count)
    
#^The above for loop uses the country_code_index.txt file to create a list of
# dictionaries, containing country names and their corresponding three digit 
#numeric country codes.
#^These country codes are important when joining to the IPUMS International 
#shape file referenced in the README.md file.


dfcd=pd.DataFrame(count_list)

#print(dfcd)  #<Deleting the first # in this line will print dataframe dfcd 
#containing all countries in the country_code_index and their corresponding code.

result = pd.merge(dfc, dfcd, how="left", on=["Country"])

#^result contains a merged dataframe containing both coincidence and country 
#code information

print(result)
result.to_csv("2022_UNITED_STATES_For_Map.csv",index=True,header=True) 

#Above, result, containing country names, voting coincidences, the year, and 
#country codes for the given year is saved to a CSV file and printed.
#This CSV file will be an input file in For_Map_Joiner.py
#Be sure to name this CSV file appropriately, cointainking the year and the 
#key1 country. Details on naming can be found in the README.md file.
    
    
    
    
    