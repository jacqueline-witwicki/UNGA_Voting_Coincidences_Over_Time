# UNGA_Voting_Coincidences_Over_Time
## A tool to analyze UNGA Voting coincidences between member states.

### USER GUIDE

> Voting coincidences measure how frequently two United Nations General Assembly (UNGA) member states voted together on all UNGA resolutions that came to a vote, in a given calendar year. 
> When two states vote together, one point is added to their coincidence score. When one state votes and the other abstains or is absent, half a point is added. When states vote in opposition, no points are added. 
> This coincidence total is divided by the number of resolutions that came to a vote (possible coincidence points) in the year. 
> This is the same methodology used in The Department of State Report to Congress on Voting Practices in the United Nations for 2020 Section 406 of Public Law 101-246 (22 U.S.C. §2414a), with the small difference that absences are treated the same as abstentions.
> View the 2020 Report [HERE.]( https://www.state.gov/wp-content/uploads/2021/11/Report-Voting-Practices-in-the-United-Nations-2020.pdf "Report to Congress") 


### EXPLORE THE DATA

> The results of this repository can be used to gain a better understanding of the relationships between member states in the United Nations General Assembly (UNGA).
> The results can also be used to determine how ideologically aligned various member states are.
> For example, as of 6 May 2022, the only resolutions that have come to a vote in 2022 have been in response to Russia's invasion of Ukraine.
> Looking at voting coincidences in 2022, you can understand the feelings of all UNGA member states, regarding the conflict.
> These relationships can be modeled with maps, line graphs, bar charts, and various other visualization tools.
> I created a Tableau Public page to model the result of using this repository to calculate voting coincidences for The United States, China, and Russia with all other member states, over time.
> Explore the results on Tableau [HERE.](https://public.tableau.com/views/VotingCoincidencesintheUnitedNationsGeneralAssemblyOverTime/VotingCoincidenceswithKeyUNGAMemberStates?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link "Jacqueline's Tableau")


### FILE BREAKDOWN


#### INPUTS :

1. Country_Code_index.txt ->   
   * This file contains UNGA member states and their country codes. I wrote this file by hand using country codes in world_countries_2020.shp. 

   * It is used by DF_OUTPUT_EDIT.py to produce files with the (*YEAR*)_(*key1 COUNTRY*)_For_Map.csv naming convention.
                    
   
2. world_countries_2020.shp  ->    
   * Using Tableau, this file joins with files that have the (*key1 COUNTRY*)_For_Map.csv naming convention on the three digit country codes.
   
   * This file contains polygon information that produces a map of the world with 2020 country borders.
  
   * This file is not included in this repository due to its size. It is produced by IPUMS International and can be downloaded by clicking the link at the top of the page [HERE.](https://international.ipums.org/international/gis.shtml "IPUMS International Shape File")
   

3. United Nations Digital Library Voting Data ->    
   * text_parser.py scrapes this data directly from the United Nations Digital Library Website and uses it to produce files with the (*YEAR*)_RAW_COIN.csv naming convention. 
  
   * The digital library contains UNGA voting data organized by resolution and year. It can be viewed [HERE.](https://digitallibrary.un.org/search?ln=en&cc=Voting%20Data&p=&f=&rm=&ln=en&sf=year&so=a&rg=50&c=Voting%20Data&c=&of=hb&fti=0&fct__2=General%20Assembly&fct__9=Vote&fct__3=2021&fti=0&fct__2=General%20Assembly&fct__9=Vote&fct__3=2021 "United Nations Digital Library")
   

#### PYTHON FILES:
    
1. text_parser.py ->   
   * This file scrapes text from the United Nations Digital Library website.

   * The user inserts the year that they are interested in gathering voting data from in year_of_interest variable at the top of the code.

   * This file returns a CSV file with the naming scheme  (*YEAR*)_RAW_COIN.csv, which contains raw voting data on all resolutions for the given year.

   * The output of this code is the input of DF_OUTPUT_EDIT.py
                    
   
2. DF_OUTPUT_EDIT.py  ->    
   * This file uses the raw voting data produced in text_parser.py and stored in (*YEAR*)_RAW_COIN.csv to calculate voting coincidences between one member state and all other member states, for the given year.
  
   * The user inserts the year that they are calculating voting coincidences for in the year_of_interest variable at the top of the code. This year should also be reflected in the input file and naming of the output file.
   
   * The user inserts the country they want to calculate coincidences for, against the rest of all UNGA member states, as key1, using the country_of_interest variable at the top of the code. This selection should be reflected in the name of the output file.   
   
   * This file returns a CSV file with the naming scheme (*YEAR*)_(*key1 COUNTRY*)_For_Map.csv, which contains UNGA member countries, their voting coincidence with the key1 country as a decimal, the year associated with the input file, and their three digit numeric country code.
   
   * The output of this code is an input of For_Map_Joiner.py  
  

3. For_Map_Joiner.py ->    
   * This file concatenates a list of files produced by DF_OUTPUT_EDIT.py to create a file using the (*key1 COUNTRY*)_For_Map.csv naming pattern. 
  
   * The user selects what files with the (*YEAR*)_(*key1 COUNTRY*)_For_Map.csv naming scheme they wish to be included in the output, (*key1 COUNTRY*)_For_Map.csv. These input files should have the same key1 country and span multiple years of interest. 
   
   * (*key1 COUNTRY*)_For_Map.csv can be joined with world_countries_2020.shp from IPUMS International using Tableau to create outputs similar to those in the Tableau Public link above. 
  

#### OUTPUT FILES:
  
1. (*YEAR*)_RAW_COIN.csv  ->    
   * Files with this naming convention are outputs of text_parser.py and inputs of DF_OUTPUT_EDIT.py.  
  
   * These files contain each resolution for a given year and each UNGA member state voted.  In the file, Y indicates a yes vote by the column country for the row resolution. N is a no vote. A is an abstention. X is an absence.
  
  
2. (*YEAR*)_(*key1 COUNTRY*)_For_Map.csv  ->    
   * Files with this naming convention are outputs of DF_OUTPUT_EDIT.py and inputs of  For_Map_Joiner.py.  
  
   * These files contain the names of all UNGA member countries, their corresponding country codes, the year associated with the corresponding (*YEAR*)_RAW_COIN.csv input file, and their voting coincidence with the key1 country.
  
  
3. (*key1 COUNTRY*)_For_Map.csv  ->    
   * Files with this naming convention are outputs of For_Map_Joiner.py and inputs of the Tableau project, Voting Coincidences in the United Nations General Assembly Over Time.twb. These files can be joined with world_countries_2020.shp from IPUMS International using Tableau to create various visualizations.
  
   * These files hold concatenated information from all For_Map_Joiner.py input files used in their production.      
   
   * Files with this naming convention that also contain the number 2 include data from 1992-2022. All other files with this name contain data from 2003-2022.  


4. Voting Coincidences in the United Nations General Assembly Over Time.twb  ->    
   * This Tableau file is the result of joining three different (*key1 COUNTRY*)_For_Map.csv files for (The United States, China, and Russia with world_countries_2020.shp, in Tableau.
   
   * The files are joined on the three digit country codes for each country. 
   
   * The Tableau Dashboard in the files contains three maps and three bar graphs, visualizing coincidences over time for the key1 countries associated with the input files.
   
   * The output of this file can be accessed in Tableau Public, above. 
            
