import pandas as pd
from fbprophet import Prophet


df = pd.read_csv('./data_sets/time_series_covid19_confirmed_US.csv')
print(df.head())

# TODO: Modify data to use ds - y format. Where y is the number of cases. and ds is datetimestamp.