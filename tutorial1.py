import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates
import sqlalchemy
df=pd.read_csv('C:\\Users\\manish\\OneDrive\\Documents\\weather.csv')
print(df)
print(df.shape)
rows,column=df.shape
print(rows)
print(column)
print(df.head())
print(df.head(3))
print(df.tail())
print(df.tail(1))
print(df[2:5])
print(df[:])
print(df.columns)
print(df.Day)
# df.Day=df['Day']
print(df['Day'])
print(type(df['Day']))
print(df[['Day','event']])
print(df['Temperature'].max())
print(df['Temperature'].mean())
print(df['Temperature'].std())
print(df.describe())
print(df[df.Temperature>43])
print(df[df.Temperature==df.Temperature.max()])
print(df[['event','Day']][df.Temperature==df.Temperature.max()])
print(df.index)
print(df.set_index('Day'))
print(df)
# to change the index of original dataframe we use inplace=true
print(df.set_index('Day',inplace=True))
print(df)
print(df.reset_index(inplace=True))
print(df)
# create dataframe by csv ,excel,python dictionary,tuple
# skipping rows ,we will use skiprows
df1=pd.read_csv('C:\\Users\\manish\\OneDrive\\Documents\\weather.csv',skiprows=1)
print(df1)
df2=pd.read_csv('C:\\Users\\manish\\OneDrive\\Documents\\weather.csv',header=None,names=["date","value","temp","condition"])
print(df2)
# skiprows='' is used for skipping of rows in certain valus;
# nrows= is used for limited rows
# na_values=[""] is used for placing NaN instead of not available ,n.a etc. or cleaning of messy data from csv or excel;
df3=pd.read_csv('C:\\Users\\manish\\OneDrive\\Documents\\company1.csv')
print(df3)
df3=pd.read_csv('C:\\Users\\manish\\OneDrive\\Documents\\company1.csv',nrows=2)
print(df3)
df3=pd.read_csv('C:\\Users\\manish\\OneDrive\\Documents\\company1.csv',na_values=["not available","n.a."])
print(df3)
# na_values by using dictioary
df3=pd.read_csv('C:\\Users\\manish\\OneDrive\\Documents\\company1.csv',na_values={
    'eps':["not available","n.a."],
    'revenue':["not available","n.a.",-1],
'price':["not available","n.a."],
'people':["not available","n.a."],
})
print(df3)
df3.to_csv('new.csv')
# to_csv is used to create a new csv file
# read_excel
# in excel file ,converter is used to change the value of cell ; converters={ 'column name' : function call}
# DataFrame is used for dictionary
# in excel , excelwriter is used for joining two excel sheets with diff name
df4=pd.read_excel('C:\\Users\\manish\\OneDrive\\Documents\\answer.xlsx')
print(df4)
df_stocks= pd.DataFrame({
    'tickers':['googl','wmt','msft'],
    'prices':[321,64,54],
    'pe':[23.23,43.34,4.23],
    'eps':[3,4,4]
})
print(df_stocks)
df_weather=pd.DataFrame({
    'day':['1/2/2019','2/3/2021','2/3/2022'],
    'temp':[23,43,54],
    'event':['rain','sunny','snow']
})
print(df_weather)
with pd.ExcelWriter('stocks_weather.xlsx') as writer:
    df_stocks.to_excel(writer,sheet_name="stocks")
    df_weather.to_excel(writer,sheet_name="weather")

df5=pd.read_excel('stocks_weather.xlsx')
print(df5)
print(df3)
print(df3.fillna(0))
# print(df3.fillna({
#     'eps':0,
#     'revenue':0,
#     'price':0,
# })
# bfill and ffill is used for filling cell vertically
# axis=columns is used for filling cell horizontly
# method=ffill
# limit is used for fill to a certain limit
# interpolate is used for better guess
df6=pd.read_csv('C:\\Users\\manish\\OneDrive\\Documents\\answer.csv')
print(df6)
print(df6.fillna(method="bfill"))
print(df6.fillna(method="bfill",axis="columns"))
# bfill=backward filling
# ffill= forward filling
print(df6.fillna(method="ffill",limit=1))
print(df6.interpolate())
# dropna() method drop all the rows which has "na" in dataframe
print(df6.dropna())
# how="all" is used for not to drop that rows having atlest one data
print(df6.dropna(how="all"))
# thresh=1 is also used for not to drop that rows having atleast one valid value .
print(df6.dropna(thresh=1))
df7=pd.read_csv("C:\\Users\\manish\\Downloads\\report.csv")
print(df7)
print(df7.replace(-9999,np.NaN))
print(df7.replace([-9999,-99999],np.NaN))
# we can use list also in replace method.
# we can use dictionary also in replace method.
print(df7.replace({
    'Temperature': -9999,
    'windspeed': -9999
},np.NaN))
print(df7.replace({
    -9999: np.NaN,
    'no event': 'sunny'
}))
# regex is used for replacing some pattern like any units ex-m/s
# df7.replace('[A-Za-z]','',regex=true)
# using dictionary---
# df7.replace({
#   'Temperature': '[A-Za-z]',
#   'windspeed': '[A-Za-z]'
# },'',regex=true)
df8=pd.DataFrame({
    'score':['poor','good','excellent','average'],
    'student':['rob','maya','sonjana','raj']
})
print(df8)
# replacing list from another list
print(df8.replace(['poor','good','excellent','average'],[3,4,1,2]))
# group by is used for grouping
# syntax -- g=df.groupby(any column name)
# for print g -- for city ,city_df in g:
#                       print(city)
#                        print(city_df)
# other function to display g--- g.get_group(any column data)
# split apply combine means group by ,aggregate function ,combine.
# describe function in group by dataframe gives all important detail such as std,mean,min,max etc.

# concat function is used for join dataframes .
# for continuous indexing , we will use ignore_index=True .
# in merge function , we merge different dataframes
# in merge function , how = left method is used for left join and similarly we can use right join , inner join also
# pivot function is used for reshaping the dataframe and pivot_table function also.
# syntax of pivot function --- pivot(index=  , column=  )
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
rng=pd.date_range(start="12-17-2020",end="12-16-2021",freq='B')
print(rng)
print(Df1.set_index(rng,inplace=True))
print(Df1.close.plot())
# asfreq function uses
print(Df.asfreq('D',method='pad'))
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
usb=CustomBusinessDay(calendar=USFederalHolidayCalendar())
rng=pd.date_range(start="12-17-2020",end="12-16-2021",freq=usb)
print(rng)


































