import SCBDB
import time
from sklearn import tree
import numpy

start = time.time()


kommunlist = numpy.array(SCBDB.kommunToData('kommuner.txt'))


clf = tree.DecisionTreeClassifier()
klasser = numpy.array([1261,1266,1276,1280,1281])
clf = clf.fit(kommunlist,klasser)

test = SCBDB.SCBData(1272).featureList
print(clf.predict(test))



print(time.time()-start )
#for kommun in kommunlist:
 #   print(kommun.featureList)

