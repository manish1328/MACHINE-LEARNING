import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates
import sqlalchemy
Df=pd.read_csv("C:\\Users\\manish\\Downloads\\AAPL.csv",parse_dates=["Date"],index_col="Date")

print(Df.head(3))
print(Df["12-2020"])
print(Df["12-2020"].Close.mean())
print(Df["17-12-2020":"01-01-2021"])
# resample is used for also find monthly , quartly etc.
print(Df.Close.resample('M').mean())
print(Df.Close.resample('Q').mean())
print(Df.Close.resample('Q').mean().plot())
Df1=pd.read_csv("C:\\Users\\manish\\Downloads\\AAPL11.csv")
print(Df1.head(6))
# rng1=pd.date_range(start="12-17-2020",end="12-16-2021",freq='B')
# print(rng1)
# print(Df1.set_index(rng1,inplace=True))
print(Df1.close.plot())
# asfreq function uses
print(Df.asfreq('D',method='pad'))
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
usb=CustomBusinessDay(calendar=USFederalHolidayCalendar())
rng=pd.date_range(start="12-17-2020",end="12-16-2021",freq=usb)
print(rng)
# creating own custom calendar
from pandas.tseries.holiday import AbstractHolidayCalendar,nearest_workday,Holiday
class mybirthdayCalendar (AbstractHolidayCalendar) :
    rules=[
        Holiday('Manish Birth Day',month=4,day=15)
    ]
my=CustomBusinessDay(calendar=mybirthdayCalendar())
print(pd.date_range(start="4-1-2012", end="4-20-2012",freq=my))
# in egypt , weekend is friday and sunday .
# weekmask used in custombusiness day.
b=CustomBusinessDay(weekmask='Sun Mon Tue Wed Thu')
print(pd.date_range(start="4-1-2012", end="4-20-2012",freq=b))
dates=['2017-01-05 2:30 PM','2017-01-07 2:00PM','2017-01-08']
print(pd.to_datetime(dates))
# epoch or unix time is number of seconds that have passed since Jan 1,1970 UTC
t=1639810931
print(pd.to_datetime(t,unit='s'))
y=pd.Period('2020')
print(y)
print(y.start_time)
m=pd.Period('2020-1',freq='M')





