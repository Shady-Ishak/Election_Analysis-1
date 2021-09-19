import csv
import os

#Data needed to retrieve
election_path= os.path.join("resources/election_results.csv")
print(election_path)

total_votes=0
candidate_option=[]
county_option=[]
candidate_votes={}
winning_candidate=""
winning_count=0
winning_percentage=0

file_to_save=os.path.join("analysis","election_analysis.txt")
with open(file_to_save,"w")as txt_file:
    txt_file.write("Counties in the elections\n--------------\nArapahoe\nDenver\nJefferson")
   

with open(election_path) as election_data : 
    reader= csv.reader(election_data)
    header = next(reader)
    print(header)
    
    for row in reader:   
        print (row)
        total_votes+=1
        candidate_name = row[2]
        county_name = row[1]
        if candidate_name not in candidate_option:
          candidate_option.append(candidate_name)
          candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1
# To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
    for candidate_name in candidate_votes:
        votes=candidate_votes[candidate_name]
        vote_percentage=float(votes)/ float(total_votes)*100
        print (f"{candidate_name}: received {vote_percentage}% of the vote.")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate_name
        print (f"{candidate_name}:{vote_percentage}%({votes:,})\n")

        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n") 


print (total_votes)
print (candidate_option)
print (candidate_votes)
print (winning_candidate_summary)

