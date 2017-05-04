import shelve
import pyodbc
import CRMDB


def createCRMDATA():
    DBurl = 'DRIVER={SQL Server Native Client 10.0};SERVER=localhost;DATABASE=CustomerDATA;UID=kth;PWD=pass'
    cnxn = pyodbc.connect(DBurl)
    cursor = cnxn.cursor()

    cursor.execute('SELECT DISTINCT zip FROM [CustomerDATA].[dbo].[Contact] as a join [CustomerDATA].[dbo].[SFA_Opportunity] on a.Contact_Id= [CustomerDATA].[dbo].[SFA_Opportunity].Contact_Id;')
    zips = cursor.fetchall()

    CRM = shelve.open('CRMData','w')
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
print(len(crm))
for thing in crm:
    print(thing)


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
