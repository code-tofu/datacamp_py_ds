# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(index="type",values="weekly_sales")

# Print mean_sales_by_type
print(mean_sales_by_type)

# Import NumPy as np
import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales",index="type",aggfunc=[np.mean,np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales",index="type",columns= "is_holiday")

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)



# Index temperatures by city
temperatures_ind = temperatures.set_index("city")
# Reset the index, keeping its contents
print(temperatures_ind.reset_index(drop=False))
# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop=True))
#dropping the contents of the index

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country","city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil","Rio De Janeiro"),("Pakistan","Lahore")]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])
# Specify two country/city pairs to keep (i.e): "Brazil"/"Rio De Janeiro" and "Pakistan"/"Lahore", assigning to rows_to_keep. use rows_to_keep to subset

# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level="city"))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=["country","city"],ascending=[True,False]))

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan":"Russia"])
#note, have to subset srt values

# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc["Lahore":"Moscow"])

# Subset rows from Pakistan, Lahore to Russia, Moscow
# Note the space after comma , in tuple is required?
print(temperatures_srt.loc[("Pakistan", "Lahore"):("Russia", "Moscow")])

# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India", "Hyderabad"): ("Iraq", "Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, "date":"avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[("India", "Hyderabad"): ("Iraq", "Baghdad"),"date":"avg_temp_c"])

# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
# NOT temperatures_bool = temperatures[("date" >= "2010-01-01") & ("date" <= "2011-12-31")]
print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08":"2011-02"])

# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22,1])

# Get the first 5 rows (index positions 0 to 5).
# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])
#up to but not including

#Get all rows, columns 3 and 4 (index positions 2 to 4).
# Use slicing to get columns 3 to 4
print(temperatures.iloc[:,2:4])

#Get the first 5 rows, columns 3 and 4.
# Use slicing in both directions at once
print(temperatures.iloc[:5,2:4])

# Add a year column to temperatures
temperatures["year"] = temperatures["date"].dt.year

#Make a pivot table of the avg_temp_c column, with country and city as rows, and year as columns. Assign to temp_by_country_city_vs_year, and look at the result.
# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c",index=['country', 'city'], columns="year")

# See the result
print(temp_by_country_city_vs_year)

# Subset for Egypt to India
temp_by_country_city_vs_year.loc["Egypt":"India"]

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi")]

# Subset in both directions at once
temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi"),"2005":"2010"]
#note no () for year


# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])
