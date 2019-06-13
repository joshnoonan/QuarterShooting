import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import copy

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

allD = np.load('allDict.npy').item()
statD = np.load('statDict.npy').item()


firstQ = [allD[team]['1'] for team in allD.keys()]
secondQ =[allD[team]['2'] for team in allD.keys()]
thirdQ = [allD[team]['3'] for team in allD.keys()]
fourthQ = [allD[team]['4'] for team in allD.keys()]

teams = [key for key in allD.keys()]

#format of tuple is (shooting percentage, z score)

firstQuarter = {}
for x,y in zip(teams,firstQ):
    firstQuarter[x] = (y, ((y-(statD['1st Quarter'][0]))/(statD['1st Quarter'][1])))

secondQuarter = {}
for x,y in zip(teams,secondQ):
    secondQuarter[x] = (y, ((y-(statD['2nd Quarter'][0]))/(statD['2nd Quarter'][1])))

thirdQuarter = {}
for x,y in zip(teams,thirdQ):
    thirdQuarter[x] = (y, ((y-(statD['3rd Quarter'][0]))/(statD['3rd Quarter'][1])))

fourthQuarter = {}
for x,y in zip(teams,fourthQ):
    fourthQuarter[x] = (y, ((y-(statD['4th Quarter'][0]))/(statD['4th Quarter'][1])))
    

quarters = [firstQuarter, secondQuarter, thirdQuarter, fourthQuarter]
np.save('quarters.npy',quarters)
teamQ = []
for quarter in quarters:
    teamQ.append(keywithmaxval(quarter))

bestQ = {}

for x,y in zip(teamQ,quarters):
    bestQ[x] = y[x]
    print(x, ":",  y[x])

print(bestQ)
    


