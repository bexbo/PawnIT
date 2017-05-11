import numpy as np
from sklearn.naive_bayes import GaussianNB

import time
import shelve
from matplotlib import pyplot as plt
from matplotlib import colors
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import itertools
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import VarianceThreshold
from CRMAggregate import calcSuccessRate
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import SelectPercentile, f_classif

def random_forest():
    X_train,X_test,Y_train,Y_test,X,Y = pre_process()


    clf = RandomForestClassifier(n_estimators=15)
    clf.fit(X_train,Y_train)

    scores = cross_val_score(clf, X, Y)

    predict = clf.predict(X_test)

    print(clf.score(X_test, Y_test))
    cnf_matrix = confusion_matrix(Y_test, predict)
    class_names = [1, 2, 3]
    plot_confusion_matrix(cnf_matrix, classes=class_names,
                          title='Confusion matrix, without normalization')

    plt.show()

    print(scores , " (random forest score)")

def pre_process():
    labeledData = calcSuccessRate()
    #training data

    X_data = []
    kommuner = []
    d = shelve.open('testdata','r')
    target = []

    banned_features = [24,33,45,51]
    for kommun in labeledData:
        i = 0
        temp = []
        for f in d[kommun]:
            if i not in banned_features:
                temp.append(f)
            i += 1
        X_data.append(temp)
        target.append(labeledData[kommun])

    d.close()



    #
    # for key in d.keys():
    #
    #     if not key.isalpha():
    #         kommuner.append(key)
    #
    # for i in kommuner:
    #     try:
    #         X_data.append(d[i])
    #     except:
    #         continue


    X = np.array(X_data).astype(np.float)
    #classes
   # print(X)
    #sel = VarianceThreshold(threshold=(.8 * (1 - .8)))

    #print(X)


## THIS IS WHERE WE ADD THE CLASSIFICATIONS AFTER WE HAVE CALCULATED SUCCESSRATE ETC.
    #
    # for i in range(len(X)):
    #     if i < len(d)/3:
    #         target.append(0)
    #     elif i > len(d)/3 and i < 2*len(d)/3:
    #         target.append(1)
    #     else:
    #         target.append(2)

##  REPLACE ABOVE CODE ACCORDING TO PREVIOUS COMMENT.

    Y = np.array(target) #0 = bad, 1 = ok, 2 = good

    X_indices = np.arange(X.shape[-1])
    selector = SelectPercentile(f_classif, percentile=10)
    selector.fit(X, Y)
    scores = -np.log10(selector.pvalues_)
    scores /= scores.max()
    plt.bar(X_indices - .45, scores, width=.2,
        label=r'Univariate score ($-Log(p_{value})$)', color='darkorange')

    #sel = SelectKBest(chi2, k=10).fit_transform(X,Y)
    #print(sel.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2)

    #print(X_train,X_test,Y_train,Y_test,X,Y)
    return X_train,X_test,Y_train,Y_test,X,Y

def naive_bayes():
    X_train,X_test,Y_train,Y_test,X,Y = pre_process()
    clf = GaussianNB()
    GaussianNB(priors=None)
    clf.fit(X_train,Y_train)
    xlim = (-1, 8)
    ylim = (-1, 5)
    xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 71),
                     np.linspace(ylim[0], ylim[1], 81))
    #test data
    predict = clf.predict(X_test)
    print(predict,'Hello')
    print(clf.score(X_test,Y_test))
    cnf_matrix = confusion_matrix(Y_test, predict)
    class_names = [1,2,3]
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

    np.set_printoptions(precision=2)

    # Plot non-normalized confusion matrix
    plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=class_names,
                      title='Confusion matrix, without normalization')

    plt.show()

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


start = time.time()
random_forest()
naive_bayes()

print(time.time()-start, " sekunder")
