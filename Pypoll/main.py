# import csv module
import csv

# Setting up variables
numOfVotes = 0
winner = ''

# Setting up dictionary
voteCount = {}

# Opens input csv file and reads data row by row
with open('election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        # Counting total number of votes casted by adding 1 to count for each row in csv
        numOfVotes += 1
        # Counting votes for each candidate. If dictionary does not already contain candidate (identified by name), add it to dictionary. For candidate in row, add 1 to existing count
        candidateName = row[2]
        if candidateName not in voteCount:
            voteCount[candidateName] = 0
        voteCount[candidateName] += 1