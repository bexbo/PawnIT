import SCBDB
import time
from sklearn import tree
import numpy
from kommun_mapper import kommunDict

start = time.time()

kommunMap = kommunDict()
kommunlist = numpy.array(SCBDB.kommunToData('kommuner.txt'))

clf = tree.DecisionTreeClassifier()
klasser = numpy.array([1261,1266,1276,1280,1281])
clf = clf.fit(kommunlist,klasser)


test = SCBDB.SCBData(1381).featureList
prediction = clf.predict(numpy.array(test))
prediction= str(prediction[0])
print(kommunMap[prediction])


print(time.time()-start )
#for kommun in kommunlist:
 #   print(kommun.featureList)
