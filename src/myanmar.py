#Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

#Import Data

def import_dataframe():
    food_df = pd.read_csv('/Users/catherinefuller/galvanize/daimil10/projects/Mid_Term/Myanmar_Food/data/wfp_food_prices_mmr 2.csv')
    return food_df

#Clean Data Frame

def clean_df(df):
    #Remove first row
    first_row_remove_df = df.drop(index=df.index[0], axis=0, inplace=True)

