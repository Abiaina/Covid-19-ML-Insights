[Forecasting Global Covid-19 with Kaggle Dataset](https://www.kaggle.com/c/covid19-global-forecasting-week-4)

Using FacebookProphet forecasting tooling and python, this is an attempt to forecast global covid 19 spread. Specifically, forecast confirmed cases and fatalities between April 15 - May 14 2020  by region.

Implemented with Python 3.7.4, FacebookProphet, and (external database)[data-sources].
** Note: Graph only visible when run with Jupyter Notebook. **

## Run Locally
1. `pip install -r requirements.txt`
1. `python src/covid_forecaster.py`


## Run in Docker Locally
1. docker build .
1. docker run -i <name of image created above>

# Run with Jupyter Notebook
Graph will print out in the notebook.
1. `pip install -r requirements.txt`
1. `jupyter notebook ./src/US_Covid_19_Cases_Forecast.ipynb`

# Data Sources
## Time Series Summary of Covid
Daily time series summary tables, including confirmed, deaths and recovered. All data are from the daily case report ([Source](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series)).

# Forecast Graphs
## US Cases 30 Day Forecast
#### Forecast with data until May 12 2020
![US Cases 30 Day Forecast](./static_images/covid_us_cases_30_day_forecast_5_12_2020.png?raw=true "US Cases 30 Day Forecast")

#### Forecast with data until April 2020
![US Cases 30 Day Forecast](./static_images/covid_us_cases_30_day_forecast.png?raw=true "US Cases 30 Day Forecast")
