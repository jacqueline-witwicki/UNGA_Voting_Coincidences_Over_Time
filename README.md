# UNGA_Voting_Coincidences_Over_Time
## A tool to analyze UNGA Voting coincidences between member states.



###FILE BREAKDOWN

####PYTHON FILES:
    
1. text_parser.py ->   
  * Reads a copied vote count from the UN digital library and returns a list of Y,N,A, and Xs. This list can then be copied into a spreadsheet.

  * Once this has been done for all relevant resolutions, filling the spreadsheet. The spreadsheet can be copied into its own txt file and run through VOTE_CNTR.py  

  * I am currently writing a web scraper that will do this by year, not resolution.  

  * !!! For this code to work, you must copy the vote count for the resolution into the txt file that UNGA_READER.py is pulling from.  
                    
   
2. DF_OUTPUT_EDIT.py  ->    
  * Reads a txt file with vote counts that have been translated by UNGA_READER.py.  
  
  * Returns voting coincidence, coincidence breakdowns, and absentee rates.  
   
  * !!! For this code to work, it must read a text file that contains UNGA_READER.py translated vote counts.  
   
  * Each resolution must have it's own line in the txt file.  
   
  * I reccomend copying UNGA_READER.py outputs into an Excel file and then copying the finished excel file, with all relevant resolutions, into a txt file for VOTE_CNTR.py to read.  
   
  * NOTE: THIS CODE WILL ONLY GIVE AN ACCURATE READ FOR YEARS THAT HAVE THE SAME 193 MEMBER STATE MAKE UP IN THE UNGA AS 2022. It could be edited to read data from other years.   


3. For_Map_Joiner.py ->    
  * Reads a txt file with vote counts that have been translated by UNGA_READER.py.  
  
  * Returns voting coincidence, coincidence breakdowns, and absentee rates.    
  

####OUTPUT FILES:
  
1. (*YEAR*)_RAW_COIN.csv  ->    
  * Reads a txt file with vote counts that have been translated by UNGA_READER.py.  
  
  * Returns voting coincidence, coincidence breakdowns, and absentee rates.  
  
  
2. (*YEAR*)_(*key1 COUNTRY*)_For_Map.csv  ->    
  * Reads a txt file with vote counts that have been translated by UNGA_READER.py.  
  
  * Returns voting coincidence, coincidence breakdowns, and absentee rates.    
  
  
3. (*key1 COUNTRY*)_For_Map.csv  ->    
  * Reads a txt file with vote counts that have been translated by UNGA_READER.py.  
  
  * Returns voting coincidence, coincidence breakdowns, and absentee rates.              
            
