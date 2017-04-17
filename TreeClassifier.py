import SCBDB
import time









kommunlist = SCBDB.kommunToData('kommuner.txt')
start = time.time()
print(kommunlist[0].featureList[0])
print(start - time.time())
#for kommun in kommunlist:
 #   print(kommun.featureList)

