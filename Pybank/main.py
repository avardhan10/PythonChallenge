#import module
import csv

#Setting up variabes
months = []
earnings = []
netEarnings = 0
averageChange = 0
changeMonth = ['', '']
changeAmount = [0, 0]

# Opens input csv file and reads data row by row
with open('budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        netEarnings += int(row[1])
        months.append(row[0])
        earnings.append(int(row[1]))

# in the range of net earnings from the second month to the end, calculating the greatest increase and decrease
    for entry in range(1, len(earnings)):
        averageChange += earnings[entry] - earnings[entry - 1]
        currentChange = earnings[entry] - earnings[entry - 1]
