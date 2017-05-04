import shelve
import pyodbc
import CRMDB


def createCRMDATA():
    DBurl = 'DRIVER={SQL Server Native Client 10.0};SERVER=localhost;DATABASE=CustomerDATA;UID=kth;PWD=pass'
    cnxn = pyodbc.connect(DBurl)
    cursor = cnxn.cursor()

    cursor.execute('SELECT DISTINCT zip FROM [CustomerDATA].[dbo].[Contact] as a join [CustomerDATA].[dbo].[SFA_Opportunity] on a.Contact_Id= [CustomerDATA].[dbo].[SFA_Opportunity].Contact_Id;')
    zips = cursor.fetchall()
    a = open('zips','w')
    for zip in zips:
        zip =str(zip)
        a.write(zip)
    return
    CRM = shelve.open('CRMData',writeback=True)
    kommun = shelve.open('postnummerToKommun')
    kommundata=shelve.open('kommundata')
    i=0

    for zip in zips:
        zip = str(zip)
        zip = zip.replace("'", "").replace("(", "").replace(")", "").replace(" ", "").replace(",", "")
        try:
            kommun[zip] = str(kommun[zip])
            CRM[kommun[zip]]=[]
        except:
            continue
    i=0
    for zip in zips:
        zip = str(zip)
        zip = zip.replace("'","").replace("(","").replace(")","").replace(" ","").replace(",","")

        i=i+1
        if zip.isdigit():
            try:
                print(i)

                crm = CRMDB.CRMDB(zip)
                crm.createDict()
                d = crm.dictList
                if d !=[]:
                    #print(zip)

                    CRM[kommun[zip]].append(d)

               # print(d)

            except:
                i = i + 1


crm = shelve.open('CRMData')
# print(len(crm))
# for thing in crm:
#     print(thing)
#     print(crm[thing])

ilist=[]
jlist=[]
klist =[]
upper = 0
middle = 0
lower = 0
ulimit = 0.4
mlimit = 0.2
entrylimit = 4
for kommun in crm:
    i = 0
    j = 0
    k = 0
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
        elif i == 0:
            lower = lower + 1
            ilist.append(0)
        else:
            q = i/(i+j)
            ilist.append(q)
            if q >= ulimit:
                upper =upper+1
            elif q<ulimit and q>=mlimit:
                middle=middle+1
            else:
                lower = lower+1

        klist.append(k)
  #  jlist.append(j)

ilist.sort()
print(len(ilist),list(reversed(ilist)))
print(len(klist),klist)
print('upper: ', upper,' middle: ',middle,' lower: ',lower)
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
