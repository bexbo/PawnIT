import numpy as np
from sklearn.naive_bayes import GaussianNB
import SCBDB as SCBDB
import kommun_mapper as km
import time
def naive_bayes():
    #training data
    #X = np.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
    kommunData = SCBDB.kommunToData('kommuner.txt')
    #print(kommunData)
    kommunist = np.array(kommunData).astype(np.float)
    #print(kommunist)
    #classes
    #Y = np.array([1,1,1,2,2,2])
    klasser = np.array([1261,1266,1276,1280,1281])
    #print(klasser)
    clf = GaussianNB()
    GaussianNB(priors=None)
    #clf.fit(X,Y)
    clf.fit(kommunist,klasser)
    #test data
    testKommun = SCBDB.SCBData(1381)
    predict = clf.predict(testKommun.featureList)
    predict = str(predict[0])
    print(km.kommunMap[predict])

    #print(clf.predict([[1,-1]]))
    #clf_pf = GaussianNB()
    #clf_pf.partial_fit(X,Y,np.unique(Y))
    #print(clf_pf.predict([[-0.8,-1]]))

start = time.time()
naive_bayes()
print(time.time()-start)