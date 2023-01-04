import os
import csv
    
input_path = os.path.join('..', 'Resources', 'election_data.csv')

# Initializing variables to store the winner of the election
winner =""
winning_count=0

# Opening the input file
with open(input_path) as polldata:
    csvreader = csv.reader(polldata, delimiter=',')

    # Skipping the header and storing
    csvheader = next(csvreader)

    # initializing variables, where unique_candidates store the names of each candidate, a counter for all the votes
    total_num_votes = 0
    unique_candidates = []
    candidate_votes = {}

    for row in csvreader:
        total_num_votes+=1
        name = row[2]
        if name not in unique_candidates:
            unique_candidates.append(name)
            candidate_votes[name] = 0
        candidate_votes[name] +=1
    print(candidate_votes)

# Creating the output file

output_path = os.path.join('analysis.txt')

with open(output_path,"w") as output_data:
    output = f"""
Election Results 
---------------------
Total votes: {total_num_votes:,}
---------------------\n
"""
    print(output)
    output_data.write(output)
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        percentages = votes/total_num_votes*100
        candidate_output = (f"{candidate}: {votes:,} votes, {percentages:.2f}%\n")
        print(candidate_output)
        output_data.write(candidate_output)
        if votes > winning_count:
            winning_count = votes
            winner = candidate
    winner_output = f"""
---------------------
Winner: {winner} 
    """
    print(winner_output)
    output_data.write(winner_output)