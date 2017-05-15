import shelve
#import pyodbc
#import CRMDB
import SCBDB

# def createCRMDATA():
#     DBurl = 'DRIVER={SQL Server Native Client 10.0};SERVER=localhost;DATABASE=CustomerDATA;UID=kth;PWD=pass'
#     cnxn = pyodbc.connect(DBurl)
#     cursor = cnxn.cursor()
#
#     cursor.execute('SELECT DISTINCT zip FROM [CustomerDATA].[dbo].[Contact] as a join [CustomerDATA].[dbo].[SFA_Opportunity] on a.Contact_Id= [CustomerDATA].[dbo].[SFA_Opportunity].Contact_Id;')
#     zips = cursor.fetchall()
#     a = open('zips','w')
#     for zip in zips:
#         zip =str(zip)
#         a.write(zip)
#     return
#     CRM = shelve.open('CRMData',writeback=True)
#     kommun = shelve.open('postnummerToKommun')
#     kommundata=shelve.open('kommundata')
#     i=0
#
#     for zip in zips:
#         zip = str(zip)
#         zip = zip.replace("'", "").replace("(", "").replace(")", "").replace(" ", "").replace(",", "")
#         try:
#             kommun[zip] = str(kommun[zip])
#             CRM[kommun[zip]]=[]
#         except:
#             continue
#     i=0
#     for zip in zips:
#         zip = str(zip)
#         zip = zip.replace("'","").replace("(","").replace(")","").replace(" ","").replace(",","")
#
#         i=i+1
#         if zip.isdigit():
#             try:
#                 print(i)
#
#                 crm = CRMDB.CRMDB(zip)
#                 crm.createDict()
#                 d = crm.dictList
#                 if d !=[]:
#                     #print(zip)
#
#                     CRM[kommun[zip]].append(d)
#
#                # print(d)
#
#             except:
#                 i = i + 1


#calculates the success rate for every kommun
def calcSuccessRate():
    crm = shelve.open('CRMData')
    ilist=[]
    jlist=[]
    klist =[]
    upper = 0
    middle = 0
    lower = 0
    ulimit = 0.1 #worst rate for upper
    mlimit = 0.1 #worst rate for medium
    entrylimit = 4 #smallest amount
    resDict= {}
    for kommun in crm:
        i = 0 #successful sales
        j = 0 #unsuccessful sales
        k = 0 #number of sales
        for postal in crm[kommun]:

            for sale in postal:

                k =k+1
                if sale['a.[Status] ']==8:
                    i = i+1
                elif sale['a.[Status] ']!=8:
                    j = j+1

       # print('\n')


        if k >= entrylimit:
            if j == 0:
                ilist.append(1)
                upper = upper +1
                resDict[kommun] = '1'
            elif i == 0:
                lower = lower + 1
                ilist.append(0)
                resDict[kommun] = '2'
            else:
                q = i/(i+j)
                ilist.append(q)
                if q >= ulimit:
                    upper =upper+1
                    resDict[kommun] = '1'
                elif q<ulimit and q>=mlimit:
                    middle=middle+1
                    resDict[kommun] = '2'

                else:
                    lower = lower+1

                    resDict[kommun] = '2'

            klist.append(k)
      #  jlist.append(j)
    returnlist =[]
    result = 'upper: %(u)s  middle: %(m)s lower: %(l)s'
    result = result %{'u':upper,'m':middle,'l':lower}
    print(result)
    returnlist.append(result)
    returnlist.append(ilist)
    returnlist.append(klist)
    return resDict


        # ilist.sort()
        # print(len(ilist),list(reversed(ilist)))
        # print(len(klist),klist)
        # print('upper: ', upper,' middle: ',middle,' lower: ',lower)
#
# d = calcSuccessRate()
#
# plzwork = shelve.open('testdatatvaklasser')
# i = 0
# for kommun in d:
#     data = SCBDB.SCBData(kommun)
#     plzwork[kommun] = data.featureList
#     print(i)
#     i = i+1

# for thing in d:
#    print(d[thing],thing)
#

#print(jlist)
       # print(sale['a.[Status] '])
#createCRMDATA()
    #
    # crm = CRMDB.CRMDB(zip)
    #
    #
    # crm.createDict()
    # d = crm.dictList
    #
    #
    # for thing in d:
    #     print(thing['[Zip] '])
    #     print(thing['a.[Status] '])
    #     print(thing['[Quote_Total_In_Sys_Currency] '])
    #
    #
    #
