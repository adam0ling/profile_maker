import pandas as pd
import numpy as np
from profile_maker import genDf

# set up vars
timeDeltas = 60
year = 2019
seasonalityArray = [
    1.1,      # winter
    1,        # spring
    0.9,      # summer
    1         # autumn
]
weekArray = [
    1,        # Monday
    1.05,     # Tuesday
    1.05,     # Wednesday
    1.05,     # Thursday
    1,        # Friday
    0.5,      # Saturday
    0.5       # Sunday
    ]

dayArray = [
    0.9,        # 0
    0.9,        # 1
    0.9,        # 2
    0.9,        # 3
    0.9,        # 4
    1,        # 5
    1,        # 6
    1.02,        # 7
    1.04,        # 8
    1.05,        # 9
    1.07,        # 10
    1.09,        # 11
    1.11,        # 12
    1.09,        # 13
    1.07,        # 14
    1.05,        # 15
    1.03,        # 16
    1.01,        # 17
    1,        # 18
    1,        # 19
    1,        # 20
    0.9,        # 21
    0.9,        # 22
    0.9         # 23
    ]


# gen the df
df = genDf(
    timeDeltas=timeDeltas, 
    year=year, 
    seasonalityArray=seasonalityArray, 
    weekArray=weekArray, 
    dayArray=dayArray
    )

df.to_csv('example.csv', index=False)