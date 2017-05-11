import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=localhost;DATABASE=CustomerDATA;UID=kth;PWD=pass')

cursor = cnxn.cursor()

sql_string_1 = "select Zip, City, Annual_Revenue, Number_Of_Employee, Annual_Number_of_Orders_Map from dbo.Company"
sql_string_2 = "select Decision_Date, Quote_Total_In_Sys_Currency, Quote_Total_In_Oppt_Currency, Status, Pipeline_Stage from dbo.SFA_Opportunity"
sql_string_3 = "select Quote_Sub_Total, Quote_Total from dbo.SFA_Quote"
sql_string_4 = "select Zip, City, Annual_Revenue, Number_Of_Employee, Annual_Number_of_Orders_Map, Decision_Date, Quote_Total_In_Sys_Currency, Quote_Total_In_Oppt_Currency, Pipeline_Stage from dbo.Company join dbo.SFA_Opportunity on dbo.Company.Company_Id = dbo.SFA_Opportunity.Company_Id join dbo.SFA_Quote on dbo.Company.Company_Id = dbo.SFA_Quote.Company_Id"
foo ="select * from dbo.SFA_Opportunity"
boo ='select [CustomerDATA].[dbo].[Contact].Company_Id FROM [CustomerDATA].[dbo].[Company]  join [CustomerDATA].[dbo].[Contact] on [CustomerDATA].[dbo].[Company].[Company_Id]=[CustomerDATA].[dbo].[Contact].Company_Id;'

query = open('sqlQueries.txt','r')

loo = query.read()

#print(loo)
#customerQuery ='select a.Company_ID, a.Zip, a.Annual_Revenue, a.Number_Of_Employee,  from dbo.Company as a; '
cursor.execute(loo)

#dbo.Company (Zip, City, Annual_Revenue, Number_Of_Employee, Annual_Number_of_Orders_Map)
#dbo.SFA.Opportunity (Decision_Date, Quote_Total_In_Sys_Currency, Quote_Total_In_Oppt_Currency, Status, Pipeline_Stage)
#dbo.SFA.Quote (Quote_Sub_Total, Quote_Total)

row = cursor.fetchall()


for thing in row:
    print(thing)




