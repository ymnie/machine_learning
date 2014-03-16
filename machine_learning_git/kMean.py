'''
Created on Feb 24, 2014
this module shows the k-means clustering algorithm
@author: yimin.nie
'''
from numpy import *
import matplotlib.pyplot as plt
'''
load the data set
'''
def loadData(filename):
    data = []
    fr = open(filename)
    for line in fr.readlines():
        line = line.strip().split('\t')
        data.append([float(line[0]),float(line[1])]) # here please note that we must convert string to float when load the data
    
    return data
'''
calculate the distance between two points
'''
def dist(x,y):
    return sqrt(sum((x-y)**2))
'''
randomly set up k centres, the ideas is that we first set up the k*n matrix 
such that each row of this matrix represents a central point corresponding to 
cluster k, which will be moved later.

then we randomly sample the coordinates for these k points as initiation
'''
def setCenter(data,k): # k is the total number of cluster needed
    data = mat(data)
    n = shape(data)[1] # the dimension of each data point
    centers = mat(zeros((k,n))) # k centers
    for j in range(n):
        minJ = min(data[:,j])
        rangeJ = float(max(data[:,j]) - minJ)
        centers[:,j] = minJ + rangeJ * random.rand(k,1)
    return centers
data = loadData('testset.txt')
data = array(data)
centers = setCenter(data,4)
print setCenter(data,10)

'''
k-means clustering algorithm
'''
def kMeans(data,k,centers):
    m = shape(data)[0] # the total numbers of data points in this data set
    cluster = mat(zeros((m,2)))
    centers = setCenter(data,k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m): # for each point
            minDist = inf
            minInd = -1
            for j in range(k):
                distIJ = dist(centers[j,:],data[i,:])
                if distIJ < minDist:
                    minDist = distIJ
                    minIndex = j
            if cluster[i,0]!= minIndex: clusterChanged = True
            cluster[i,:] = minIndex,minDist**2
        for cent in range(k):
            ptsInClust = data[nonzero(cluster[:,0].A == cent)[0]]
            centers[cent,:] = mean(ptsInClust, axis = 0)
    return centers, cluster
        
        
        
        
        
        
        
        
        
        
     
import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot(data[:,0],data[:,1],'b.')
plt.plot(centers[:,0],centers[:,1],'r+')
plt.show()
'''   
data = loadData('ex0.txt') 
data = array(data)
minJ = min(data[:,0])
maxJ = max(data[:,0])
print maxJ
print minJ
z = maxJ - minJ
print z
'''