import pandas as pd
import numpy as np
import pandas_datareader as web
from datetime import datetime
import statistics

#api_key = 'BRLOYG1FH1HQDSQR'

#Inputs the data from user tickers, start date and end date
user_input =input("Enter the stock tickers(each followed by a coma) : ").upper()
symbols = user_input.split(',')        
#start_date = input("Enter the start date YYYY/MM/DD : ")
#end_date = input("Enter the end date YYYY/MM/DD : ")

stocks_data = {}
#for s in symbols:
#    try:
#        stocks_data[s] = web.DataReader(s, 'av-daily', start = start_date, end = end_date, api_key = api_key)
#    except ValueError as err:
#        print(f"Error fetching data for {s} : {err}")
#ERROR HANDLING OR api REUEST LIMITS

#Create a individual data file for each ticker
#for s, data in stocks_data.items():
#    filename = f'{s}_stock_data.csv'
#    data.to_csv(filename)


# To rename the first column with heading 'Date'
for s in symbols:
    first_row = [row for row in open(f'/home/chandan-nekkanti/Practice/chandan-practice/{s}_stock_data.csv')][0][:4]
    if first_row != 'Date':
        filepath = f'/home/chandan-nekkanti/Practice/chandan-practice/{s}_stock_data.csv'
        new_data = 'Date'
        df = pd.read_csv(filepath)
        with open(filepath, 'r') as file:
            cont =file.read()
        with open(filepath, 'w') as file:
                file.write(new_data + cont)

close_data = pd.DataFrame()

#Adding the date column and setting it as index
dt_one = symbols[0]
dt_file =pd.read_csv(f'/home/chandan-nekkanti/Practice/chandan-practice/{dt_one}_stock_data.csv')
close_data.insert(0,'Date',dt_file['Date'])
close_data.set_index('Date')



#Change the column name and combine them into a single datframe
for s in symbols:
    filepath = f'/home/chandan-nekkanti/Practice/chandan-practice/{s}_stock_data.csv'
    df = pd.read_csv(filepath)
    df.rename(columns={'close':f'{s}_close'}, inplace=True)
    
    close_data = pd.concat([close_data,df[f'{s}_close']],axis = 1)


#print(close_data.head())

for s in symbols:
     close_data[f'{s}_dl_returns'] = close_data[f'{s}_close'].pct_change()*100

for s in symbols:
     close_data[f'{s}_dl_returns'] = close_data[f'{s}_dl_returns'].astype(float)
     


#Handling NULL values, replaced with 0 as all the columns in the dataframe have numeric values(first row is null for daily change)
close_data.fillna("0")


#Calculation of Total Return
tot_returns = 0
for s in symbols:
     start_val = close_data[f'{s}_close'].iloc[0]
     close_val = close_data[f'{s}_close'].iloc[-1]
     returns = (close_val/start_val-1)*100
     tot_returns += returns 
     #print(f'Total return for {s} stock is: {returns:.2f}%')

port_return = tot_returns/len(symbols)     
#print(f'Total portfolio return for the stocks is: {port_return:.2f}%')


#Calculation of Average Daily return
avp_returns = 0
for s in symbols:
     avg_return = close_data[f'{s}_dl_returns'].mean() 
     avp_returns += avg_return
     #print(f'Average daily return for {s} stock is: {avg_return:.2f}%')
Avg_port_returns = avp_returns/len(symbols)     
#print(f'Average daily return for portfolio is: {Avg_port_returns:.2f}%')

#Calculation of Volatility
for s in symbols:
     vol = close_data[f'{s}_dl_returns'].std()
     
     #print(f'Volatlility for {s} stock is: {vol: .2f}')

co_mat = pd.DataFrame()
for s in symbols:
     co_mat[f'{s}_dl_retuns'] = close_data[f'{s}_dl_returns']
print(co_mat.head(4))
matrix = co_mat.corr().to_numpy()

print(matrix[0][1])
print(matrix[0][2])
print(matrix[1][2])
weight = 100/len(symbols)
print(weight)



#print(close_data.head(4))
#print(close_data.columns)

#Calculation of Sharpe Ratio
#rfr = 0.02

#sharpe_ratio = (Avg_port_returns - rfr / len(close_data['Date'])) / std_dev_return

#print(f"Sharpe Ratio of the portolio is: {sharpe_ratio:.2f}")



