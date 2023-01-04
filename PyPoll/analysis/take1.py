import os
import csv

    
input_path = os.path.join('..', 'Resources', 'election_data.csv')
winner =""
winning_count=0

# Opening the input file
with open(input_path) as polldata:
    csvreader = csv.reader(polldata, delimiter=',')

    # Skipping the header and storing
    csvheader = next(csvreader)

    # initializing variables, where unique_candidates store the names of each candidate, a counter for all the votes, and a converting the csvreader to a list
    total_num_votes = 0
    unique_candidates = []
    list = []
    candidate_votes = {}

    for row in csvreader:
        total_num_votes+=1
        name = row[2]
        if name not in unique_candidates:
            unique_candidates.append(name)
            candidate_votes[name] = 0
        candidate_votes[name] +=1
    #     list.append(row)
    print(candidate_votes)
# Initialing a list to store the voting for each candidate

# count_votes = []

# for candidate in unique_candidates:
#     counter = 0
#     for item in list:
#         if item[2] == candidate:
#             counter +=1
#     count_votes.append(counter)

# Initializing a list to store the percentage of voting each candidate obtained

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
# percentages = [round(item/total_num_votes*100,2) for item in count_votes]

# The three lists are zipped, and will be used to store to an output file
# results = zip(unique_candidates, count_votes, percentages)

# Determining the winner of the election

# winner = unique_candidates[percentages.index(max(percentages))]

# # Print all results on Terminal
# print("Election Results \n---------------------")
# print(f"Total votes: {total_num_votes} \n---------------------")
# for item in results:
#     print(f'{item[0]}: {item[1]} votes, {item[2]}%')
# print(f'---------------------\nWinner: {winner} ')

# # Store data to an output file
# output_path = os.path.join('analysis.csv')

# results = zip(unique_candidates, count_votes, percentages)

# with open(output_path,"w") as output_data:
#     csvwriter = csv.writer(output_data)
#     header = ['candidate', 'total number of votes', 'percentage voting']
#     csvwriter.writerow(header)
#     csvwriter.writerows(results)