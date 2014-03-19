'''
Created on Mar 19, 2014
this modules shows how to use perceptron for data set classification
@author: yimin.nie
'''
from numpy import *
'''
create a data sample in a list: the final col represent the class labels: 1 or -1
the remaining data represent the data points, here we use 2-d data point
'''
def createDataSet():
    list = [[3,3,1],[4,3,1],[1,1,-1]]
    return list
'''
load the preprocess the data set
return value: data represents the data part, and labels represents class label

'''
def loadData(dataSet):
    dataMat = array(dataSet)
    labels = []
    data = []
    for dataVec in dataMat:
        labels.append(dataVec[-1])
        data.append(dataVec[:-1])
    return data, labels # return the data part and label part separately
        
'''
learning the data set using perceptron: the cost function is defined as E = sum(label *(w*x+b))
(1) set up the initial value for weight w and bias b
(2) for each instance i in the data set, calculate E = labels[i] *(w*x_i+b), 
(3) if the data is classified incorrectly E<=0, update matrix weight and bias b until it converges
'''    
def perceptron(data,labels):
    data = array(data) #make sure that you convert the data part to matrix
    labels = array(labels)
    N = len(data) # the number of instances in the data
    M = len(data[0])  # the dimension of data in each instance
    weight = array(zeros((1,M)))#the weight matrix which is zero initially, here it is better to define in this way such that the matrix manipulation will be consistent with theory w*x.T
    eps = 10**-4          # the threshold of training error
    maxLoop = 500
    b = 0.0      # set a bias to be zero initially
    
    rate = 1 #learning rate
    for loop in range(maxLoop):
        for i in range(N): #for each instance
            E = labels[i] * (sum(weight * data[i])+b)    
            if E<=eps:  
                weight = weight + rate * labels[i] * data[i]
                b = b + rate * labels[i]
                E = labels[i] * (sum(weight * data[i])+b)  
    return weight,b
    
dataSet = createDataSet()
data,labels = loadData(dataSet)    
weight, b = perceptron(data,labels)  
print weight
print b  
