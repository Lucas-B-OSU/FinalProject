
def classify_aqi(aqi): # Classifying the AQI values in the dataset with the Air Quality Index Scale
  if 0 <= aqi <= 50:
    return 'Good'

  elif 51 <= aqi <= 100: 
    return 'Moderate'

  elif 101 <= aqi <= 150: 
    return 'Unhealthy for sensitive'

  elif 151 <= aqi <= 200:
    return 'Unhealthy'

  elif 201 <= aqi <= 300: 
    return 'Very Unhealthy'

  elif 301 <= aqi <= 500: 
    return 'Hazardous'

  else: 
    return 'Invalid'

def print_yearly_aqi_trend(dataset, pollutant): #defining function to analysis the yearly trend for specific pollutnat
    nonzero_dataset = dataset[dataset[f'{pollutant} AQI'] > 0].copy()
    nonzero_dataset['Year'] = nonzero_dataset['Date'].dt.year 

    yearly_avg = nonzero_dataset.groupby('Year')[f'{pollutant} AQI'].mean().dropna() #groups by year and calcs average aqi by year
    year_counts = nonzero_dataset['Year'].value_counts()
    valid_years = year_counts[year_counts > 50].index # only keeps years with more than 50 records for more accurate data
    yearly_avg = yearly_avg.loc[yearly_avg.index.isin(valid_years)]

    if len(yearly_avg) < 2: # making sure there is enough data to show a trend
        print("Not enough valid data for yearly trend analysis.")
        return

    first_year = yearly_avg.index.min() #gets first and last year and their AQI Averages
    last_year = yearly_avg.index.max()
    first_avg = yearly_avg.loc[first_year]
    last_avg = yearly_avg.loc[last_year]

    
    print(f"Yearly AQI Trend for {pollutant}") #print statement comparison
    print("------------------------------------------------------")
    print(f"Average AQI in {first_year}: {round(first_avg, 2)}")
    print(f"Average AQI in {last_year}: {round(last_avg, 2)}")

    if first_avg > 0: #calcs percentage chnage over time 
        percent_change = ((last_avg - first_avg) / first_avg) * 100
        direction = "increased" if percent_change > 0 else "decreased"
        print(f"{pollutant} AQI has {direction} by {round(abs(percent_change), 2)}% from {first_year} to {last_year}")
    else:
        print("Cannot calculate percentage change due to 0 starting average.")
    print("------------------------------------------------------")



