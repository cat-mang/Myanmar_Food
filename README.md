# Myanmar Markets

# Myanmar_Food

Link to data set:
https://www.kaggle.com/datasets/usmanlovescode/myanmar-food-prices-dataset

# Dataset Info
What is the shape of your dataset (rows, columns)?

You are probably looking for a dataset with between 1000 and 500000 rows.

34,196 rows // 14 columns

# Dataset Description
How many categorical fields? What do they represent?
1. date
2. admin1 (ethnic group)
3. admin2 (ethnic group)
4. market (name of market)
5. latitude (of market)
6. longitude (of market)
7. category (commodity category)
8. commodity
9. unit (measurement of commodity)
10. priceflag
11. pricetype
12. currency (MMK - Myanmar Kyat)

How many quantitative? What do they represent?
1. price (in MMK)
2. usdprice (price in USD)

Is there missing data or data that seems to be wrong somehow (e.g. age = -99)?

Some of the units of measurement for the food commodities are in "Days" which does not logically compare against other values such as Kilograms or Liters.

Has the data already been summarized, or are the observations raw and unprocessed?
The food prices from MMK to USD has already been converted.

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

