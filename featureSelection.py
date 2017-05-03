from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import shelve
iris = load_iris()
X, y = iris.data, iris.target
print(X.shape)
X_new = SelectKBest(chi2, k=2).fit_transform(X, y)
print(X_new.shape)

d = shelve.open('kommundata','r')
print(d["0120"])
