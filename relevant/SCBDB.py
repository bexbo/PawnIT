import requests
import json
import time


class SCBData:
    def __init__(self,postNumber):
        self.featureList = []
        self.postNumber=postNumber
        self.queries =['{ "query": [ { "code": "Region", "selection": { "filter": "vs:RegionKommun07EjAggr", "values": [ "%s" ] } }, { "code": "Hushallstyp", "selection": { "filter": "item", "values": [ "E90" ] } }, { "code": "ContentsCode", "selection": { "filter": "item", "values": [ "000000KD", "000000KE" ] } }, { "code": "Tid", "selection": { "filter": "item", "values": [ "2015" ] } } ], "response": { "format": "json" } }','{ "query": [ { "code": "Region", "selection": { "filter": "vs:RegionKommun07EjAggr", "values": [ "%s" ] } }, { "code": "Kon", "selection": { "filter": "item", "values": [ "1+2" ] } }, { "code": "TillgangSkuld", "selection": { "filter": "item", "values": [ "CNETTO" ] } }, { "code": "Tid", "selection": { "filter": "item", "values": [ "2007" ] } } ], "response": { "format": "json" } }','{ "query": [ { "code": "Region", "selection": { "filter": "item", "values": [ "%s" ] } }, { "code": "Forbrukar", "selection": { "filter": "item", "values": [ "99" ] } } ], "response": { "format": "json" } }','{ "query": [ { "code": "Region", "selection": { "filter": "vs:RegionKommun07EjAggr", "values": [ "%s" ] } }, { "code": "ContentsCode", "selection": { "filter": "item", "values": [ "000000M5" ] } }, { "code": "Tid", "selection": { "filter": "item", "values": [ "2016" ] } } ], "response": { "format": "json" } }','{ "query": [ { "code": "Region", "selection": { "filter": "item", "values": [ "%s" ] } }, { "code": "Kategori", "selection": { "filter": "item", "values": [ "9", "91", "92", "93", "94", "95", "96", "961", "9611", "962", "963" ] } }, { "code": "Energityp", "selection": { "filter": "item", "values": [ "14", "16", "Totalt" ] } }, { "code": "Tid", "selection": { "filter": "item", "values": [ "2008" ] } } ], "response": { "format": "json" } }','{ "query": [ { "code": "Region", "selection": { "filter": "item", "values": [ "%s" ] } }, { "code": "Produktionssatt", "selection": { "filter": "item", "values": [ "Totalt" ] } }, { "code": "Bransle", "selection": { "filter": "item", "values": [ "17", "950" ] } }, { "code": "Tid", "selection": { "filter": "item", "values": [ "2008" ] } } ], "response": { "format": "json" } }']
        self.urls =['http://api.scb.se/OV0104/v1/doris/sv/ssd/START/HE/HE0110/HE0110G/Tab4bDispInkN','http://api.scb.se/OV0104/v1/doris/sv/ssd/START/HE/HE0104/TillgOversiktReg','http://api.scb.se/OV0104/v1/doris/sv/ssd/START/EN/EN0123/InstSolcell','http://api.scb.se/OV0104/v1/doris/sv/ssd/START/BE/BE0101/BE0101S/HushallT09','http://api.scb.se/OV0104/v1/doris/sv/ssd/START/EN/EN0203/EnergiKommKat','http://api.scb.se/OV0104/v1/doris/sv/ssd/START/EN/EN0203/ProdbrElOv']
        self.postQueries()

    def __str__(self):
        return self.featureList

    def postQueries(self):
        for i in range(0,len(self.queries)):
            self.queries[i] = self.queries[i] % self.postNumber

            r = requests.post(self.urls[i], self.queries[i])

            data = json.loads(r.content[3:])['data']
            print(len(data), data)
            self.appendToList(data)
            time.sleep(0.75) #do not remove, only 10 requests per 10 seconds to the DB are allowed


    def appendToList(self,data):
        for row in data:
            for value in row['values']:
                if value == '.' or value == '..':
                    value = 0
                self.featureList.append(float(value))


def kommunToData(filename):
    kommuner = open(filename,'r')

    kommuner = kommuner.readlines()

    kommunlist = []
    for kommun in kommuner:
        kommun = kommun.strip('\n').strip(',').strip('"')
        #foo = SCBData(kommun)
        #kommunlist.append(foo.featureList)
        kommunlist.append(kommun)
    return kommunlist

#
# foo = SCBData('1280')
#
# for thing in foo.queries:
#     print (thing)
#
# for bo in foo.urls:
#     print(bo)
#
# print(len(foo.featureList), foo.featureList)

# kommuner = open('kommuner.txt','r')
# kommuner = kommuner.readlines()
# kommunlist = []
# for kommun in kommuner:
#     kommun = kommun.strip('\n').strip(',').strip('"')
#     foo = SCBData(kommun)
#     kommunlist.append(foo)
#
# for kommun in kommunlist:
#     print(kommun.featureList)
