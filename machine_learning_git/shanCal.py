'''
Created on Feb 27, 2014
this module shows how to calculate Shannon information and split input data according 
to the information gain
H = - sum(p_i log p_i)
@author: yimin.nie
'''
'''
create a test data set
'''
from numpy import *
'''
calculate the Shannon information
'''
def shannCal(data):
    N = len(data)
    labelCount = {}
    for feat in data:
        currentLab = feat[-1]
        if currentLab not in labelCount.keys():
            labelCount[currentLab] = 0
        labelCount[currentLab] += 1
    print labelCount
    shannEnt = 0.0 
    for keys in labelCount:
        p = float(labelCount[keys])/N
        shannEnt -= p * log(p)
    return shannEnt

'''
data set splitting on a given feature

'''
def splitData(data,n): #split the data set from the nth col
    restData = []
    for feat in data:
            reducedVec = feat[:n]
            reducedVec.extend(feat[n+1:])
            restData.append(reducedVec)
    return restData

'''
choose the best way to split the data set according to information gain
'''
def optSplit(data):
    optN  = 0
    shannEnt = shannCal(data)
    bestInfoGain = 0.0
    bestFeature = -1
    N = len(data[0])
    for n in range(N):
        splitedData = splitData(data,n)
        newShannEnt = shannCal(splitedData)
        inforGain = shannEnt - newShannEnt
        if inforGain>bestInfoGain:
            bestInforGain = inforGain
            bestFeature = n
    return bestFeature











