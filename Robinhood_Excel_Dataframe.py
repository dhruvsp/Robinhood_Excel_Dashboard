# Install robinhood API Library
pip install robin_stocks

#Required Library
import robin_stocks 
import pandas as pd
import matplotlib.pyplot as plt

#LoggingIn into Robinhood and Enter Authentication number
robin_stocks.login("YourUserID","YourPassword")

#Accessing the Purchased Stock Data
my_stocks = robin_stocks.build_holdings()

#Converting into Dataframe for better Visualization
stock_list = pd.DataFrame(my_stocks)
stock_list = stock_list.T
stock_list['ticker'] = stock_list.index

#DAddine New Row to Calculate total Money Invested
stock_list = stock_list.reset_index(drop=True)
stock_list['quantity'] = stock_list['quantity'].astype(float)
stock_list['average_buy_price'] = stock_list['average_buy_price'].astype(float)
stock_list["total_stock_price"] = stock_list["quantity"]*stock_list["average_buy_price"]
stock_list.loc['Total Money Invested'] = pd.Series(stock_list['total_stock_price'].sum(), index = ['total_stock_price'])

#Dropping unnecessary column
data = pd.DataFrame(dct)  
stock_list.drop(['id','type'], axis=1)

#Invested Money Dataframe
invested_money = stock_list.filter(['name','quantity','average_buy_price', 'total_stock_price'], axis=1)
invested_money.loc['Total_Money_Invested'] = pd.Series(invested_money['total_stock_price'].sum(), index = ['total_stock_price'])

#Current Stock Value Dataframe
current_value = stock_list.filter(['name','quantity','price', 'equity'], axis=1)
current_value['equity'] = current_value['equity'].astype(float) #Converting string into **Float**
current_value.loc['Actual_Value'] = pd.Series(current_value['equity'].sum(), index = ['equity'])

#Calculating Profit and Loss
Profit_Loss = current_value['equity'][:-1].sum() - invested_money['total_stock_price'][:-1].sum()

#Importing Current Date
from datetime import date
dd=date.today()
print(dd)
date=[]
date.append(dd)

#Adding updated Profit/Loss to CSV file
new_row = [date, Profit_Loss] 
from csv import writer
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
        
#Converting Pandas dataframe into CSV File
append_list_as_row('data.csv', new_row)
