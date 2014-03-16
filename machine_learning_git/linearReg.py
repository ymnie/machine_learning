'''
Created on Feb 23, 2014
this module gives the algorithm for linear regression 
@author: yimin.nie
'''
from numpy import *
import matplotlib.pyplot as plt
'''
create a 2-D data set with size of N
'''
def createDataSet(N):
    data = []
    a =2; b =3
    for i in range(N):
        data.append([i,a+b*i+50*random.rand()]) 
    return data

'''
linear regression algo
'''
def linearReg(data):
    N = len(data)
    xVec = array(data)[:,0] # xValue
    yVec = array(data)[:,1] # yValue
    numMat = mat([sum(yVec),sum(xVec*yVec)])
    denoMat = mat([[N,sum(xVec)],[sum(xVec),sum(array(xVec)**2)]])
    returnMat = numMat*denoMat.I
    return returnMat[0,0],returnMat[0,1]
'''
plotting the regression curve
'''
def plotRegCurve(data,xVec,yVec):
    fig = plt.figure()
    a, b = linearReg(data)
    plt.plot(array(data)[:,0],array(data)[:,1],'b.')
    plt.plot(xVec,a+b*xVec,'r')
    plt.show()
    

data = createDataSet(100)
returnMat = linearReg(data)
xVec = array(data)[:,0] # xValue
yVec = array(data)[:,1] # yValue

plotRegCurve(data,xVec,yVec)


