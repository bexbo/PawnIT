import shelve
import pyodbc
import CRMDB

DBurl = 'DRIVER={SQL Server Native Client 10.0};SERVER=localhost;DATABASE=CustomerDATA;UID=kth;PWD=pass'
cnxn = pyodbc.connect(DBurl)
cursor = cnxn.cursor()

cursor.execute('SELECT DISTINCT ZIP FROM [CustomerDATA].[dbo].[Company]')
zips = cursor.fetchall()

#CRM = shelve.open('CRMData')
kommun = shelve.open('postnummerToKommun')
kommundata=shelve.open('kommundata')
i=0
for zip in zips:
    zip = str(zip)
    zip = zip.replace("'","").replace("(","").replace(")","").replace(" ","").replace(",","")


    if zip.isdigit():
        try:
            kommun[zip] 
            crm = CRMDB.CRMDB(zip)
            crm.createDict()
            d = crm.dictList
            if d ==[]:
                print(zip)
           # print(d)

        except:

            i = i + 1

print(len(zips))
print(i)



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
