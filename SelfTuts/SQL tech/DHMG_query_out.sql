--shivalik sen stored procedure to take list of SPs and get their output in respective tables 
--24/11/14

CREATE procedure DHMG_query_out 
as
begin


declare @sp_name varchar (100)

declare @dateof datetime

select @dateof = getdate()


While (Select Count(*) From DHMTable Where Processed = 0) > 0
Begin


   Select Top 1 @sp_name = spname From DHMTable Where Processed = 0

   
    
    select 'sent and updated', 'spname', @sp_name, 'date', @dateof
    
    exec sp_table_maker @sp_name  -- this procedure does the main work
    
    
    Update DHMTable Set Processed = 1 Where spname = @sp_name 

End --while loop ends

end

