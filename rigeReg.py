'''
Created on Feb 24, 2014
this module shows how to ovrcome the overfitting or underfitting 
problems in linear or polynomial regressions
@author: yimin.nie
'''
from numpy import *
import matplotlib.pyplot as plt
'''
create a 2-D data set with size of N
'''

def createDataSet(N):
    data = []
    a=2;b=3
    for i in range(N):
        data.append([i,a+b*i+100*random.rand()]) 
    return data
'''
linear regression by setting up regular term: lambda

'''
def rigeLinear(data):
    N = len(data)
    xValue = array(data)[:,0]
    yValue = array(data)[:,1]
    lamb  = -5.0 #set up the range of lambda
    maxLamb = 5.0
    optA = 2
    optB = 3
    optLamb = lamb
    minE = Inf # cost function
    while lamb <= maxLamb:
        numMat = mat([sum(yValue),sum(xValue*yValue)])
        denoMat = mat([[N+lamb,sum(xValue)],[sum(xValue),lamb+sum(xValue**2)]])
        a = (numMat*denoMat.I)[0,0]
        b = (numMat*denoMat.I)[0,1]
        E = 0.5*sum((a+b*xValue-yValue)**2)+0.5*lamb*(a**2+b**2)
        print E
        if E<minE:
            minE = E
            optA = a
            optB = b
            optLamb = lamb
        lamb += 0.05
    return optA,optB,optLamb
        
def plotRegCurve(data):
    xValue = array(data)[:,0]
    yValue = array(data)[:,1]
    fig = plt.figure()
    a, b,lamb = rigeLinear(data)
    plt.plot(array(data)[:,0],array(data)[:,1],'b.')
    plt.plot(xValue,a+b*xValue,'r')
    plt.show()

data = createDataSet(100)
plotRegCurve(data)
    