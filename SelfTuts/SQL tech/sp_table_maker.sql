--shivalik sen - This takes SP name and executes it, creates view based on O/P & creates out_table based on this view.
-- 24/11/14
CREATE procedure sp_magic @var varchar(100)
as
begin


---- starts---


	begin try

	begin tran

		declare @dateof datetime
		declare @tmp varchar(500)
		--declare @var varchar(100)

		--set @var = 

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

		-----------Now the table making magic happens------------------

		declare @SqlTab varchar(500)

		declare @tab varchar(50)

		declare @drptbl varchar(500)

		select @tab = @var + convert(varchar(50), '_out_tbl_24Nov')

		if exists (select * from INFORMATION_SCHEMA.COLUMNS where table_name = @tab)
			begin
		    
			select @drptbl = 'drop table ' + @tab 
			exec( @drptbl )
		    
			end


		SELECT @SqlTab = 'SELECT  * INTO  ' +   @tab + ' FROM    MyView5
		alter table ' + @tab + ' add  DHM_Instance_Id bigint, DHM_ID      varchar(40), DHM_company_name  varchar     (20) '
		 
		Exec(@SqlTab)


		-----------More magic to remove spaces in column name------------------

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

end