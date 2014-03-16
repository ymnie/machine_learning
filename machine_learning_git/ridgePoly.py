'''
Created on Feb 24, 2014
this module shows how to choose the order and penalty term using 
polynomial regression method
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
def polyRidgeReg(data,K): # optimize the poly fit
    xValue = array(data)[:,0]
    yValue = array(data)[:,1]

    N = len(data)
    lamb = -5.0
    maxLamb = 5.0
    lambMat = lamb*eye(K)
    minE = inf                 #cost function
    xMat = []
    optOmega = zeros((1,K))
    for n in range(N):
        temMat = []
        for k in range(K):
            temMat.append(xValue[n]**k)
        xMat.append(temMat)
    
    
    while lamb<= maxLamb:
        numMat = []
        denoMat = [] # denominator
        for i in range(K):
            temMat = []
            for j in range(K):
                temMat.append(sum(xValue**(i+j)))  
            denoMat.append(temMat)
            numMat.append(sum(yValue*(xValue**i))) 
        numMat = mat(numMat)
        denoMat = mat(denoMat).T+lambMat
        omega = numMat*denoMat.I
        E = 0.5*sum(array(omega*(mat(xMat).T)-mat(yValue))**2) + 0.5*lamb*omega*omega.T
        if E<minE:
            minE = E
            optOmega = omega
        lamb += 0.01
    return optOmega
           

def plotFit(data,K):
    N = len(data)
    lamb = -5.0  #initiate the penalty term lambda
    xValue = array(data)[:,0]
    yValue = array(data)[:,1]
    fig = plt.figure()
    plt.plot(xValue,yValue,'bo')
    xMat = []
    yFit = []
    omega = array(polyRidgeReg(data,K))
    print omega
    for n in range(N):
        temMat = []
        for k in range(K):
            temMat.append(xValue[n]**k)
        xMat.append(temMat)
        yFit.append(sum(omega*temMat))
    plt.plot(xValue,yFit,'r')
    plt.show()
    
    
plotFit(data,6)
