'''
Created on Feb 25, 2014
this module show how to use local kernel to optimize the linear regression fitting
@author: yimin.nie
'''
from numpy import *
def loadData(filename):
    fr = open(filename)
    data = []
    for line in fr.readlines():
        line = line.strip().split('\t')
        data.append([float(line[1]),float(line[2])])
    return data

'''
assign kernel matrix for input data sets
''' 
def W(data,sigma):
    x = array(data)[:,0]
    N = len(x)
    w = zeros((N,N))
    for i in range(N):
        for j in range(N):
            w[i][j] = exp(abs(x[i]-x[j])/(-2*sigma**2))
    return w

def localKernelLinear(data,sigma):
    x = array(data)[:,0]
    y = array(data)[:,1]
    w = W(data,sigma)
    omega = (mat(x)*w*mat(x).T)**(-1)*(mat(x)*W*mat(y).T)
    print omega

def plotFit(data):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    x = array(data)[:,0]
    y = array(data)[:,1]
    plt.plot(x,y,'b.')
    plt.show()
    
data = loadData('ex0.txt')
plotFit(data)    
#localKernelLinear(data,2)
print random.rand(4,1)  
    
    
    
    
    
    
    
    
    
    