import csv
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
import numpy
import pandas as pd
import plotly.offline as py
import requests

# Gets all cases in US for current date.
# Uses most up to date data.
full_set = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv")


# Create Table with Total Cases and Date for US.

# Removes all columns that are not dates.
only_date_cases_us_set = us_set.drop(['UID','iso2','iso3','code3','FIPS','Admin2','Province_State','Country_Region','Lat','Long_','Combined_Key'], axis=1)
# Transforms dataset to have date as first column, with cases as remaining columns.
only_date_cases_us_set = only_date_cases_us_set.T
only_date_cases_us_set = only_date_cases_us_set.sum(1)

# Re-writes modified dataset so it can be used by FBProphet.
df = pd.DataFrame(only_date_cases_us_set)
df.to_csv('./modified_us_covid19_confirmed_cases.csv')

df_ds_y = pd.read_csv('./modified_us_covid19_confirmed_cases.csv', names=['ds', 'y'])
df_ds_y = df_ds_y[df_ds_y.y.notnull()]
df_ds_y = df_ds_y[df_ds_y.ds.notnull()]

m = Prophet()
m.fit(df_ds_y)

# 30 Day prediction.
future = m.make_future_dataframe(periods=30)
future.tail()
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
fig1 = m.plot(forecast, xlabel='Date', ylabel='Number of Covid Cases (1000000)')
ax = fig1.gca()
ax.set_title("30 Day US Covid Cases Forecast", size=34)
ax.set_xlabel("Date (Year-Month-Day)", size=25)
ax.set_ylabel("Cases (1,000,000)", size=25)
ax.tick_params(axis="x", labelsize=24)
ax.tick_params(axis="y", labelsize=24)

# TODO: Print out today's date.
# TODO: Print out today's forecasted cases.
# TODO: Print out actual cases per CDC/WHO tracker.