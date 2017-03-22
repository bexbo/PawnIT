import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=localhost;DATABASE=ED;UID=kth;PWD=pass')

cursor = cnxn.cursor()

sql_string_1 = "select Zip, City, Annual_Revenue, Number_Of_Employee, Annual_Number_of_Orders_Map from dbo.Company"
sql_string_2 = "select Decision_Date, Quote_Total_In_Sys_Currency, Quote_Total_In_Oppt_Currency, Status, Pipeline_Stage from dbo.SFA_Opportunity"
sql_string_3 = "select Quote_Sub_Total, Quote_Total from dbo.SFA_Quote"
sql_string_4 = "select * from dbo.SFA_Opportunity join (select * from dbo.Company join dbo.SFA_Quote on dbo.Company.Company_Id = dbo.SFA_Quote.Company_Id) as foo on dbo.SFA_Opportunity.Company_Id=foo.Company_Id"
cursor.execute(sql_string_4)

#dbo.Company (Zip, City, Annual_Revenue, Number_Of_Employee, Annual_Number_of_Orders_Map)
#dbo.SFA.Opportunity (Decision_Date, Quote_Total_In_Sys_Currency, Quote_Total_In_Oppt_Currency, Status, Pipeline_Stage)
#dbo.SFA.Quote (Quote_Sub_Total, Quote_Total)

row = cursor.fetchall()


for thing in row:
    print(thing)




