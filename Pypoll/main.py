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