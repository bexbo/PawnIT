from SCBDB import SCBData


def kommunToData(kommuner):
    kommunlist = []
    for kommun in kommuner:
        kommun = kommun.strip('\n').strip(',').strip('"')
        foo = SCBData(kommun)
        kommunlist.append(foo)

    for kommun in kommunlist:
        print(kommun.featureList)

    return kommunlist





kommuner = open('kommuner.txt','r')
kommuner = kommuner.readlines()

kommunlist= kommunToData(kommuner)

