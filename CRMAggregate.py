import shelve
import pyodbc
import CRMDB


def createCRMDATA():
    DBurl = 'DRIVER={SQL Server Native Client 10.0};SERVER=localhost;DATABASE=CustomerDATA;UID=kth;PWD=pass'
    cnxn = pyodbc.connect(DBurl)
    cursor = cnxn.cursor()

    cursor.execute('SELECT DISTINCT zip FROM [CustomerDATA].[dbo].[Contact] as a join [CustomerDATA].[dbo].[SFA_Opportunity] on a.Contact_Id= [CustomerDATA].[dbo].[SFA_Opportunity].Contact_Id;')
    zips = cursor.fetchall()

    CRM = shelve.open('CRMData')
    kommun = shelve.open('postnummerToKommun')
    kommundata=shelve.open('kommundata')
    i=0
    for zip in zips:
        zip = str(zip)
        zip = zip.replace("'","").replace("(","").replace(")","").replace(" ","").replace(",","")


        if zip.isdigit():
            try:
                print(kommun[zip])

                crm = CRMDB.CRMDB(zip)
                crm.createDict()
                d = crm.dictList
                if d !=[]:
                    print(zip)

                    CRM[kommun[zip]] = CRM[kommun[zip]].extend(d)
               # print(d)

            except:
                i = i + 1



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
