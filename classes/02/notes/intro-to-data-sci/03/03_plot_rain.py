import numpy as np
import pandas
import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, let's
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.

    Let's plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()

    Your histogram may look similar to bar graph in the instructor notes below.

    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms

    You can see the information contained within the turnstile weather data here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''

    plt.hold(True)
    plt.figure()
    df = turnstile_weather[['rain', 'ENTRIESn_hourly']]
    df_r = df[(df['rain'] == 1) & (df['ENTRIESn_hourly'] < 6000)]
    df_n = df[(df['rain'] == 0) & (df['ENTRIESn_hourly'] < 6000)]
    df_n['ENTRIESn_hourly'].hist(label='No rain', alpha=0.5)
    df_r['ENTRIESn_hourly'].hist(label='Rain', alpha=0.5)
    plt.legend(loc='upper right')
    return plt
