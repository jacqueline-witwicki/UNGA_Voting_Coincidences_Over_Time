# UNGA_Voting_Coincidences_Over_Time
## A tool to analyze UNGA Voting coincidences between member states.



-FILE BREAKDOWN:
    
1. text_parser.py ->   
Reads a copied vote count from the UN digital library and returns a list of Y,N,A, and Xs. This list can then be copied into a spreadsheet.

   Once this has been done for all relevant resolutions, filling the spreadsheet. The spreadsheet can be copied into its own txt file and run through VOTE_CNTR.py  

⋅⋅⋅I am currently writing a web scraper that will do this by year, not resolution. ⋅⋅

⋅⋅⋅!!! For this code to work, you must copy the vote count for the resolution into the txt file that UNGA_READER.py is pulling from. ⋅⋅
                    
   
2. VOTE_CNTR.py  ->    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reads a txt file with vote counts that have been translated by UNGA_READER.py. 
                        Returns voting coincidence, coincidence breakdowns, and absentee rates. 
                    !!! For this code to work, it must read a text file that contains UNGA_READER.py translated vote counts.
                        Each resolution must have it's own line in the txt file.
                        I reccomend copying UNGA_READER.py outputs into an Excel file and then copying the finished excel file, with all relevant resolutions, into a txt file for VOTE_CNTR.py to read.
                  NOTE: THIS CODE WILL ONLY GIVE AN ACCURATE READ FOR YEARS THAT HAVE THE SAME 193 MEMBER STATE MAKE UP IN THE UNGA AS 2022. It could be edited to read data from other years.  
                  
    
3. (20-22)_UNSC_Coin.py -> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The code in this group of 3 files runs similarly to VOTE_CNTR.py.
                        Reads a txt file with vote counts that have been translated by UNGA_READER.py and returns voting coincidence.
                        A new version of the code must be written for each year, in it's current state, as the UNSC rotates members.
                        

4. TXT   Files  ->     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;These files are the inputs for UNGA_READER.py, VOTE_CNTR.py, and `(20-22)_UNSC_Coin.py.  
                         UN_Read.txt is specifically the input for UNGA_Reader.py.
                         
                         
