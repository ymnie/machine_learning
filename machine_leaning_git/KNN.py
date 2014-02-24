'''
Created on Feb 12, 2014

@author: yimin.nie
for each point x in the data set, calculate the distance between x and given center point x0
then sort the distances in increasing order
take k items with lowest distances to x0
mark these data
'''
from numpy import *
import matplotlib.pyplot as plt
from myalgo import quickSort
from myalgo import dist
'''
#import data with python
#in the following function createDataSet, we create the primitive data sets using array 
then we assign labels for each features in the data set. in this data set, one row represents
one feature.
'''
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels
group, labels = createDataSet()

'''
the following function classify0 shows how the find nearest neighbours from given centre point 
inX.

'''
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]# here dataSet.shape[0] means it return the row number not the col number
    diffMat = tile(inX, (dataSetSize , 1)) - dataSet # this means we tile the inX over the matrix
    sqDiffMat = diffMat**2 # calculate the squared distance
    sqDistances = sqDiffMat.sum(axis = 1)# this means it adds all elements along the col not row
    distances = sqDistances**0.5
    sortedDistIndices = distances.argsort()# this sorted the array and return the index
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sort(classCount.iteritems(),key = None,reverse = True)
    return sortedClassCount[0][0]

def classify(data, x0, K):
    distance = []
    for i in range(len(data)):
        distance.append(dist(data[i],x0))
    quickSort(distance)
    return distance[1:K]

def autoNorm(dataSet):
    minVal = dataSet.min(0)
    maxVal = dataSet.max(0)
    ranges = maxVal - minVal
    normSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normSet = dataSet - tile(minVal,(m,1))
    normSet = normSet/tile(ranges,(m,1))
    return normSet, range,min    
    
'''
the following function gives the idea of how to convert from txt file to matrix 
such that we can further use it 
'''    
def getNumOfLine(filename):
    fr = open(filename)
    return len(fr.readlines())


def file2matrix(filename):
    fr = open(filename)
    #numberOfLines = len(fr.readlines())         #get the number of lines in the file
    returnMat = zeros((getNumOfLine(filename),3))        #prepare matrix to return
    valueVec = []  # return values                                      
    labelVec = []  #prepare labels return
    index = 0
    for line in fr.readlines():
        line = line.strip()
        valueVec.append(line.split('\t'))
    for index in range(len(valueVec)):
        returnMat[index,:] = valueVec[index][0:3]
        labelVec.append(valueVec[index][-1])
    return returnMat,labelVec
returnMat,labelVec = file2matrix('datingTestSet.txt')
print returnMat
print labelVec[0:20]

fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.scatter(returnMat[:,1],returnMat[:,2])
plt.plot(returnMat[:,1],returnMat[:,2],'.')
plt.show()
'''
the following function openFile gives how to convert from the .txt file to list

def openFile(filename):
    fr= open(filename)
    vec = []
    for line in fr.readlines():
        line= line.strip() # this eliminates the \n from each line
        vec.append(line.split('\t')) # this eliminates \t from each line
    return vec
returnVec = openFile('datingTestSet.txt')
returnMat = zeros((1000,3))
print returnVec[0]
for index in range(len(returnVec)):
    returnMat[index,:] = returnVec[index][0:3]
print returnMat
'''
