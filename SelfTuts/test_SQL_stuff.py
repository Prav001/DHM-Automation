"""This file has a lot of test code for creating SQL server 2008 cursors trough python,
and then using them to create tables, views, updating data, and other db management.
All of these test snippets were later used somewhere or the other in the project."""


import pyodbc
import sys
import logging

   
logging.basicConfig(level=logging.DEBUG, filename='/Python34/Scripts/demosite/textsearch/errors.log')


conn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=RAMCOBL267;DATABASE=AVNAPPDB;UID=sa;PWD=development12$')
#conn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=hqramcot13;DATABASE=AVNAPPDB;UID=sa;PWD=SAyy72Kz')


sql2 = """
if exists( select * from sys.tables where name = 'persons' )
    begin
    drop table persons
    end

CREATE TABLE Persons
    (Per_Id INTEGER IDENTITY(1,1) PRIMARY KEY, 
    FullName VARCHAR(100), 
    City VARCHAR(100), 
    Country VARCHAR(100),
   )

--declare @tmp datetime
--set @tmp = getdate()

INSERT INTO Persons (City,Country,FullName) 
VALUES ('ny', 'usa', 'johnsmith')
EXEC cmn_transaction_stats_sp '2014-07-01','2014-11-05'
"""


sql = """---- starts---


begin try

begin tran

declare @dateof datetime
declare @tmp varchar(500)
declare @var varchar(100)

set @var = ?

set @dateof = getdate()

if exists( select * from INFORMATION_SCHEMA.COLUMNS where table_name = 'MyView5' )
begin

drop view MyView5

end


set @tmp = 'CREATE view MyView5 as
    select *
    from openrowset 
    (
        ''sqloledb'',
        ''server=(local);trusted_connection=yes;'',
        ''exec avnappdb.dbo.' + convert(varchar(50),@var) + ''')'
   
   


exec(@tmp)



declare @SqlTab varchar(500)

declare @tab varchar(50)

declare @drptbl varchar(500)

select @tab = @var + convert(varchar(50), '_out_tbl')

if exists (select * from INFORMATION_SCHEMA.COLUMNS where table_name = @tab)
    begin
    
    select @drptbl = 'drop table ' + @tab 
    exec( @drptbl )
    
    end


SELECT @SqlTab = 'SELECT  * INTO  ' +   @tab + ' FROM    MyView5
alter table ' + @tab + ' add  DHM_Instance_Id bigint, DHM_ID      varchar(40), DHM_company_name  varchar     (20) '
 
Exec(@SqlTab)


-----------next block to remove spaces in column name------------------

declare @sql nvarchar(max)

select @sql = coalesce(@sql, '' ) + '
exec sp_rename ''[' + @tab + '].[' + syscolumns.name + ']'', ''' + replace(syscolumns.name,' ','_') + ''''
from sysobjects, syscolumns
where 
      sysobjects.id = syscolumns.id 
      and sysobjects.id = object_id('[' + @tab + ']')
      and syscolumns.name like '% %'
      
--print @sql

exec (@sql)
--select * from @tab

commit tran

insert into dhm_succ_tbl
(spname, comments, dateof, tablename)
values
(@var,'Success', @dateof, @tab)

end try

begin catch

rollback tran
 insert into dhm_error_tables      
 (spname, errormsg, dateof)      
 values      
 (@var, error_message(), @dateof )   

end catch
    

----------ends-----------


 """



#for item in list:
 #   var = item

c = conn.cursor()

text = open("SpName.txt","r")    
lines = text.read().split(',\n')
#result = [line.split(',\n') for line in text] -- this does same as above, but makes 2D array. why?

i=0

for item in lines:
    print(item)

    # try:
    c.execute(sql, item)   

    # except:
    #     print (item)
    #     logging.exception("Oops:")

    # else:
    #     # i=i+1
        # print(i)
        # print ("times")
    conn.commit()


# item = 'DHMG_MAT_Scrap_11_SP'


# c.execute(sql, item) 
# conn.commit()
conn.close()


for arg in sys.argv:
	abc = '"' + arg + '*"'
	print(abc)



# print (lines)



text.close()


#  begin catch  
 
     
#  insert into dhm_error_tables      
#  (spname, errormsg, dateof)      
#  values      
#  (@var, error_message(), @dateof )   

    
# end catch



