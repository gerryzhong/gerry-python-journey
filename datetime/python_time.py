#--encoding=utf8--
import time
import calendar

#get time stamp
time_stamp = time.time()
#1480160098.88

#get local_time:
local_time = time.localtime()
#time.struct_time(tm_year=2016, tm_mon=11, tm_mday=26, tm_hour=19, tm_min=33, tm_sec=37, tm_wday=5, tm_yday=331, tm_isdst=0)

#get utc_time
utc_time = time.gmtime()
#time.struct_time(tm_year=2016, tm_mon=11, tm_mday=26, tm_hour=11, tm_min=34, tm_sec=19, tm_wday=5, tm_yday=331, tm_isdst=0)

#convert between time_stamp,local_time,utc_time
local_time1 = time.localtime(time_stamp)
utc_time1 = time.gmtime(time_stamp)
time_stamp1 = time.mktime(local_time1)
time_stamp2 = calendar.timegm(utc_time1)

#convert different time to string format
#convert time_stamp to string
print time.ctime(time_stamp)

# convert local_time to string
print(time.asctime(local_time))    
# convert utc_time to string
print(time.asctime(utc_time))     


# convert local_time to customized string format 
print(time.strftime("%Y-%m-%d, %H:%M:%S, %w", local_time))
# convert utc_time to customized string format 
print(time.strftime("%Y-%m-%d, %H:%M:%S, %w", utc_time))

#parse string format to struct_time
struct_time = time.strptime("2016-11-15, 15:32:12, 2", "%Y-%m-%d, %H:%M:%S, %w") 


