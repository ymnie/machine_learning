'''
Created on Mar 29, 2014
this modules shows how to implement logistic regression for multiple class >2
@author: yimin.nie
'''
'''
create the sample data set with class 1, 0 and -1 as labels
'''
from numpy import *
def createDataSet():
    dataSet = [[1,3,-1],[2,1,0],[1,2,-1],[3,6,1],[1,-2,-1],[4,3,0],[9,8,-1],[7,6,-1],[12,45,1],[13,56,1]]
    return dataSet
'''
preprocess the data set

'''
def loadData(dataSet):
    data = []
    labels = []
    
    for dataVec in dataSet:
        data.append(dataVec[:-1])
        labels.append(dataVec[-1])
    return data,labels

'''
calculate the softmax function for a given class label
y_k = exp(W_k * x) /(sum(exp(W_k * x)))
'''

def softMax(W,x,k,K): # W is the weight matrix, k is the current class index, K is the total number of classes
    deno = 0.0
    W = mat(W)
    x = mat(x)
    for i in range(K):
        deno += exp(x*W[:,i])
    y = exp(x*W[:,k])/(1+deno)
    return y
   
'''
logistic regression algorithm
for class set C = {C_1,C_2,...C_K}
set weight matrix for each class C_k as W_k
'''

'''
count the classes in the data set
'''
def countLabel(labels): #categorise the difference classes from labels input
    labelCount = {}
    for label in labels:
        if label not in labelCount.keys():
            labelCount[label] = []
        labelCount[label].append(label)
    return labelCount
    
def lr(dataSet):
    data,labels = loadData(dataSet)
    N,M =shape(data) # the dimension of the data set, N is the number of instance, M is the dimension of each instance
    x = mat(data)    # training data matrix (n,m)  
    labelCount = countLabel(labels)
    K  = len(labelCount)
    W = ones((M,K))/M  # weight matrix for each class
    W = mat(W)
    maxLoop = 20  # the maximal iteration for this training
    rate = 0.01 # the learning rate
    error = ones((N,1))
    for loop in range(maxLoop):
        for k in range(K): # for each class
            y = softMax(W,x,k,K) #calculate the estimation using model: y is a (N,1) matrix
            error = y-mat(labels).T  # the training error
            W[:,k] += rate* x.T * error #update the weight matrix for class k
    return W

dataSet = createDataSet()
data,labels = loadData(dataSet)
#print data
#print labels
labelCount =  countLabel(labels)
N,M = shape(data)
x= mat(data)
K =len(labelCount)
W = ones((M,K))/float(M)
W= mat(W)
#print x
#print W
#print x*W[:,1]
#print exp(x*W[:,0])
y = softMax(W,x,0,K)
print y
print lr(dataSet)

            
        
    
    
