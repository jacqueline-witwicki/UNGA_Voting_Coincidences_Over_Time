#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 21:31:18 2022

@author: jacquelinewitwicki
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:45:24 2022

@author: jacquelinewitwicki
"""



import requests
from bs4 import BeautifulSoup
import pandas as pd






def eachyear(year):
    
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
    
codes=eachyear("1992")


def eachres(java):
    
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
           #vote.split(' ')[0]=vote.split(' ')[0].replace(alt_options)
           count={"Country":str(vote).strip()[2:],resolution:str(vote).split(" ")[0]} 
           count_list.append(count)
       elif vote == (''):
           pass
       else:
           count={"Country":str(vote),resolution:"X"}
           count_list.append(count)
           
       
    
  
    return count_list

country_list=[]
code=codes[0]
counts=eachres(code)
for line in counts:
    CountryPlease=line.get("Country")
    country_list.append(CountryPlease)
print(country_list) 


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
  
problem_children=[]

df = pd.DataFrame(columns=["Country"])

for item in codes:
    item = pd.DataFrame(eachres(item))
    item=item[item["Country"].isin(problem_children)==False]
    item["Country"]=item["Country"].replace(fix_names)
    item.set_index("Country",inplace=True,drop=True)

    df = pd.concat([item,df],axis=1)

    
    df_t=df.T

df_t.to_csv("1992_RAW_COIN.csv",index=False,header=True)    
print(df_t)




