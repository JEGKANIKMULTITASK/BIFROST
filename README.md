# BIFROST

 By: Kristine M. L. Krighaar 
 
 McStas version of BIFROST for simulation of dispersion.

 NOTE: Since I am using VScode as my editor, I have developed a slightly bad happit by being able to choose the environment for each individual notebook. Therefore multible are needed to make the scripts run. 

 Backend written in McStasScript and datareduction is made using Scipp. Description of folders:
 
 Analyzer_positions: Files provided from Rasmus Toft-Petersen of analyzer positions.
 BIFROST_Design_Article: Code used for the BIFROST design article. Includes energy resolution and brilliance transfer simulations, as well as guide drawing for the article. 
 DataConversionMJOLNIR: The dataconversion scripts that are using scipp. The plan is to make a reduction that MJOLNIR can read (Qx, Qy, I, Ierr. Example given from Jakob in lassIN5Conversion.py). To run notebook the Env_with_KGS.yml should be used as I have my own libary on a daily basis. 
 McStasScript: Code to make a mcstas simulation of the backend of BIFROST. Primary Notebook here is BIFROST_UNION_Backend.ipynb. Currently also includes notes from Rasmus on datareduction, .csv files of the  analyzer and detector information for an easy import.  

 Hope the Env_with_KGS.yml works with KGS (Kristines Golden Standard), if not, please let me know. 
