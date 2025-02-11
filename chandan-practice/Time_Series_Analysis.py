import pandas as pd

ts_data = pd.read_csv('/home/chandan-nekkanti/Practice/chandan-practice/ts_data.csv')

#Converting to datetimr
ts_data['DATE'] = pd.to_datetime(ts_data['DATE'])
ts_data.set_index('DATE', inplace=True)     
#print(ts_data.head())

#emd of month prices
eom_prices = ts_data.resample('M').last()
#print(eom_prices)

daily_retuns = ts_data.pct_change()
#print(daily_retuns.head())

#rolling averages
rolling_avg = ts_data.rolling(window=7).mean()
print(rolling_avg.head(10))

corr = daily_retuns.corr()
#print(corr)