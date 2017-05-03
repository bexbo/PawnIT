import numpy as np
from sklearn.naive_bayes import GaussianNB
import SCBDB as SCBDB
import kommun_mapper as km
import time
import shelve
from matplotlib import pyplot as plt
from matplotlib import colors
from sklearn.model_selection import train_test_split


def naive_bayes():
    #training data

    X_data = []
    kommuner = []
    d = shelve.open('kommundata','r')
    for key in d:
        if not key.isalpha():
            kommuner.append(key)
    for i in kommuner:
        try:
            X_data.append(d[i])
        except:
            continue
    X = np.array(X_data).astype(np.float)

    #classes

    target = []

## THIS IS WHERE WE ADD THE CLASSIFICATIONS AFTER WE HAVE CALCULATED SUCCESSRATE ETC.

    for i in range(len(X)):
        if i < len(d)/3:
            target.append(0)
        elif i > len(d)/3 and i < 2*len(d)/3:
            target.append(1)
        else:
            target.append(2)

##  REPLACE ABOVE CODE ACCORDING TO PREVIOUS COMMENT.

    Y = np.array(target) #0 = bad, 1 = ok, 2 = good
    X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2)
    clf = GaussianNB()
    GaussianNB(priors=None)
    clf.fit(X_train,Y_train)
    xlim = (-1, 8)
    ylim = (-1, 5)
    xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 71),
                     np.linspace(ylim[0], ylim[1], 81))
    #test data
    predict = clf.predict(X_test)
    print(predict)
    print(clf.score(X_test,Y_test))
    #print(clf.predict([[1,-1]]))
    #clf_pf = GaussianNB()
    #clf_pf.partial_fit(X,Y,np.unique(Y))
    #print(clf_pf.predict([[-0.8,-1]]))

    fig = plt.figure(figsize=(5, 3.75))
    #ax = fig.add_subplot(111)
    #ax.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.binary, zorder=2)

    #ax.set_xlabel('$x$')
    #ax.set_ylabel('$y$')
    plt.plot(X_test,Y_test,'bo',label="woot")
    plt.show()




start = time.time()
naive_bayes()
print(time.time()-start, " sekunder")
