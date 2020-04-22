[Forecasting Global Covid-19 with Kaggle Dataset](https://www.kaggle.com/c/covid19-global-forecasting-week-4)

Using FacebookProphet forecasting tooling and python, this is an attempt to forecast global covid 19 spread. Specifically, forecast confirmed cases and fatalities between April 15 - May 14 2020  by region.

Implemented with Python 3.7.4, FacebookProphet, and (external database)[data-sources].

## Run Locally
1. `pip install -r requirements.txt`
1. `python src/covid_forecaster.py`


## Run in Docker Locally
1. docker build .
1. docker run -i <name of image created above>


# Data Sources
## Time Series Summary of Covid
Daily time series summary tables, including confirmed, deaths and recovered. All data are from the daily case report ([Source](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series)).

# Run with Jupyter Notebook
1. `pip install -r requirements.txt`
1. `jupyter notebook ./src/US_Covid_19_Cases_Forecast.ipynb`

### US Cases 30 Day Forecast
![Alt text](covid_us_cases_30_day_forecast.png?raw=true "Title")
![US Cases 30 Day Forecast]('covid_us_cases_30_day_forecast.png')