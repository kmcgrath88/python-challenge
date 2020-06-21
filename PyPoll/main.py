#-----PYPOLL code for PYTHON CHALLENGE-----#
import os
import csv

totalVotes = [] #Empty list for total votes

path = os.path.join("Resources", "PyPoll.csv") #Path to open csv

with open(path,"r") as text: #Read csv file
    csvreader = csv.reader(text, delimiter=",")
    
    header = next(csvreader) #Skip header

    Dict1 = {} #Empty dictionary for candidates and vote counts
    for row in csvreader: #Loop through rows and collect votes and candidates
        totalVotes.append(row[0])
        candidate, votes = row[2], 1 #Variables for dictionary
        if candidate not in Dict1: #If candidate not in dictionary, add to dictionary
            Dict1[candidate] = votes #????     
        else:
            Dict1[candidate] +=1
WIN = max(Dict1, key=Dict1.get) #??? #Find winner

#-----Print results to terminal-----#
print(f'Election Results')
print(f'--------------------------')
print(f'Total Votes: {len(totalVotes)}')
for candidate in Dict1: #Loop through dictionay, print candidates, calculate percent of votes
    print(f'{candidate}: {(Dict1[candidate]/(len(totalVotes))*100):.3f}% ({Dict1[candidate]})')
print(f'--------------------------')       
print(f'Winner: {WIN}')

outPATH = os.path.join("Analysis", "Election Results.txt") #Outpath to create text file
#-----Print results to text file-----#
with open(outPATH, "w") as text2:

    text2.write(f'Election Results\n')
    text2.write(f'--------------------------\n')
    text2.write(f'Total Votes: {len(totalVotes)}\n')
    text2.write(f'--------------------------\n')
    for candidate in Dict1: 
        text2.write(f'{candidate}: {(Dict1[candidate]/(len(totalVotes))*100):.3f}% ({Dict1[candidate]})\n') 
    text2.write(f'--------------------------\n')
    text2.write(f'Winner: {WIN}\n')
    text2.write(f'--------------------------')