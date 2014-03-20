'''
Created on Mar 19, 2014
this module shows how to use naive Bayes method for classification
@author: yimin.nie
'''
from numpy import *

'''
create a small data sample with labels +1 and -1
'''
def createDataSet():
    dataSet = [[1,3,-1],[2,1,1],[1,2,-1],[3,6,1],[1,-2,-1],[4,3,1]]
    return dataSet
'''
preprocess the data set
'''
def loadData(dataSet):
    data = []
    lables = []
    for dataVec in dataSet:
        data.append(dataVec[:-1])
        lables.append(dataVec[-1])
    return data,lables

'''
build a dictionary to classify the sample data set
'''
def dict(dataSet):
    data,lables = loadData(dataSet)
    lableCount = {}
    for i in range(len(data)):
        lable = lables[i]
        if lable not in lableCount:
            lableCount[lable]=[]
        lableCount[lable].extend(data[i])
    return lableCount


'''
find the likelihood p(x|c), given input vector x= {x_1,x_2,..x_n}
according to naive Bayes, p(x|c) = product(p(x_i|c)) for all i
'''
def prob(x,label,dataSet): # calculate the prob of x in class c: p(x|c), given training data set
    count = [ 0 for i in range(len(x))]
    labelCounter = dict(dataSet)
    totalCount= len(labelCounter[label])
    for i in range(len(x)):
        for item in labelCounter[label]:
            if x[i] == item:
                count[i]+=1
        count[i] = float(count[i])/totalCount
    prob = product(count)      
    return prob
'''
find which class a new input x belongs to
'''
def classifyFor(x, dataSet):# determine the class for new input vector x in data set
    labels = loadData(dataSet)[1]
    numLabels = len(labels)
    # first we calculate the priority prob P(c_k)
    labelDic = {}
    for label in labels:
        if label not in labelDic:
            labelDic[label] = 0
        labelDic[label]+=1    
    #then calculate the prob p(x|c)*p(c) for each class c (label), and find the best class which gives 
    # the max prob
    maxProb = -inf
    bestLabel = None
    for label in labelDic:
        p = prob(x,label,dataSet)*(float)(labelDic[label])/numLabels
        if p>maxProb:
            maxProb = p
            bestLabel = label
    return bestLabel
            
dataSet = createDataSet()
data,lables = loadData(dataSet) 
labelCount = dict(dataSet)
print labelCount
label = classifyFor([1,2],dataSet)
print label

    
    
         
    
    