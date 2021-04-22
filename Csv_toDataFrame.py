# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 13:36:47 2018

@author: WakeSurfin1

@ use Tate Gallery data set from GitHub
https://github.com/tategallery/collection

"""

import pandas as pd
import matplotlib.pyplot as plt

## read first 5 lines of csv file into pandas data frame
## use Spyder variable explorer to view results
## df = pd.read_csv("C:/Data/artwork_data.csv", nrows=5)

## create a list of columns to use from the csv file
COLS_TO_USE = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear',
               'height', 'width', 'units']

## create Pandas dataframe from the csv files using the columns in the list
## and identify the index column
df = pd.read_csv("C:/Data/artwork_data.csv",
                 usecols=COLS_TO_USE, index_col='id',
                 low_memory=False)

## use the artist field as an index to create a series
## get count of unique/distinct artists in the series
artists = df['artist']
CntDistinctArtists = len(pd.unique(artists))

## reuse the artists series from above
## count the number of records with artist == 'Bacon, Francis'
artist_cnt = artists.value_counts()
cntBacon = artist_cnt['Bacon, Francis']

## demo loc versus iloc indexing
## loc works on lables
## iloc works on position
strArtists1 = df.loc[1035, 'artist']
strArtists2 = df.iloc[0, 0]
SeriesSliceArtists = df.iloc[0:2, 0]

## group by artist get the minimum acquisition year for each artist
for artist, group_df in df.groupby('artist'):
    min_year = group_df['acquisitionYear'].min()
    
## group by acquisition year, count records per ac year
SeriesAcquistYears = df.groupby('acquisitionYear').size() 

## output to a simple graph   
SeriesAcquistYears.plot()
plt.show()