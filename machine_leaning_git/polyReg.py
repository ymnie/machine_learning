'''
Created on Feb 24, 2014
this module gives the algorithms of polynomial regression
@author: yimin.nie
'''
from numpy import *
import matplotlib.pyplot as plt

'''
generate the testing data set
'''
def createDataSet(N):
    data = []
    for i in range(N):
        data.append([i,sin(0.1*i)+random.rand()])
    return data
data = createDataSet(100)  

'''
fit the data set using polynomial regression algorithm
'''
def polyReg(data, K): # K is the order we use for
    xVal = array(data)[:,0]
    yVal = array(data)[:,1]
    numMat = []  # numerator
    denoMat = [] # denominator
    N = len(data)
    for i in range(K):
        temMat = []
        for j in range(K):
            temMat.append(sum(xVal**(i+j)))  
        denoMat.append(temMat)
        numMat.append(sum(yVal*(xVal**i))) 
    numMat = mat(numMat)
    denoMat = mat(denoMat).T
    omega = numMat*denoMat.I
    return omega   #return the parameters

def plotFit(data,K):
    N = len(data)
    xValue = array(data)[:,0]
    yValue = array(data)[:,1]
    fig = plt.figure()
    plt.plot(xValue,yValue,'bo')
    xMat = []
    yFit = []
    omega = array(polyReg(data,K))
    for n in range(N):
        temMat = []
        for k in range(K):
            temMat.append(xValue[n]**k)
        xMat.append(temMat)
        yFit.append(sum(omega*temMat))
    print yFit
    plt.plot(xValue,yFit,'r')
    plt.show()

K = 9
omega = polyReg(data,K)
print omega
plotFit(data,K)

        
    
    
    
    
    
    
    
