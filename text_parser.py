#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:45:24 2022

@author: jacquelinewitwicki
"""
#NOTE: THE YEAR USED IN THE EACHYEAR FUNCTION IN LINE 36 AND USED TO LABEL THE 
#OUTPUT FILE SHOULD ALL BE THE SAME.

import requests
from bs4 import BeautifulSoup
import pandas as pd


def eachyear(year):
    
#The eachyear function accepts a given year as input and produces title_list, 
#which contains a list of java handles.
#Each item in title list is associated with a UNGA resolution that came to a 
#vote, in the given year.   

    def getdata(url): 
        r = requests.get(url) 
        return r.text 
    htmldata = ["https://digitallibrary.un.org/search?",
          "ln=en&cc=Voting%20Data&p=&f=&rm=&ln=en&sf=year&so=a&rg=200&",
          "c=Voting%20Data&c=&of=hb&fti=0&fct__2=General%20Assembly&fct__9=Vote&",
          "fct__3=",year,"&fti=0&fct__2=General%20Assembly&fct__9=Vote&fct__3=",year
          ]
    response = ''.join(htmldata)
    response=getdata(response)
    soup = BeautifulSoup(response, 'html.parser') 
     
    title_list=[]
    for line in soup.body.find_all('abbr',title=True, class_="unapi-id"):
        title=line.get('title')
        title=str(title)
        title_list.append(title)
    return title_list
    
codes=eachyear("2022")
#^INSERT THE TARGET YEAR YOU WANT TO PULL VOTE DATA FROM IN THE ABOVE FUNCTION

#%%
def eachres(java):
    
#The eachres function accepts a java handle and produces a cleaned version of 
#the text on the associated resolution's UN Digital library page.
#For the resolution associated with the given input, the function identifies 
#the resolution number and the list of votes.
#It then creates a list of dictionaries that each contail the country's name, 
#the given resolution, and how the country voted.
#For votes, Y = a yes vote, N = no, A = abstain, X = absent     

    def getdata(url): 
        r = requests.get(url) 
        return r.text 
    resolution=[]
    htmldata = ["https://digitallibrary.un.org/record/",java,"?ln=en"] 
    response = ''.join(htmldata)
    response=getdata(response)
    response=response.replace("<br/>", "<br>")
    soup = BeautifulSoup(response, 'html.parser') 
    data = '' 
    for data in soup.find_all("span")[31]: 
       res=data.get_text()
       resolution.append(res)
    resolution=resolution[0]
      

    count_list=[]
    options=['Y','A','N']


    for data in soup.select_one('span:-soup-contains("FRANCE")'): 
       vote=data.get_text().strip()
       
       if vote.split(' ')[0] in options:
           count={"Country":str(vote).strip()[2:],resolution:str(vote).split(" ")[0]} 
           count_list.append(count)
       elif vote == (''):
           pass
       else:
           count={"Country":str(vote),resolution:"X"}
           count_list.append(count)
 
    return count_list

#%%
#Fix_names contains a dictionary of former country names and their current names.
#This is used in the below loop to ensure countries can be tracked over time, 
#regardless of name changes.
#The decision was made to track  Serbia and Montenegro's voting data under 
#Serbia, until Serbia and Montenegro split.
#As the focus of this analysis was on the last 20-30 years, this only captures
# name changes after the break up of the USSR. 
#The choice was made to exclude some state that no longer exist from tables 
#More states can be added in the below dictionary to extend analysis further 
#back in the "Old Name":"New Name" format

fix_names={
    "CZECH REPUBLIC":"CZECHIA",
    "THE FORMER YUGOSLAV REPUBLIC OF MACEDONIA":"NORTH MACEDONIA",
    "CAPE VERDE":"CABO VERDE",
    "LIBYAN ARAB JAMAHIRIYA":"LIBYA",
    "BOLIVIA (PLURINATIOANL STATE OF)":"BOLIVIA (PLURINATIONAL STATE OF)",
    "BOLIVIA":"BOLIVIA (PLURINATIONAL STATE OF)",
    "SERBIA AND MONTENEGRO":"SERBIA",
    "VENEZUELA":"VENEZUELA (BOLIVARIAN REPUBLIC OF)",
    "SERBIAMONTENEGRO":"SERBIA",
    "SWAZILAND":"ESWATINI"}
  
#The below for loop builds dataframe df and transposes it into dataframe df_t.
#Using the eachres function, defined abouve, to build a dataframe containing 
#vote data for each resolution, the loop concatenates these dataframes.
#The product of this loop is a dataframe that contains each countries vote for 
#the year given to the eachyear fuction in codes, line 36.

df = pd.DataFrame(columns=["Country"])

for item in codes:
    item = pd.DataFrame(eachres(item))
    item["Country"]=item["Country"].replace(fix_names)
    item.set_index("Country",inplace=True,drop=True)

    df = pd.concat([item,df],axis=1)

    
    df_t=df.T
    
#Below, df_t, containing vote data on all resolutions for the given year is 
#saved to a CSV file and printed.
#This CSV file will be the input file in #DF_OUTPUT_EDIT
#Be sure to name this CSV file appropriately. Details on naming can be found 
#in the README.md file.

df_t.to_csv("2022_RAW_COIN.csv",index=False,header=True)    
print(df_t)




