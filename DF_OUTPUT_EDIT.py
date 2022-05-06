#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:32:56 2022

@author: jacquelinewitwicki
"""


import pandas as pd


df=pd.read_csv("1992_RAW_COIN.csv")



rows, columns = df.shape


    
vote_list=df.to_dict("records")

def getList(dict):
    return dict.keys()
countries=(getList(vote_list[0]))

sum_votes = len([ele for ele in vote_list if isinstance(ele, dict)])
sum_votes=sum_votes-1
#print(sum_votes)

coin_list=[]

def coincidence(key1,key2,year):
   
    val=0
    same=0
    partial=0
   
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
    
   

for country in countries:
   run=coincidence("UNITED STATES",country,"1992")
   


dfc = pd.DataFrame.from_dict(coin_list)

#print(dfc)



count_list = []
with open("Country_Code_index.txt") as file:
 for line in file:
    line=line.strip("\n")
    count={"Country":str(line).split("\t")[0],"Code":str(line).split("\t")[1]}
    count_list.append(count)
    


dfcd=pd.DataFrame(count_list)
#print(dfcd)

result = pd.merge(dfc, dfcd, how="left", on=["Country"])

print(result)
result.to_csv("1992_UNITED_STATES_For_Map.csv",index=True,header=True) 
    
    
    
    
    