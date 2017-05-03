#Class to calculate expected sales.
import pyodbc
import shelve

class CRMDB:
    DBurl = 'DRIVER={SQL Server Native Client 10.0};SERVER=localhost;DATABASE=CustomerDATA;UID=kth;PWD=pass'
    #sqlQuery = ' SELECT [Opportunity_Name] ,a.[Contact_Id] ,[Decision_Date] ,[Quote_Total_In_Sys_Currency] ,[Expiry_Date] ,[Probability_To_Close] ,a.[Status] ,[Actual_Decision_Date] ,[Actual_Revenue_Date] ,[SFA_Opportunity_Id] ,a.[Rn_Descriptor] ,a.[Rn_Create_Date] ,[MRM_Project_Id] ,[X_Expected_Revenue_Date] ,[X_Property_Code] ,[X_Price_Group] ,[X_Opportunity_Type] ,[X_Previous_Status] ,[X_Opportunity_Category] ,[X_Total_Quote_Value] ,[X_Won_Timestamp] ,[X_Opportunity_Type_Id] ,[X_Won_Date] ,[Zip] ,a.[Account_Manager_Id],[Contact_Name_Soundex] ,[Address_1] ,[Same_As_Primary_Company] ,[Inactive] ,[Dont_Call] ,[Country] ,[City] ,[X_External_Source_Update_Time] ,[X_Person_Number] ,[X_Dont_Email] ,[X_CustomerId] ,[X_Address_Approved] ,[X_Dont_SMS] ,[X_Dont_SMS_Last_Change] ,[X_Dont_Email_Last_Change] ,[X_SMS_Number] ,[X_KIC_Customer_Ref] FROM [CustomerDATA].[dbo].[Contact] as a join [CustomerDATA].[dbo].[SFA_Opportunity] on a.Contact_Id= [CustomerDATA].[dbo].[SFA_Opportunity].Contact_Id WHERE a.Zip = %s;'

    def __init__(self,zip):

        self.zip = zip
        self.dictList = []

        self.connectToDB()
        self.createDict()



    def connectToDB(self):
        self.cnxn = pyodbc.connect(self.DBurl)
        self.cursor = self.cnxn.cursor()
        query = open('sqlQueries.txt', 'r')

        self.readQ = query.read()
        query = self.readQ % self.zip
        #query = self.sqlQuery % self.zip
        #self.cursor.execute(self.readQ)

        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()




    def createDict(self):
        file = open('columnNames.txt','r')
        file = file.read().split(',')
        for row in self.rows:
            index = 0
            dict = {}
            for value in row:
                dict[file[index]] = value
                index += 1
            self.dictList.append(dict)

DBurl = 'DRIVER={SQL Server Native Client 10.0};SERVER=localhost;DATABASE=CustomerDATA;UID=kth;PWD=pass'
getZIP = "SELECT DISTINCT ZIP FROM [CustomerDATA].[dbo].[Company]"
cnxn = pyodbc.connect(DBurl)
cursor = cnxn.cursor()
cursor.execute(getZIP)
rows = cursor.fetchall()

zipList = []
for row in rows:
    row = str(row)
    row = row.strip("', )").strip("('").strip(" ").replace(" ", "")
   # print(row)
    try:
        row = int(row)
        row =str(row)
        zipList.append(row)
    except ValueError:
        #print(row)
        continue

translator=shelve.open('postnummerTokommun','w')

i = 0
j = []
kommuner =['MalmÃ¶','Limhamn','Upplands VÃ¤sby','Sollentuna','Sigtuna','Lund','Bunkeflostrand','KungsÃ¤ngen','Arlandastad','Bro','Helsingborg','SÃ¶dertÃ¤lje','Nybrostrand','Ã¶stersund','Fagersta','Kristinehamn','Lidingö','Kiruna','Arjeplog','Handen','Vintrie','Lomma','Jokkmokk','TÃ¤by','StrÃ¶msund','Enköping','Alnarp','TygelsjÃ¶','Gånghester','Flen','MÃ¤rsta','Bara','Klagshamn','Lyckeby','HÃ¤ljarp']
kod = [1280,1280,'0114','0163','0191','01281',1280,'0139','0191','0139',1283,'0181',1286,2380,1982,1781,'0186',2584,2506,'0136',1280,1262,2510,'0160',2313,'0381',1262,1280,1490,'0482','0191',1263,1280,1080,1282]
dict ={}
ä = 'Ã¤'
ö = 'Ã¶'

for i in range (0,len(kommuner)):
    dict[kommuner[i]] = kod[i]
    print(kommuner[i],kod[i])


for zip in zipList:
    try:

       # thing = int(translator[zip])
        temp = translator[zip]
        try:
            thing = int(translator[zip])
        except:
            if
            
            print(translator[zip])
    except:
        j.append(zip)
        i = i+1

print('hello')
print(len(zipList))
print(i)
print(j)

#crmdb = CRMDB('71308')
#print(crmdb.dictList[1])