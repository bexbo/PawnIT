import requests
import json

class SCBData:
    municipalities = '"1261"'
    # Disponibel inkomst för hushåll. Medelvärde, tkr efter region, hushållstyp, ålder och år
    # medelvärde, median tkr
    url1 ="http://api.scb.se/OV0104/v1/doris/sv/ssd/START/HE/HE0110/HE0110G/Tab4bDispInkN"
    q1 ='{ "query": [ { "code": "Region", "selection": { "filter": "vs:RegionKommun07EjAggr", "values": [ %s ] } }, { "code": "Hushallstyp", "selection": { "filter": "item", "values": [ "E90" ] } }, { "code": "ContentsCode", "selection": { "filter": "item", "values": [ "000000KD", "000000KE" ] } }, { "code": "Tid", "selection": { "filter": "item", "values": [ "2015" ] } } ], "response": { "format": "json" } }'


    def __init__(self,postNumber):
        self.postNumber=postNumber
        self.q1 = self.q1 % self.postNumber
        self.postQuery()


    def postQuery(self):
        self.r = requests.post(self.url1, self.q1)




foo = SCBData(1261)
print(foo.r.text)








