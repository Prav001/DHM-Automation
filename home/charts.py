#home/charts.py
from __future__ import print_function, division, absolute_import, unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
import time
from home.models import Graphs
from operator import attrgetter

class chartdata():
#...
   	
	@classmethod

	def get_cust_wise(self):

		
		
		data = Graphs.objects.all()
		
		cust = []

		for i in data:
			cust.append(i.cust_name)
		
		print(cust)


		return cust


	@classmethod	


	def get_date_wise(self):

		
		data = Graphs.objects.all()
		data=sorted(data, key=attrgetter('rundate'))
		
		date = []

		for i in data:
			temp = i.rundate
			#tmp = strftime("%d, %b, %Y",temp)
			date.append(temp)
		
		#print(date)
		return date


	@classmethod	

	def get_count_wise(self):

	
		
		data = Graphs.objects.all()
		
		ct = []

		for i in data:
			ct.append(i.total_count)
		
		print(ct)
	

		return ct	

	@classmethod	
	def get_air_wise(self):

		data = Graphs.objects.all()
		
		ct = []

		for i in data:
			if(i.cust_name=='Air India'):
				ct.append(i.total_count)
		
		print(ct)
	

		return ct

	@classmethod
	def get_aero_wise(self):

		data = Graphs.objects.all()
		
		ct = []

		for i in data:
			if(i.cust_name=='Aerogulf'):
				ct.append(i.total_count)
		
		print(ct)
	

		return ct	
		

