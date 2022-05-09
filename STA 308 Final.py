#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 11:40:42 2022

@author: BaileyBurdick
"""
#%%
#### Importing tidyverse and the data sets

import pandas as pd

state_unemploy_data = pd.read_csv("https://tjfisher19.github.io/data/marchStateUnemployment.csv")
abb_codes_data= pd.read_csv("https://tjfisher19.github.io/data/state_abb_codes.csv")
census_regions_data = pd.read_csv("https://tjfisher19.github.io/data/censusRegions.csv")

#%%
#### Filtering out DC from all the data sets
march_unemploy_50 = state_unemploy_data[state_unemploy_data ['State'] != "District of Columbia"]
abb_codes_50 = abb_codes_data[abb_codes_data ['State'] != "District of Columbia"]
census_regions_50 = census_regions_data[census_regions_data ['State'] != "DC"]

#%%
#### Merging the data sets together into "unemployment_abb"
unemployment_abb = abb_codes_50.merge(
    march_unemploy_50, left_on = "State", right_on = "State")

unemployment_abb_census = unemployment_abb.merge(
    census_regions_50, left_on = "Code", right_on = "State")
#%%
#### Removing the extra state variables - Code and Abbrev
unemployment_abb_census = unemployment_abb_census.loc[:, ['March_21', 'March_22', 'State_x', 'Region']]  

#### Making the variable "Difference", which is March_21 - March_22
unemployment_abb_census ['Difference'] = unemployment_abb_census ['March_21'] - unemployment_abb_census['March_22']
#%%
#### Making the variable mean_unemployment_rates by calculating mean of Difference
mean_unemployment_rates = unemployment_abb_census.groupby('Region')['Difference'].agg('mean')

#%%
#### Making the variable sd_unemployment_rates by subtracting standard deviation of unemployment rates in March 2022 FROM March 2021
sd_unemployment_rates = unemployment_abb_census.groupby('Region')['Difference'].agg('std')


#%%
#### Merging mean_unemployment_rates and sd_unemployment_rates to one data frame
mean_unemployment_rates = mean_unemployment_rates.to_frame()
sd_unemployment_rates = sd_unemployment_rates.to_frame()

mean_std_cv = mean_unemployment_rates.merge(
    sd_unemployment_rates, left_on = "Region", right_on = "Region")

mean_std_cv.rename(columns={'Difference_x': 'Mean', 'Difference_y': 'Standard Deviation'}, inplace=True)

#### Calculating the Coefficient of variation by dividing 
mean_std_cv ['Coefficient of Variation'] = mean_std_cv['Standard Deviation']/mean_std_cv['Mean']

#%%

|           	| Mean 	| Standard Deviation 	| Coefficient of Variation 	|
|-----------	|------	|--------------------	|--------------------------	|
| Midwest   	| 1.34 	| 0.46               	| 0.34                     	|
| Northeast 	| 2.11 	| 0.75               	| 0.35                     	|
| South     	| 1.54 	| 0.49               	| 0.32                     	|
| West      	| 2.15 	| 0.91               	| 0.42                     	|

