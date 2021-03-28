import os 
import csv 
# Import the csv file
poll_csv = os.path.join('Resources', 'election_data.csv')

# Create empty lists
total_votes = 0
# List for candidate names
candidate = []
# List for each candidate's votes
candidate_votes = []
# List for precentage for each candidate
perc_votes = []

# Open the file as reader
with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    # Read after the header row 
    header = next(csvreader)

    # for row in csvreader:
    #     print(row)

# To get total votes
    for row in csvreader:
        total_votes += 1
# To add candidate names to candidate and get candidate_votes for each candidate
        if row[2] not in candidate:
            candidate.append(row[2])
            index = candidate.index(row[2])
            candidate_votes.append(1)
        else:
            index = candidate.index(row[2])
            candidate_votes[index] += 1

# To find percentage of votes in candidate_votes:
    for votes in candidate_votes:
        percentage = (votes/total_votes)
        percentage = '{:.3%}'.format(percentage)
        perc_votes.append(percentage)

# To find the overall winner
    winner = max(candidate_votes)
    index = candidate_votes.index(winner)
    winning_candidate = candidate[index]

# To print results to terminal
print('Election Results')
print('---------------------------')
print(f'Total Votes: {str(total_votes)}')
print('---------------------------')
for each in range(len(candidate)):
    print(f'{candidate[each]}: {str(perc_votes[each])} ({str(candidate_votes[each])})')
print('---------------------------')
print(f'Winner: {winning_candidate}')
print('---------------------------')

# To export results to text file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidate)):
    line = str(f"{candidate[i]}: {str(perc_votes[i])} ({str(candidate_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))