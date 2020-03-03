import pandas as pd
import numpy as np
import datetime

# generate years worth df
def genDf(
    timeDeltas=60, 
    year=(datetime.datetime.now().year - 1),
    seasonalityArray = [1, 1, 1, 1],
    weekArray = [1, 1, 1, 1, 1, 1, 1],
    dayArray = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ):    
    '''
    timeDeltas - time incriments in minutes, default 60mins
    year - which year to use for dataframe, default last year
    seasonalityArray - array to set weights to different seasons, order = Winter, Spring, Summer, Autumn. default [1, 1, 1, 1]
    weekArray - array to set weights for weekdays, default [1, 1, 1, 1, 1, 1, 1],
    dayArray - array to set wieghts for hours, default [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    '''
    sdate = datetime.datetime(year, 1, 1, 0, 0)   # start date
    edate = datetime.datetime(year+1, 1, 1, 0, 0)  # end date

    currentDate = sdate
    dates = []
    dates.append(currentDate)
    while currentDate < edate:  # generate needed dates
        currentDate += datetime.timedelta(minutes=timeDeltas)
        dates.append(currentDate)

    seasonsDf = pd.DataFrame()
    seasonsDf['Month'] = [i for i in range(1, 13)]
    seasonsDf['Season'] = 'Winter'
    for i in range(len(seasonsDf)):
        if seasonsDf.iloc[i, 0] in [3, 4, 5]:
            seasonsDf.iloc[i,1] = 'Spring'
        elif seasonsDf.iloc[i, 0] in [6, 7, 8]:
            seasonsDf.iloc[i,1] = 'Summer'
        elif seasonsDf.iloc[i, 0] in [9, 10, 11]:
            seasonsDf.iloc[i,1] = 'Autumn'   

    df = pd.DataFrame()  # dataframe used
    df['Time'] = dates  # dates
    df['Month'] = [i.month for i in df['Time']]  # months
    df = df.merge(seasonsDf, on='Month')  # seasons
    df['Weekday'] = [i.weekday() for i in df['Time']]  # weekdays
    df['Hour'] = [i.hour for i in df['Time']]  # hours

    df['Consumption'] = 1

    # seasonality multiplier
    seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
    for i in range(len(seasons)):
       df.loc[df['Season']==seasons[i], 'Consumption'] = seasonalityArray[i]

    consumptionSum = df['Consumption'].sum()
    df['Consumption'] = df['Consumption']/consumptionSum  # reweight consumption

    # weekday multiplier
    weekdays = [i for i in range(7)]
    for i in range(len(weekdays)):
       df.loc[df['Weekday']==weekdays[i], 'Consumption'] = weekArray[i]

    consumptionSum = df['Consumption'].sum()
    df['Consumption'] = df['Consumption']/consumptionSum  # reweight consumption

    # hour multiplier
    hours = [i for i in range(24)]
    for i in range(len(hours)):
       df.loc[df['Hour']==hours[i], 'Consumption'] = dayArray[i]

    consumptionSum = df['Consumption'].sum()
    df['Consumption'] = df['Consumption']/consumptionSum  # reweight consumption

    dfA = df[['Time','Consumption']]

    return(dfA)
