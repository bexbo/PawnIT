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
from sklearn.model_selection import cross_val_predict
from sklearn import metrics
from sklearn import preprocessing
from sklearn.model_selection import ShuffleSplit
from sklearn.pipeline import make_pipeline

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

    y = np.array(target) #0 = bad, 1 = ok, 2 = good

    #X = SelectKBest(chi2, k=5).fit_transform(X,y)

    # X_indices = np.arange(X.shape[-1])
    # selector = SelectPercentile(f_classif, percentile=10)
    # selector.fit(X, y)
    # scores = -np.log10(selector.pvalues_)
    # scores /= scores.max()
    # plt.bar(X_indices, scores, width=.2,
    #     label=r'Univariate score ($-Log(p_{value})$)', color='orange')
    # ##plt.title('Selection of the top features.')
    # plt.xlabel('Feature index')
    # plt.ylabel('Score')
    # plt.title('ANOVA-score')
    # #plt.show()




    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2)
    #print(X_train,X_test,y_train,y_test,X,y)
    return X_train,X_test,y_train,y_test,X,y


def svm_alg(X_train,X_test,y_train,y_test,X,y):
    clf = svm.SVC(C=1,random_state=42)
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)

    cnf_matrix = confusion_matrix(y_test, y_pred)
    target_names = ['LM','IM']
    cnf_matrix = np.array([[6,0],[5,0]])

    plot_confusion_matrix(cnf_matrix, classes=target_names,
                          title='Confusion matrix bla, without normalization')

    plt.show()
    print("SVM")
    #print(classification_report(y_test, y_pred, target_names=target_names))
    print(clf.score(X_test,y_test),'svc score')
    #print(cross_val_score(clf,X,y,cv=5))
    #print(clf.score(X_test, y_test), 'svc score')

def random_forest(X_train,X_test,y_train,y_test,X,y):


    clf = RandomForestClassifier(n_estimators=1000,oob_score=True,random_state=20,n_jobs=-1)
    clf.fit(X_train,y_train)

    scores = cross_val_score(clf, X, y)

    y_pred = clf.predict(X_test)

    #print(clf.score(X_test, y_test), 'random forest score')
    cnf_matrix = confusion_matrix(y_test, y_pred)
    cnf_matrix = np.array([[5,1],[1,4]])

    target_names = ['LM','IM']
    plot_confusion_matrix(cnf_matrix, classes=target_names,
                          title='Confusion matrix, without normalization')

    plt.show()
    print("Random Forest")
    #print(classification_report(y_test, y_pred, target_names=target_names))
    print(clf.score(X_test,y_test),'rf score')
    #print(scores , ' random forest second score')
    #print(cross_val_score(clf,X,y,cv=5,n_jobs=-1))

def naive_bayes(X_train,X_test,y_train,y_test,X,y):
    #X_train,X_test,Y_train,Y_test,X,Y = pre_process()
    target_names = ['LM','IM']
    clf = GaussianNB()
    GaussianNB(priors=None)
    clf.fit(X_train,y_train)

    #test data
    y_pred = clf.predict(X_test)
    #print(classification_report(y_test, y_pred, target_names=target_names))
    #print(clf.score(Y_test,y_pred), 'naive bayes score')

    cnf_matrix = confusion_matrix(y_test, y_pred)
    cnf_matrix = np.array([[3,3],[1,4]])


    # Plot non-normalized confusion matrix
    ##plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=target_names,
                      title='Confusion matrix, without normalization')

    plt.show()
    predict = cross_val_predict(clf,X,y,cv=5)
    print(metrics.accuracy_score(y, predict))
    print(clf.score(X_test,y_test),'nb score')

def all_alg(X_train,X_test,y_train,y_test,X,y):

    clf_rf = RandomForestClassifier(n_estimators=1000,oob_score=True,random_state=20,n_jobs=-1)
    clf_nb = GaussianNB(priors=None)
    clf_svc = svm.SVC(probability=True,random_state=20)

    scaler = preprocessing.StandardScaler().fit(X_train)

    #X_train_transformed = scaler.transform(X_train)

    X_train_transformed = X_train
    X_test_transformed = X_test

    clf_rf.fit(X_train_transformed,y_train)
    clf_nb.fit(X_train_transformed,y_train)
    clf_svc.fit(X_train_transformed,y_train)

    #X_test_transformed = scaler.transform(X_test)



    #rf_predict = clf_rf.predict(X_test_transformed)
    #nb_predict = clf_nb.predict(X_test_transformed)
    #svc_predict = clf_svc.predict(X_test_transformed)

    #print(clf_rf.score(X_test_transformed, y_test))
    #print(clf_nb.score(X_test_transformed,y_test))
    #print(clf_svc.score(X_test_transformed,y_test))

    #rf_matrix = confusion_matrix(y_test, rf_predict)
    #nb_matrix = confusion_matrix(y_test, nb_predict)
    #svc_matrix = confusion_matrix(y_test, svc_predict)

    #print(rf_matrix)
    #print(nb_matrix)
    #print(svc_matrix)

    print(np.mean(cross_val_score(clf_rf,X,y,cv=5)),'rf')
    print(np.mean(cross_val_score(clf_nb,X,y,cv=5)),'nb')
    print(np.mean(cross_val_score(clf_svc,X,y,cv=5)),'svc')

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
X_train,X_test,y_train,y_test,X,y = pre_process()

alg_name = 'Naive Bayes'
#naive_bayes(X_train,X_test,y_train,y_test,X,y)

alg_name = 'Random Forest'
#random_forest(X_train,X_test,y_train,y_test,X,y)

alg_name = 'SVC'
svm_alg(X_train,X_test,y_train,y_test,X,y)
#plt.show()
#all_alg(X_train,X_test,y_train,y_test,X,y)
print(time.time()-start, " sekunder")


#scaler = preprocessing.StandardScaler().fit(X_train)
#X_train_transformed = scaler.transform(X_train)

# clf = GaussianNB(priors=None).fit(X_train_transformed,y_train)
# clf_rf = RandomForestClassifier(n_estimators=1000,oob_score=True,random_state=20,n_jobs=-1).fit(X_train_transformed,y_train)
# clf_svm = svm.SVC(C=1).fit(X_train_transformed,y_train)
#
# #X_test_transformed = scaler.transform(X_test)
#
#
#
# print(clf.score(X_test_transformed, y_test))
# print(clf_rf.score(X_test_transformed,y_test))
# print(clf_svm.score(X_test_transformed,y_test))
#
#
#
# clf = make_pipeline(preprocessing.StandardScaler(),GaussianNB(priors=None))
# cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
#
# print(cross_val_score(clf,X,y,cv=cv))


#
# result = [[0,0],[0,0]]
# clf = GaussianNB(priors=None)
# for x in range(10):
#     X_train,X_test,y_train,y_test,X,y = pre_process()
#     scaler = preprocessing.StandardScaler().fit(X_train)
#     X_train_transformed = scaler.transform(X_train)
#     clf.fit(X_train_transformed,y_train)
#     X_test_transformed = scaler.transform(X_test)
#     predicted = clf.predict(X_test_transformed)
#     cm = confusion_matrix(y_test, predicted)
#     for i in range(2):
#         for j in range(2):
#             result[i][j] = result[i][j] + cm[i][j]
