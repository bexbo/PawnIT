import requests
import json
import codecs


class SCBData:
    municipalities = '"1261"'
    queries =['{ "query": [ { "code": "Region", "selection": { "filter": "vs:RegionKommun07EjAggr", "values": [ %s ] } }, { "code": "Hushallstyp", "selection": { "filter": "item", "values": [ "E90" ] } }, { "code": "ContentsCode", "selection": { "filter": "item", "values": [ "000000KD", "000000KE" ] } }, { "code": "Tid", "selection": { "filter": "item", "values": [ "2015" ] } } ], "response": { "format": "json" } }','{ "query": [ { "code": "Region", "selection": { "filter": "vs:RegionKommun07EjAggr", "values": [ "%s" ] } }, { "code": "Kon", "selection": { "filter": "item", "values": [ "1+2" ] } }, { "code": "TillgangSkuld", "selection": { "filter": "item", "values": [ "CNETTO" ] } }, { "code": "Tid", "selection": { "filter": "item", "values": [ "2007" ] } } ], "response": { "format": "json" } }']
    urls =['http://api.scb.se/OV0104/v1/doris/sv/ssd/START/HE/HE0110/HE0110G/Tab4bDispInkN','http://api.scb.se/OV0104/v1/doris/sv/ssd/START/HE/HE0104/TillgOversiktReg']

    # Disponibel inkomst för hushåll. Medelvärde, tkr efter region, hushållstyp, ålder och år
    # medelvärde, median tkr
    url1 ="http://api.scb.se/OV0104/v1/doris/sv/ssd/START/HE/HE0110/HE0110G/Tab4bDispInkN"
    q1 ='{ "query": [ { "code": "Region", "selection": { "filter": "vs:RegionKommun07EjAggr", "values": [ %s ] } }, { "code": "Hushallstyp", "selection": { "filter": "item", "values": [ "E90" ] } }, { "code": "ContentsCode", "selection": { "filter": "item", "values": [ "000000KD", "000000KE" ] } }, { "code": "Tid", "selection": { "filter": "item", "values": [ "2015" ] } } ], "response": { "format": "json" } }'

    #Förmögenhetsstatistik för personer efter region, kön, tillgångar/skulder, tabellinnehåll och år
     # Totalsumma, milj kr, Antal personer som har respektive tillgång/skuld,Medelvärde, tillgångar och skulder för samtliga personer, tkrMedelvärde för personer som äger tillgång/har skuld, tkr
    url2 ='http://api.scb.se/OV0104/v1/doris/sv/ssd/START/HE/HE0104/TillgOversiktReg'
    q2 ='{ "query": [ { "code": "Region", "selection": { "filter": "vs:RegionKommun07EjAggr", "values": [ "%s" ] } }, { "code": "Kon", "selection": { "filter": "item", "values": [ "1+2" ] } }, { "code": "TillgangSkuld", "selection": { "filter": "item", "values": [ "CNETTO" ] } }, { "code": "Tid", "selection": { "filter": "item", "values": [ "2007" ] } } ], "response": { "format": "json" } }'
    def __init__(self,postNumber):
        self.featureList = []
        self.postNumber=postNumber
        self.q1 = self.q1 % self.postNumber
        self.postQueries()




    def postQueries(self):

        for i in range(0,len(self.queries)):

            self.queries[i] = self.queries[i] % self.postNumber
            r = requests.post(self.urls[i], self.queries[i])

            data = json.loads(r.content[3:])['data']
            self.appendToList(data)

        # self.r = requests.post(self.url1, self.q1)
        # self.data = json.loads(self.r.content[3:])['data']
        # self.appendToList()

    def appendToList(self,data):
        for row in data:
            for value in row['values']:
                self.featureList.append(value)






#1261 = kävlinge
foo = SCBData(1261)
print(foo.featureList)