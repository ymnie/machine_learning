'''
Created on Feb 24, 2013
this module shows how to classify the data set using logistic function
@author: yimin.nie
'''
from numpy import *
def loadData(filename):
    fr = open(filename)
    data = []
    for line in fr.readlines():
        line = line.strip().split()
        data.append(float(line[0]),float(line[1]))
    return data

def sigmoid(x):
    from math import exp
    return 1.0/(1+exp(-x))

'''
gradient descent algorithms to find the optimal parameters
'''
def gradDecent(data):
    dataMat = mat(data)
    x = array(data)[:,0]
    y = array(data)[:,1]
    m,n = shape(dataMat)
    beta = 0.001 #learning rate
    finalError = 10**(-5)
    error = ones((n,1))
    weights = ones((n,1))   # parameters to be trained
    while error>=finalError:
        h = sigmoid(dataMat*weights)
        error = y - h
        weights -= beta*dataMat.T*error
    return weights
           