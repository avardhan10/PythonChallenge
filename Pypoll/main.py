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

    # Find election winner
    winningVoteCountSoFar = 0
    # voteCount.keys() returns list of all candidates because that is how I constructed it.
    for candidate in voteCount.keys():
        votesForCandidate = voteCount.get(candidate)
        if (winningVoteCountSoFar < votesForCandidate):
            winningVoteCountSoFar = votesForCandidate
            winner = candidate
        else:
            continue

    print('Election Results')
    print('Total Votes: ' + str(numOfVotes))
    for candidate in voteCount.keys():
        print(candidate + ": " + str("{:.3f}".format((voteCount.get(candidate) / numOfVotes) * 100)) + "% (" + str(
                voteCount.get(candidate)) + ")")
    print('Winner:' + winner)

    # writing to text file
    with open('pypoll.txt', 'w') as csvfile:
        csvfile.writelines('Election Results\n')
        csvfile.writelines('Total Votes: ' + str(numOfVotes) + '\n')
        for candidate in voteCount.keys():
            csvfile.writelines(
                candidate + ": " + str("{:.3f}".format((voteCount.get(candidate) / numOfVotes) * 100)) + "% (" + str(
                    voteCount.get(candidate)) + ")\n")
        csvfile.writelines('Winner: ' + winner + "\n")