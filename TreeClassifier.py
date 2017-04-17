import SCBDB
import time
from sklearn import tree

start = time.time()


kommunlist = SCBDB.kommunToData('kommuner.txt')


for kommun in kommunlist:
    for f in kommun:
        print(type(f))
        print(f)

clf = tree.DecisionTreeClassifier()
klasser = [1261,1266,1276,1280,1281]
clf = clf.fit(kommunlist,klasser)

test = SCBDB.SCBData(1272).featureList
clf.predict(test)



print(time.time()-start )
#for kommun in kommunlist:
 #   print(kommun.featureList)

