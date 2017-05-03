import numpy as np
from sklearn.naive_bayes import GaussianNB
import SCBDB as SCBDB
import kommun_mapper as km
import time
import shelve

def naive_bayes():
    #training data
    #X = np.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
    X_data = []
    kommuner = SCBDB.kommunToData('kommuner.txt')
    d = shelve.open('kommundata','r')
    for i in kommuner:
        try:
            X_data.append(d[i])
        except:
            continue
    X = np.array(X_data).astype(np.float)
    #classes
    #Y = np.array([1,1,1,2,2,2])
    #klasser = np.array([1261,1266,1276,1280,1281])
    Y = np.array([0,0,1,1,2])
    #print(klasser)
    clf = GaussianNB()
    GaussianNB(priors=None)
    #clf.fit(X,Y)
    clf.fit(X,Y)
    #test data
    testKommun = d['1381']

    predict = clf.predict(testKommun)
    predict = str(predict[0])
    print(predict)
    #k = km.kommunDict()
    #print(k[predict])

    #print(clf.predict([[1,-1]]))
    #clf_pf = GaussianNB()
    #clf_pf.partial_fit(X,Y,np.unique(Y))
    #print(clf_pf.predict([[-0.8,-1]]))

start = time.time()
naive_bayes()
print(time.time()-start, " sekunder")
