import csv
import os

#Data needed to retrieve
election_path= os.path.join("resources", "election_results.csv")
print(election_path)

file_to_save=os.path.join("Election_Analysis","election_analysis.txt")
with open(file_to_save,"w")as txt_file:
    txt_file.write("Counties in the elections\n--------------\nArapahoe\nDenver\nJefferson")
   


with open("/Users/shadyishak/Documents/Class.Folder/3 Python/assignment/Election_Analysis/resources/election_results.csv") as election_data : 
    reader= csv.reader(election_data)
    header = next(reader)
    print(header)

    