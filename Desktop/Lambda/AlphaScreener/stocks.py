import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = '8OSSWAF34NN90RZF'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT', interval= '1min', outputsize='full')
# print(data)

i = 1
#while i==1:
#    data, meta_data = ts.get_intraday(symbol='MSFT', interval= '1min', outputsize='full')
#    data.to_excel("output.xlsx")
#    time.sleep(60)#seconds, every minute we should get the info put into excel doc

close_data = data['4. close']
percent_change = close_data.pct_change()
print(percent_change)

last_change = percent_change[-1]
if abs(last_change) > 0.05:
    print('MSFT Alert:' + str(last_change))