import os
import csv
from pathlib import Path

file = Path('PyPoll', 'Resources', 'election_data.csv')
file_Print= Path('PyPoll', 'Analysis', "Election_Results.txt")

totalVotes = 0
candidates = []
numVotes = {}

with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row
    header = next(csvreader)

    for row in csvreader:
        totalVotes += 1
        candidate_name = row[2]

        # If candidate already in the dictionary, increment their vote count
        if candidate_name in numVotes:
            numVotes[candidate_name] += 1
        else:
            # If candidate is not in the dictionary, add them and set vote count to 1
            numVotes[candidate_name] = 1
            candidates.append(candidate_name)

# Calculate percentages for each candidate
percentVotes = [f"{candidate}: {'{:.3%}'.format(numVotes[candidate]/totalVotes)}" for candidate in candidates]

# Determine the winner
winner = max(numVotes, key=numVotes.get)

#prints final analysis to console
print("Election Results")
print("------------------------")
print(f"Total Votes: {totalVotes}")
print("------------------------")
for candidate in candidates:
    print(f"{candidate}: {'{:.3%}'.format(numVotes[candidate]/totalVotes)} ({numVotes[candidate]})")
print("------------------------")
print(f"Winner: {winner}")
print("------------------------")

#writes the analysis to txt
with open(file_Print,'w') as file:
    file.write("Election Results")
    file.write("\n")
    file.write("--------------------------------")
    file.write("\n")
    file.write(f"Total Votes: {totalVotes}")
    file.write("\n")
    file.write("--------------------------------")
    file.write("\n")
    for candidate in candidates:
        file.write(f"{candidate}: {'{:.3%}'.format(numVotes[candidate]/totalVotes)} ({numVotes[candidate]})\n")
    file.write("\n")
    file.write("--------------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write("--------------------------------")
    file.write("\n")
