#PYBANK Code for PYTHON CHALLENGE  ---- change output file and finalize

import os
import csv

#Path to PyBank.csv
path = os.path.join("Resources", "PyBank.csv")

#Creating lists
months = []
change = []
amount = []

#Reading CSV
with open(path, "r") as text:
    csvreader = csv.reader(text, delimiter = ",")

    #Skipping header
    csv_header = next(csvreader) 

    #Setting variable equal to 0
    netTotal = 0 
    
    #Reading the rows and totaling the months/net total  
    for row in csvreader:
        months.append(row[0])
        netTotal += int(row[1])
        #Adding amounts to list to find average change
        amount.append(row[1]) 
    AVGchange = round(((int(amount[-1]) - int(amount[0]))/(len(months)-1)),2)

    #Loop through Profit/Losses to find change per month; find greatest increase/decrease
    for x in range(len(amount)-1):
        change.append(int(amount[x+1])-int(amount[x]))
    greatIncrease = max(change)
    greatDecrease = min(change)
    maxIncrease = change.index(greatIncrease) + 1
    maxDecrease = change.index(greatDecrease) + 1
    
            
    print(f'Financial Analysis')
    print(f'-----------------------------')
    print(f'Total Months: {len(months)}')
    print(f'Total: ${netTotal}')
    print(f'Average Change: ${AVGchange}')
    print(f'Greatest Increase in Profits: {months[maxIncrease]} (${greatIncrease})')
    print(f'Greatest Decrease in Profits: {months[maxDecrease]} (${greatDecrease})')




#Define outPath and create new file
outPATH = os.path.join("Analysis", "TestPath2.txt")

#Open new file and print
with open(outPATH, "w") as text2:
    text2.write(f'Financial Analysis\n')
    text2.write(f'-----------------------------\n')
    text2.write(f'Total Months: {len(months)}\n')
    text2.write(f'Total: ${netTotal}\n')
    text2.write(f'Average Change: ${AVGchange}\n')
    text2.write(f'Greatest Increase in Profits: {months[maxIncrease]} (${greatIncrease}\n')
    text2.write(f'Greatest Decrease in Profits: {months[maxDecrease]} (${greatDecrease})')
