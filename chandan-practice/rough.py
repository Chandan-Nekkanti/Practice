import pandas as pd
import pandas_datareader as web
from datetime import datetime

api_key = 'BRLOYG1FH1HQDSQR'
start = datetime(2024,3,1)
end = datetime(2024,3,20)

stock_symbols = ['GOOG', 'AAPL']
stock_data = {}


#  insert exception handling
#for s in stock_symbols:
    stock_data[s] = web.DataReader(s,'av-daily', start = start, end = end, api_key = api_key)

#print(stock_data['AAPL'].head())

for symbol,data in stock_data.items():
    filename = f'{symbol}_stock_data.csv'
    data.to_csv(filename)
