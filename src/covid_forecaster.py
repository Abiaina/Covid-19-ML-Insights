import csv
import pandas as pd
import numpy
from fbprophet import Prophet


df = pd.read_csv('./data_sets/time_series_covid19_confirmed_US.csv')
wa_set = df.pivot_table(values="value", index="iso2", columns="parameter")
print(wa_set.head())
# print(wa_set.head())

# TODO: Modify data to use ds - y format. Where y is the number of cases. and ds is datetimestamp.
# raw_data = open('./data_sets/time_series_covid19_confirmed_US.csv', 'rt')
# reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
# x = list(reader)
# data = numpy.array(x)
# print(data.shape)