import time
FMT_DAY = '%Y-%m-%d'  
FMT_TIME = '%H:%M:%S'
date = time.strftime(FMT_DAY)
time = time.strftime(FMT_TIME)
print('date : ',date)
print ('time : ',time)
print ('date time : ',date,time)
