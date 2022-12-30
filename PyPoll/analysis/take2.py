import os
import csv
    
input_path = os.path.join('..', 'Resources', 'election_data.csv')

# Opening the input file
with open(input_path) as polldata:
    csvreader = csv.reader(polldata, delimiter=',')

    # Skipping the header and storing
    csvheader = next(csvreader)

    # initializing variables, where unique_candidates store the names of each candidate, a counter for all the votes, and a converting the csvreader to a list
    total_num_votes = 0
    unique_candidates = []

# Difference with main.py --> eliminated the list[]. Trying to iterate directly with the csvreader file
    for row in csvreader:
        total_num_votes+=1
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])

# Initialing a list to store the voting for each candidate

count_votes = []

#NOTE:  for some reason, it seems I need to open again the file and regenerate the csvreader, which is what I'm doing below
with open(input_path) as polldata:
    csvreader = csv.reader(polldata, delimiter=',')

    # Skipping the header and storing
    csvheader = next(csvreader)

    #NOTE: After the first iteration of the first FOR loop, the csvreader stops working. I need to ask this to the tutors.
    for candidate in unique_candidates:
        counter = 0
        for row in csvreader:
            if row[2] == candidate:
                counter +=1
        count_votes.append(counter)


# Initializing a list to store the percentage of voting each candidate obtained

percentages = []

for item in count_votes:
    pct = round(item/total_num_votes *100 , 2)
    percentages.append(pct)

# The three lists are zipped, and will be used to store to an output file
results = zip(unique_candidates, count_votes, percentages)

# Determining the winner of the election

winner = unique_candidates[percentages.index(max(percentages))]

# Print all results on Terminal
print("Election Results \n---------------------")
print(f"Total votes: {total_num_votes} \n---------------------")
for item in results:
    print(f'{item[0]}: {item[1]} votes, {item[2]}%')
print(f'---------------------\nWinner: {winner} ')

# Store data to an output file
output_path = os.path.join('analysis.csv')

results = zip(unique_candidates, count_votes, percentages)

with open(output_path,"w") as output_data:
    csvwriter = csv.writer(output_data)
    header = ['candidate', 'total number of votes', 'percentage voting']
    csvwriter.writerow(header)
    csvwriter.writerows(results)