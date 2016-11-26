import datetime
import time

datetime_local = datetime.datetime.now()
print 'datetime_local:',datetime_local

datetime_utc = datetime.datetime.utcnow()
print 'datetime_utc:',datetime_utc

#convert datetime.datetime to string format
print datetime_local.strftime('%Y-%m-%d %H:%M:%S')
print datetime_utc.strftime('%Y-%m-%d %H:%M:%S')

#convert datetime.datetime to time_stamp
#only since python 3
#time_stamp = datetime_local.timestamp()
#print 'time_stamp:',time_stamp

#convert time_stamp to local_datatime
a_datetime_local = datetime.datetime.fromtimestamp(time.time())     
#convert time_stamp to utc_datatime
a_datetime_utc = datetime.datetime.utcfromtimestamp(time.time())  
print(a_datetime_local,a_datetime_utc)

#datetime to struct_time
print(a_datetime_local.timetuple())     
print(a_datetime_utc.utctimetuple())    
