import csv
import pandas as pd
import numpy
from fbprophet import Prophet

# Gets all cases in world by country and date.
full_set = pd.read_csv('./data_sets/time_series_covid19_confirmed_US.csv')

# Gets all cases in US by country and date.
us_set = full_set[full_set['iso3'].str.contains("USA")]

# Create Table with Total Cases and Date for US.

# Removes all columns that are not dates.
only_date_cases_us_set = us_set.drop(['UID','iso2','iso3','code3','FIPS','Admin2','Province_State','Country_Region','Lat','Long_','Combined_Key'], axis=1)
# Transforms dataset to have date as first column, with cases as remaining columns.
only_date_cases_us_set = only_date_cases_us_set.T
only_date_cases_us_set = only_date_cases_us_set.sum(1)


# print(only_date_cases_us_set.head())
df = pd.DataFrame(only_date_cases_us_set)
df.to_csv('./modified_us_covid19_confirmed_cases.csv')

df_ds_y = pd.read_csv('./modified_us_covid19_confirmed_cases.csv', names=['ds', 'y'])
print(df_ds_y.head())
df_ds_y = df_ds_y[df_ds_y.y.notnull()]
df_ds_y = df_ds_y[df_ds_y.ds.notnull()]

# print(df)
# df.to_list()
# df.columns = ["y"]

# split_data = df["Capital_State"].str.split(" ")
# data = split_data.to_list()
# names = ["Capital", "State"]

# new_df = pd.DataFrame(data, columns=names)


# df["y"]= df["y"].astype(str) 

# print(df)
# print(df.columns)
# df[['ds']] = df.y.str.split(" ",expand=True,)
# print(df.head())

m = Prophet()
# only_date_cases_us_set.rename(columns={"A": "a", "B": "c"})
m.fit(df_ds_y)
future = m.make_future_dataframe(periods=365)
future.tail()
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
fig1 = m.plot(forecast)
# Create Table with Total Cases and Date by US region/state.