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
        # Greatest increase in profits in months
        if (currentChange > changeAmount[0]):
            changeAmount[0] = currentChange
            changeMonth[0] = months[entry]
        # Greatest decrease in profits in months
        elif(currentChange < -1 * changeAmount[0]):
            changeAmount[1] = currentChange
            changeMonth[1] = months[entry]

    print("Months: " + str(len(months)))
    print("Net Profit/Loss: " + str(netEarnings))
    print("Average Change: " + str(averageChange / (len(months) - 1)))
    print("Greatest increase in profits: " + str(changeMonth[0] + " " + str(changeAmount[0])))
    print("Greatest decrease in losses: " + str(changeMonth[1] + " " + str(changeAmount[1])))

    # writing to text file
    with open('pybanking.txt', 'w') as csvfile:
        csvfile.writelines(str(len(months)) + "\n")
        csvfile.writelines(str(netEarnings) + "\n")
        csvfile.writelines(str(averageChange / (len(months) - 1)) + "\n")
        csvfile.writelines(changeMonth[0] + " " + str(changeAmount[0]) + "\n")
        csvfile.writelines(changeMonth[1] + " " + str(changeAmount[1]) + "\n")