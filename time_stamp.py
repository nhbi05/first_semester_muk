import datetime
current_time_stamp= datetime.datetime.now().timestamp()#from jan 1st 1970
print(current_time_stamp)#prints block numbers with barely a meaning so we need to create a date time object from future time stamp
future_time= current_time_stamp + 10000000
dto = datetime.datetime.fromtimestamp(future_time)
print (dto)
#\n - formatting charracter for a new line
#\ - continuation character- shows that code is continuauos
# docstrings (documentation )