#-----PYBANK Code for PYTHON CHALLENGE-----#
import os
import csv

path = os.path.join("Resources", "PyBank.csv") #Path to PyBank.csv

months = [] #Creating empty lists
change = []
amount = []

with open(path, "r") as text: #Reading CSV
    csvreader = csv.reader(text, delimiter = ",")
    csv_header = next(csvreader) #Skipping header
    netTotal = 0  #Setting net total to 0
         
    for row in csvreader: #Looping through the rows and totaling the months/net total
        months.append(row[0])
        netTotal += int(row[1])
        amount.append(row[1])
    AVGchange = round(((int(amount[-1]) - int(amount[0]))/(len(months)-1)),2) #Finding the average change
    
    for x in range(len(amount)-1): #Loop through Profit/Losses to find change per month; find greatest increase/decrease
        change.append(int(amount[x+1])-int(amount[x]))
    greatIncrease = max(change)
    greatDecrease = min(change)
    maxIncrease = change.index(greatIncrease) + 1
    maxDecrease = change.index(greatDecrease) + 1

    #-----Print results to terminal-----#            
    print(f'Financial Analysis')
    print(f'-----------------------------')
    print(f'Total Months: {len(months)}')
    print(f'Total: ${netTotal}')
    print(f'Average Change: ${AVGchange}')
    print(f'Greatest Increase in Profits: {months[maxIncrease]} (${greatIncrease})')
    print(f'Greatest Decrease in Profits: {months[maxDecrease]} (${greatDecrease})')

outPATH = os.path.join("Analysis", "Financial Analysis.txt") #Define outpath for text file

#-----Print results to text file-----# 
with open(outPATH, "w") as text2:
    text2.write(f'Financial Analysis\n')
    text2.write(f'-------------------------\n')
    text2.write(f'Total Months: {len(months)}\n')
    text2.write(f'Total: ${netTotal}\n')
    text2.write(f'Average Change: ${AVGchange}\n')
    text2.write(f'Greatest Increase in Profits: {months[maxIncrease]} (${greatIncrease}\n')
    text2.write(f'Greatest Decrease in Profits: {months[maxDecrease]} (${greatDecrease})')
