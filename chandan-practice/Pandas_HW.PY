import pandas as pd

data = {

 'Asset': ['Bonds', 'Stocks', 'Real Estate', 'Commodities'],

 'Quantity': [120, 80, 50, 70],

'Market Value': [1200.00, 2400.50, 3000.00, 950.00]  # Values in USD

}

df_assets = pd.DataFrame(data)

#print(df_assets)
dat_mv = df_assets[['Asset','Market Value']]
#print(dat_mv)

#Q5
ser = pd.Series(df_assets['Market Value']*df_assets['Quantity'])
print(ser)

#print(df_assets[df_assets['Market Value'] > 1000])

#df_assets.loc[df_assets['Asset'] == 'Commodities', 'Market Value'] = 1025.0
#print(df_assets)
df_assets['Total_Market_Value'] = df_assets['Market Value']*df_assets['Quantity']

print(df_assets.sort_values(by='Total_Market_Value',ascending=False))


