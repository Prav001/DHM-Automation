#home/charts.py

from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from home.models import Graphs

class chartdata(object):
#...

##below codes from glucose tracker. Replace function with own function which gets total count from graphs 
##and makes dict of count, rundate.
##rinse, repeat for customer and pie-charts, etc
#    @classmethod

	def get_count_wise():
		#data = {'dates': [], 'total_count'=[]}

		data[ 'customer':[], 'dates':[], 'total_count':[] ] = Graphs.objects.values('cust_name','rundate','total_count').order_by('cust_name','rundate')

		print(data)






    # def get_avg_by_day(cls, user, days):
    #     now = datetime.now(tz=user.settings.time_zone).date()


    #     glucose_averages = Glucose.objects.avg_by_day(
    #         (now - timedelta(days=days)), now, user)


    #     data = {'dates': [], 'values': []}
    #     for avg in glucose_averages:
    #         data['dates'].append(avg['record_date'].strftime('%m/%d'))
    #         data['values'].append(core.utils.round_value(avg['avg_value']))


    #     return data
