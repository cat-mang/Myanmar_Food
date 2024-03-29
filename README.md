# Myanmar Markets

## Project Proposal
When I worked in Thailand in 2021, much of our focus was on Thailand's western border with Myanmar (Burma). A coup occurred in Myanmar in February 2021 and the military junta was conducting kinetic operations against Myanmar's ethnic armed groups (EAG). A humanitarian crisis followed. 
Historically, many ethnic groups in Myanmar have been subjected to oppression. Myanmar has been a very politically unstable country for years. Though currently there are no Special Operations Forces deployed to Myanmar, I wanted to use Myanmar as case study to determine where SOF might employ tactical Civil Affairs Teams in a semi/non-permissive operational environment to maximize results. 
Therefore, by analyzing historical commodity prices in Myanmar, I aimed to find the top volatile markets in Myanmar as a way to identify subregions that had highly vulnerable populations. A Civil Affairs Team could then narrowly focus operations in the vacinity of that area.


## Data Set Info and Description
The data set was provided by the World Food Programme (WFP).

The data set had 34,196 rows and 14 columns. 

Link to data set:
https://www.kaggle.com/datasets/usmanlovescode/myanmar-food-prices-dataset

The data set had 12 categorical fields:
1. date
2. admin1 (State/Region)
3. admin2 (Sub Region)
4. market (name of market)
5. latitude (of market)
6. longitude (of market)
7. category (commodity category)
8. commodity
9. unit (measurement of commodity)
10. priceflag
11. pricetype
12. currency (MMK - Myanmar Kyat)

The date set had 2 quantitative fields:
1. price (in MMK)
2. usdprice (price in USD)

Data Cleaning
The data was relatively straightforward and error free. Data cleaning involved changing the Dtype of several columns since all columns were "objects at first". Luckily, the commodity price conversions from MMK to USD was provided.

# Potential Avenues of Inquiry
Initial data exploration often sparks additional questions or potential insights that could be supported by continued exploration.

What types of questions does this dataset seem to support?

Be especially on the lookout for avenues of inquiry that produce a tangible value (the ability to make better targeted or informed decisions, or some other potential benefit to stakeholders).

This data set would support policymakers' and NGOs' analysis on where to invest more resources in Myanmar during periods of instability. This data can also predict which commodities are most in demand and where.

# Question
Where in Myanmar are markets most vulnerable to food price surges during periods of instability? 


# Minimum Viable Product
3 x graphs which depict:
1. Food prices surge during periods of instability in Myanmar
2. Top 3 commodities most impacted by instability (price change delta)
3. Top 3 markets most impacted by instability (price change delta)

# MVP +
1. Graph all commodity prices on one graph
2. Graph location on map of market locations

# Methodology 

After data cleaning, I noticed that the data was only collected on the 15th of every month. 

# Find key dates when commodity prices are highest
Clean the data to easily read date (month/year) format
You will need multiple graphs to depict average prices of different commodities:
1. Fuel (diesel)
2. Oil (palm)
3. Meat (pork)
4. Rice (high quality)
5. Rice (low quality)
6. Onions
Group by the date to find average food prices during the month/year

# Find which commodities are most vulnerable to price surges
Group by commodity to find average food prices ranging from high priced times to stable times
Possibly a histogram?
Time Correlation?

Diesel Fuel

# Determine which markets are most impacted by rising food prices
Heat map? for correlation?


# Data Frames Created
food_df: OG data frame

fuel_df: Only commodity column is diesel fuel
oil_df: Only commodity column is palm oil
meat_df: Only commodity column is pork meat
onions_df: Only commodity column is onions
riceLQ_df: Only commodity column is low quality rice

Commodity over time
fuel_over_time: fuel_df grouped by date
oil_over_time: oil_df grouped by date
meat_over_time: meat_df grouped by date
onions_over_time: onions_df grouped by date
rice_over_time: riceLQ_df grouped by date

Commodity 2008 - 2012
rice_volatile
fuel_volatile
oil_volatile
meat_volatile
onions_volatile 


Commodity 2020 - 2023
rice_coup_df
oil_coup_df
onions_coup_df
meat_coup_df

Market Analysis
markets_df = OG dataframe for markets
top_marks = only markets with 100 or more data points

top_rice_markets
high_oil
high_fuel
high_rice

