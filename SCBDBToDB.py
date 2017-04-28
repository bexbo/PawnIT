import SCBDB
import kommun_mapper
import shelve
import time
kommuner = kommun_mapper.kommunDict()





#bar = SCBDB.SCBData('0582')
# 290 kommuner

kommunlist = []

for kommun in kommuner:
    kommunlist.append(kommun)



d= shelve.open('kommundata')
kommuner = kommunlist[160:]


for kommun in kommuner:
     start = time.time()
     kommun = str(kommun)
     tempKommun = SCBDB.SCBData(kommun)
     d[tempKommun.postNumber] = tempKommun.featureList
     print(tempKommun.postNumber)




