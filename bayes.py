'''
Created on Feb 13, 2014
this module gives the idea of how to use naive Bayesian method to classify the document

this code give us the basic idea of how to process a word documents
1. we first need to load the raw data and convert the entire data set into one vector
   using function createVocabList
2. then we call function setOfWords2Vec to convert the showing up of each input word by 0 or 1,
 0 represent the word from your inputs is not in your vocabulary, 1 represents the word is in it
@author: yimin.nie
'''

'''
summary:  how to use bayes algorithms for email system
(1) load row data and output it as the list: loadDateFrom(your file name), note that if yo use set, the string will be 
    sorted
(2) parsing the data list such that punctuations will be removed
    use textParsing(String)
(3) create dictionary from each input email, finally you got one list with all words
(4) call bayes training method to train the data sets 

'''
from numpy import *

'''
the fucntion loadDataSet gives the idea of how to create the list for words
'''
def loadDataSet():
    postingList = [['my','dog','has','flea',\
                    'problems','help','please'],
                   ['maybe','not','take','him',\
                    'to','dog','park','stupid'],
                   ['my','dalmation','is','so','cute',\
                    'I','love','him'],
                   ['stop','posting','stupid','worthless','garbage'],
                   ['mr','licks','ate','my','steak','how',\
                    'to','stop','him'],
                   ['quit','buying','worthless','dog','food','stupid']]
    classVec = [0,1,0,1,0,1] # 1 is abusive, 0 not
    return postingList, classVec
mydata,myclass = loadDataSet()

#the following function shows how to load data set from the .txt file
'''
def loadDataFrom(filename):
    fr = open(filename)
    returnVec = []
    for line in fr.readlines():
        line = line.strip()
        returnVec.extend(line.split('\t'))
    return returnVec

returnVec = loadDataFrom('datingTestSet.txt')
print returnVec

'''
# or you can convert from your data set in this way
def loadDataFrom(filename):
    vec = []
    fr= open(filename)
    import re
    for line in fr.readlines():
        line = line.strip()
        vec.extend(re.split(r'\W*',line))
    return [words for words in vec if len(words)>0]

#print loadDataFrom('spam.txt')

def createVocabList(dataSet):
    vocabSet = set([])
    for token in dataSet:  # here print each line from data set
        vocabSet = vocabSet | set(token) #append each line into the tail of the vocabSet
        #print token
        #print vocabSet
    return list(vocabSet)# finally convert the set into the list

def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1 # record the index of this word in vocabList
        else:
            print "the word: %s is not in my Vocabulary" % word
    return returnVec

listOPost, listClass = loadDataSet() # load the data set and return the conbined list
#print listOPost, listClass
myVocabList = createVocabList(listOPost)# from above combined list, we build a one list containing all
#print myVocabList
#print listOPost[0]
print setOfWords2Vec(myVocabList, listOPost[0])# then call this function to record if the word of input set
                                               # shows up from the given vocabulary list
                                               
'''
the following function calculate the bayersian function for each words in the input documents
according to bayersian method, given the words w_i, we need to infer which class the words belong to,
that is P(c1|w_i) and P(c2|w_i), here let us assume that there are two different categoris c1 and c2
the bayersian theory gives that p(c1|w_i) = p(w_i|c1)*p(c1)/p(w_i)

'''                                   
def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix) #return the row of matrix
    numWords = len(trainMatrix[0]) #return the col of matrix

    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = ones(numWords);p1Num = ones(numWords)
    p0Denom = 2.0; p1Denom = 2.0
    for i in range(numTrainDocs):  # for each documents: here each doc represents each row of matrix
        if trainCategory[i] == 1:  # if this doc is in category 1
            p1Num += trainMatrix[i] # increase the accounting 
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom) # you can change the scale to log
    p0Vect = log(p0Num/p0Denom)
    return p0Vect, p1Vect, pAbusive
'''
trainMat = []
for postinDOc in listOPost:
    trainMat.append(setOfWords2Vec(myVocabList, listClass))
#print myVocabList[1]
#
#print trainNB0(trainMat, listClass)

'''
'''
the following function shows how to convert input string into the disctionary list using 
regular expression
the following section will show how to filter the spam emails using naive bayes
'''

def textParse(bigString):# parse a big string to a list
    import re  # using regular expression
    tokenList = re.split(r'\W*', bigString)
    return [tokens for tokens in tokenList] # filtering 0-9 and a_z
#print textParse(open('spam.txt').read())

'''
the function spamTest gives the basic idea of how to test the input email is spam or not using 
naive bayes
'''
def spamTest(filename):# here we just show the one email txt, if you want to filter more
    #please use interation below
    docList=[]  # to store each email file
    classList=[] # to store the class of spam or normal mail
    fullText=[]
    words = textParse(open(filename).read()) # parsing the input email txt file to a string vector
    docList.append(words) # append this parsed vector into document list
    fullText.extend(words) # create the full text list
    
    vocabList = createVocabList(docList)# here we collect all wordList and create our vocabulary list
    trainingSet = range(50) # create the size of training set
    testSet =[]  # test set list
    for i in range(10):  # this iteration randomly choose the training set
        randIndex = int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList,docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList,docList[docIndex])
        errorCount += 1    






        