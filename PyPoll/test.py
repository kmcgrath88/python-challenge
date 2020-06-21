#PYPOLL code for PYTHON CHALLENGE
import os
import csv

#Variables/lists
totalVotes = []


#Path to open csv
path = os.path.join("Resources", "PyPoll.csv")

#Read csv file
with open(path,"r") as text:
    csvreader = csv.reader(text, delimiter=",")

    #Skip header
    header = next(csvreader)

    #Loop through rows and collect votes and candidates
    Dict1 = {}
    for row in csvreader:
        totalVotes.append(row[0])
        candidate, votes = row[2],1   
        if candidate not in Dict1:
            Dict1[candidate] = votes     
        else:
            Dict1[candidate] +=1
WIN = max(Dict1, key=Dict1.get)

print(f'Election Results')
print(f'----------------------------')
print(f'Total Votes: {len(totalVotes)}')
for candidate in Dict1:
    print(f'{candidate}: {(Dict1[candidate]/(len(totalVotes))*100):.3f}% ({Dict1[candidate]})')
print(f'----------------------------')       
print(f'Winner: {WIN}')

outPATH = os.path.join("Analysis", "TestPath2.txt")
with open(outPATH, "w") as text2:

    text2.write(f'Election Results\n')
    text2.write(f'----------------------------\n')
    text2.write(f'Total Votes: {len(totalVotes)}\n')
    text2.write(f'----------------------------\n')
    for candidate in Dict1: 
        text2.write(f'{candidate}: {(Dict1[candidate]/(len(totalVotes))*100):.3f}% ({Dict1[candidate]})\n') 
    text2.write(f'----------------------------\n')
    text2.write(f'Winner: {WIN}\n')
    text2.write(f'----------------------------')
