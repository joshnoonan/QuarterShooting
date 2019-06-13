import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import copy

def shootper(l):
    return (l.count('Made Shot') / len(l))

with open('reg1719.csv','r') as f:
        csvf = csv.reader(f)
        result = []
        for row in csvf:
            if row[1].isdigit():
                result.append(row)

d ={'1' : [], '2': [], '3': [], '4':[]}

allD = {}

for row in result:
    if row[6] not in allD.keys():
        allD[row[6]] = copy.deepcopy(d) #each team corresponds to a copy of template dict 'd'

for row in result:
    if int(row[7]) < 5:
        allD[row[6]][row[7]].append(row[10])

newD = copy.deepcopy(allD)

for team in allD.keys():
    allD[team]['1'] = shootper(allD[team]['1'])
    allD[team]['2'] = shootper(allD[team]['2'])
    allD[team]['3'] = shootper(allD[team]['3'])
    allD[team]['4'] = shootper(allD[team]['4'])

# make list of shooting percentage by quarter

firstQ = [allD[team]['1'] for team in allD.keys()]
secondQ =[allD[team]['2'] for team in allD.keys()]
thirdQ = [allD[team]['3'] for team in allD.keys()]
fourthQ = [allD[team]['4'] for team in allD.keys()]

#calculate means

firstMean = np.mean(firstQ)
secondMean = np.mean(secondQ)
thirdMean = np.mean(thirdQ)
fourthMean = np.mean(fourthQ)

#calculate standard deviation

firstSTD = np.std(firstQ)
secondSTD = np.std(secondQ)
thirdSTD = np.std(thirdQ)
fourthSTD = np.std(fourthQ)

statD = {'1st Quarter' : (firstMean,firstSTD),
         '2nd Quarter' : (secondMean,secondSTD),
         '3rd Quarter' : (thirdMean, thirdSTD),
         '4th Quarter' : (fourthMean, fourthSTD)}


np.save('allDict.npy', allD)
np.save('statDict.npy', statD)








    
