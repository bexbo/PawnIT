import numpy as np
from sklearn.naive_bayes import GaussianNB
from SCBDB import *


def naive_bayes():
    #training data
    X = np.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
    kommunerlist = SCBDB.kommunToData('kommuner.txt')

    #classes
    Y = np.array([1,1,1,2,2,2])
    
    clf = GaussianNB()
    GaussianNB(priors=None)
    clf.fit(X,Y)
    #test data
    print(clf.predict([[1,-1]]))
    clf_pf = GaussianNB()
    clf_pf.partial_fit(X,Y,np.unique(Y))
    print(clf_pf.predict([[-0.8,-1]]))

naive_bayes()
