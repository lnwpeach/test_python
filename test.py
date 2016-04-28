import time
from datetime import datetime, timedelta
FMT_DAY = '%Y-%m-%d'  
date = time.strftime(FMT_DAY)
print(date)
print('%s 08:30:00' % time.strftime(FMT_DAY))
