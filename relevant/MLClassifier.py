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
from sklearn import svm
from sklearn.metrics import classification_report


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

    X = np.array(X_data).astype(np.float)
    #classes

    #sel = VarianceThreshold(threshold=(.8 * (1 - .8)))

    Y = np.array(target) #0 = bad, 1 = ok, 2 = good

    X = SelectKBest(chi2, k=10).fit_transform(X,Y)

    X_indices = np.arange(X.shape[-1])
    selector = SelectPercentile(f_classif, percentile=10)
    selector.fit(X, Y)
    scores = -np.log10(selector.pvalues_)
    scores /= scores.max()
    plt.bar(X_indices - .45, scores, width=.2,
        label=r'Univariate score ($-Log(p_{value})$)', color='darkorange')
    #plt.title('Selection of the top features.')
    plt.show()


    #sel = SelectKBest(chi2, k=10).fit_transform(X,Y)
    #print(sel.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2)
    #print(X_train,X_test,Y_train,Y_test,X,Y)
    return X_train,X_test,Y_train,Y_test,X,Y


def svm_alg(X_train,X_test,y_train,y_test,X,y):
    clf = svm.SVC(probability=True)
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)

    cnf_matrix = confusion_matrix(y_test, y_pred)
    target_names = ['hög','medel','låg']
    plot_confusion_matrix(cnf_matrix, classes=target_names,
                          title='Confusion matrix bla, without normalization')

    plt.show()
    print("SVM")
    print(classification_report(y_test, y_pred, target_names=target_names))
    #print(clf.score(X_test, y_test), 'svc score')

def random_forest(X_train,X_test,y_train,y_test,X,y):
    #X_train,X_test,Y_train,Y_test,X,Y = pre_process()


    clf = RandomForestClassifier(n_estimators=15)
    clf.fit(X_train,y_train)

    scores = cross_val_score(clf, X, y)

    y_pred = clf.predict(X_test)

    #print(clf.score(X_test, y_test), 'random forest score')
    cnf_matrix = confusion_matrix(y_test, y_pred)
    target_names = ['1','2','3']
    plot_confusion_matrix(cnf_matrix, classes=target_names,
                          title='Confusion matrix, without normalization')

    plt.show()
    print("Random Forest")
    print(classification_report(y_test, y_pred, target_names=target_names))
    #print(scores , ' random forest second score')


def naive_bayes(X_train,X_test,y_train,y_test,X,y):
    #X_train,X_test,Y_train,Y_test,X,Y = pre_process()
    target_names = ['1','2','3']
    clf = GaussianNB()
    GaussianNB(priors=None)
    clf.fit(X_train,y_train)

    #test data
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred, target_names=target_names))
    #print(clf.score(Y_test,y_pred), 'naive bayes score')

    cnf_matrix = confusion_matrix(y_test, y_pred)


    # Plot non-normalized confusion matrix
    ##plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=target_names,
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
    plt.title(alg_name)

    plt.ylabel('True label')
    plt.xlabel('Predicted label')


start = time.time()
X_train,X_test,Y_train,Y_test,X,Y = pre_process()

alg_name = 'Naive Bayes'
naive_bayes(X_train,X_test,Y_train,Y_test,X,Y)

alg_name = 'Random Forest'
random_forest(X_train,X_test,Y_train,Y_test,X,Y)

alg_name = 'SVC'
svm_alg(X_train,X_test,Y_train,Y_test,X,Y)
#plt.show()
print(time.time()-start, " sekunder")
