#PYPOLL code for PYTHON CHALLENGE
import os
import csv

#Variables/lists
totalVotes = []
candidates = []

#Path to open csv
path = os.path.join("Resources", "PyPoll.csv")

#Read csv file
with open(path,"r") as text:
    csvreader = csv.reader(text, delimiter=",")

    #Skip header
    header = next(csvreader)

    #Loop through rows and collect votes and candidates
    Dict1 = {"Khan": 0, "Correy": 0, "Li": 0, "O'Tooley": 0}
    for row in csvreader:
        totalVotes.append(row[0])
        Dict1[row[2]] +=1
        if row[2] not in candidates:
            candidates.append(row[2])

    kVotes = Dict1["Khan"]/(len(totalVotes))*100
    cVotes = Dict1["Correy"]/(len(totalVotes))*100
    lVotes = Dict1["Li"]/(len(totalVotes))*100
    tVotes = Dict1["O'Tooley"]/(len(totalVotes))*100
    WIN = max(Dict1, key=Dict1.get)

print(f'Election Results')
print(f'----------------------------')
print(f'Total Votes: {len(totalVotes)}')
print(f'----------------------------') 
print(f'{candidates[0]}: {kVotes:.3f}%  ({Dict1["Khan"]})') 
print(f'{candidates[1]}: {cVotes:.3f}%  ({Dict1["Correy"]})')
print(f'{candidates[2]}: {lVotes:.3f}%  ({Dict1["Li"]})')
print(f'{candidates[3]}: {tVotes:.3f}%  (', end = '') 
print(Dict1["O'Tooley"], end = '')
print(')')
print(f'----------------------------')
print(f'Winner: {WIN}')
print(f'----------------------------')

#Define outPath and create new file
outPATH = os.path.join("Analysis", "TestPath2.txt")

#Open new file and print
with open(outPATH, "w") as text2:

    text2.write(f'Election Results\n')
    text2.write(f'----------------------------\n')
    text2.write(f'Total Votes: {len(totalVotes)}\n')
    text2.write(f'----------------------------\n') 
    text2.write(f'{candidates[0]}: {kVotes:.3f}%  ({Dict1["Khan"]})\n') 
    text2.write(f'{candidates[1]}: {cVotes:.3f}%  ({Dict1["Correy"]})\n')
    text2.write(f'{candidates[2]}: {lVotes:.3f}%  ({Dict1["Li"]})\n')
    text2.write(f'{candidates[3]}: {tVotes:.3f}%  (') 
    text2.write(str(Dict1["O'Tooley"]))
    text2.write(f')\n')
    text2.write(f'----------------------------\n')
    text2.write(f'Winner: {WIN}\n')
    text2.write(f'----------------------------')
