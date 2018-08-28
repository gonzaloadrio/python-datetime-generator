from datetime import datetime, time
import pandas as pd

datetime_start = datetime(year=2018, month=1, day=1, hour=8)
datetime_end = datetime(year=2018, month=2, day=1, hour=16)
time_start = time(hour=14, minute=30)
time_end = time(hour=15, minute=45)
days_of_week = [0, 2, 3]

dates = pd.date_range(datetime_start, datetime_end, freq='S')

dft = pd.DataFrame({'dates': dates})

dft['day_of_week'] = dft['dates'].dt.weekday
dft['time'] = dft['dates'].dt.time

dft = dft[(dft['day_of_week'].isin(days_of_week)) & (time_start < dft['time']) & (dft['time'] < time_end)]

print(dft)
