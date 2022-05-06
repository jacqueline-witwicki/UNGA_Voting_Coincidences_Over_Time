# UNGA_Voting_Coincidences_Over_Time
## A tool to analyze UNGA Voting coincidences between member states.

### USER GUIDE













### FILE BREAKDOWN

#### PYTHON FILES:
    
1. text_parser.py ->   
   * This file scrapes text from the United Nations Digital Library website.

   * The user inserts the year that they are interested in gathing voting data from in line 36.

   * This file returns a CSV file with the naming scheme  (*YEAR*)_RAW_COIN.csv, which contains raw voting data on all resolutions for the given year.

   * The output of this code is the input of DF_OUTPUT_EDIT.py
                    
   
2. DF_OUTPUT_EDIT.py  ->    
   * This file uses the raw voting data produced in text_parser.py and stored in (*YEAR*)_RAW_COIN.csv to calculate voting coincidences between one member state and all other member states, for the given year.
  
   * The user inserts the year that they are calculating voting coincidences for in line 103. This year should also be reflected in the inpute file and naming of the output file.
   
   * The user inserts the country they want to calculate coincidences for, against the rest of all UNGA member states, as key1, in line 103. This selection should be reflected in the name of the output file.   
   
   * This file returns a CSV file with the naming scheme (*YEAR*)_(*key1 COUNTRY*)_For_Map.csv , which contains UNGA member countries, their voting coincidence with the key1 country as a decimal, the year associated with the input file, and their three digit numeric country code.
   
   * The output of this code is an input of For_Map_Joiner.py  
  

3. For_Map_Joiner.py ->    
   * Reads a txt file with vote counts that have been translated by UNGA_READER.py.  
  
   * Returns voting coincidence, coincidence breakdowns, and absentee rates.    
  

#### OUTPUT FILES:
  
1. (*YEAR*)_RAW_COIN.csv  ->    
   * Reads a txt file with vote counts that have been translated by UNGA_READER.py.  
  
   * Returns voting coincidence, coincidence breakdowns, and absentee rates.  
  
  
2. (*YEAR*)_(*key1 COUNTRY*)_For_Map.csv  ->    
   * Reads a txt file with vote counts that have been translated by UNGA_READER.py.  
  
   * Returns voting coincidence, coincidence breakdowns, and absentee rates.    
  
  
3. (*key1 COUNTRY*)_For_Map.csv  ->    
   * Reads a txt file with vote counts that have been translated by UNGA_READER.py.  
  
   * Returns voting coincidence, coincidence breakdowns, and absentee rates.              
            
