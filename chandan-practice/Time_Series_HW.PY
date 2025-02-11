import pandas as pd

df_stocks = pd.read_csv('/home/chandan-nekkanti/Practice/chandan-practice/ts_data.csv')

#Converting to datetimr
df_stocks['DATE'] = pd.to_datetime(df_stocks['DATE'])
df_stocks.set_index('DATE', inplace=True)     
#print(df_stocks.head())

df_stocks['AAPL_7day_SMA'] = df_stocks["AAPL"].rolling(window=7).mean()
#print(df_stocks)


# Calculate the running maximum
h_up = df_stocks['TSLA'].cummax()

# Calculate the drawdown
l_down = df_stocks['TSLA'] / h_up - 1

##Very Important
# Calculate the maximum drawdown
max_drawdown = l_down.min()
print(f"MDD : {max_drawdown:.2%}")

