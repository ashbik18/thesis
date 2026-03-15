#importing necessaey libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_collected = pd.read_csv('C:\\Users\\Bikas Pc\\Desktop\\env data\\merged_data.csv') #collected data
df_website = pd.read_csv('C:\\Users\\Bikas Pc\\Desktop\env data\\export.csv') #website data

# Clean column names by stripping spaces
df_collected.columns = df_collected.columns.str.strip()
df_website.columns = df_website.columns.str.strip()
# Convert 'Datetime' column to datetime format
df_collected['Datetime'] = pd.to_datetime(df_collected['Datetime'], errors='coerce') 
#Convert to datetime, any errors will be coerced to NaT
# Convert 'time' column to datetime format in the website data
df_website['time'] = pd.to_datetime(df_website['time'], errors='coerce')
# Merge the datasets on 'Datetime' and 'time', applying suffixes to distinguish columns
merged_data = pd.merge(df_collected[['Temperature(C)', 'Humidity(%)', 'Datetime']],
df_website[['temp', 'rhum', 'time']],
left_on='Datetime', right_on='time',
suffixes=('_collected', '_website'))

print("Merged Data Columns:")
print(merged_data.columns) # Check the column names after merging



#discriptive statistics
desc_collected_temp = df_collected['Temperature(C)'].describe()
desc_website_temp = df_website['temp'].describe()
desc_collected_humidity = df_collected['Humidity(%)'].describe()
desc_website_humidity = df_website['rhum'].describe()
print("Descriptive Statistics for Collected Temperature:")
print(desc_collected_temp)
print("\nDescriptive Statistics for Website Temperature:")
print(desc_website_temp)
print("\nDescriptive Statistics for Collected Humidity:")
print(desc_collected_humidity)
print("\nDescriptive Statistics for Website Humidity:")
print(desc_website_humidity)
# ---------------------------------------
# Visualize Temperature and Humidity Comparison
# ---------------------------------------
# Plot Temperature comparison
plt.figure(figsize=(14, 7))
plt.plot(merged_data['Datetime'], merged_data['Temperature(C)'], label='Collected Temperature', color='tab:blue')
plt.plot(merged_data['Datetime'], merged_data['temp'], label='Website Temperature',
color='tab:orange', linestyle='--')
plt.title('Temperature Comparison (Collected vs Website)', fontsize=16)
plt.xlabel('Datetime', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Plot Humidity comparison
plt.figure(figsize=(14, 7))

plt.plot(merged_data['Datetime'], merged_data['Humidity(%)'], label='Collected Humidity', color='tab:green')
plt.plot(merged_data['Datetime'], merged_data['rhum'], label='Website Humidity',
color='tab:red', linestyle='--')
plt.title('Humidity Comparison (Collected vs Website)', fontsize=16)
plt.xlabel('Datetime', fontsize=12)
plt.ylabel('Humidity (%)', fontsize=12)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# ---------------------------------------
# Calculate Correlation between Datasets
# ---------------------------------------

# Calculate correlation for Temperature
temperature_corr = merged_data['Temperature(C)'].corr(merged_data['temp'])
print(f"Correlation between collected and website Temperature: {temperature_corr}")
# Calculate correlation for Humidity
humidity_corr = merged_data['Humidity(%)'].corr(merged_data['rhum'])
print(f"Correlation between collected and website Humidity: {humidity_corr}")
# Create a correlation matrix between relevant variables
correlation_matrix = merged_data[['Temperature(C)', 'Humidity(%)', 'temp',
'rhum']].corr()
# Print the correlation matrix to see the values
print("Correlation Matrix:")
print(correlation_matrix)
# Plot the correlation heatmap using seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f',
linewidths=0.5, vmin=-1, vmax=1)
plt.title('Correlation Heatmap for Temperature and Humidity (Collected vs Website)',
fontsize=16)
plt.show()
# ---------------------------------------
# Anomalies
# Calculate Moving Average (7-day window)
# ---------------------------------------
merged_data['Temperature_MA'] = merged_data['Temperature(C)'].rolling(window=7).mean()
merged_data['Humidity_MA'] = merged_data['Humidity(%)'].rolling(window=7).mean()
# Calculate Z-scores for anomalies
merged_data['Temp_Zscore'] = (merged_data['Temperature(C)'] - merged_data['Temperature(C)'].mean()) / merged_data['Temperature(C)'].std()
merged_data['Humidity_Zscore'] = (merged_data['Humidity(%)'] - merged_data['Humidity(%)'].mean()) / merged_data['Humidity(%)'].std()
# Detect anomalies based on Z-score (threshold of 2 or 3)
merged_data['Temp_Anomaly'] = merged_data['Temp_Zscore'].apply(lambda x:'Anomaly' if abs(x) > 2 else 'Normal')
merged_data['Humidity_Anomaly'] = merged_data['Humidity_Zscore'].apply(lambda x: 'Anomaly' if abs(x) > 2 else 'Normal')
# ---------------------------------------
# Visualize Anomalies
# ---------------------------------------
# Plot Temperature comparison
plt.figure(figsize=(14, 7))
plt.plot(merged_data['Datetime'], merged_data['Temperature(C)'], label='Temperature')
plt.plot(merged_data['Datetime'], merged_data['Temperature_MA'], label='7-Day Moving Average', linestyle='--', color='red')
plt.scatter(merged_data['Datetime'][merged_data['Temp_Anomaly'] == 'Anomaly'],
merged_data['Temperature(C)'][merged_data['Temp_Anomaly'] == 'Anomaly'],
color='black', label='Anomalies', zorder=5)
plt.title('Temperature Anomalies Detection', fontsize=16)
plt.xlabel('Datetime', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Similarly, you can plot for Humidity
plt.figure(figsize=(14, 7))
plt.plot(merged_data['Datetime'], merged_data['Humidity(%)'], label='Humidity')
plt.plot(merged_data['Datetime'], merged_data['Humidity_MA'], label='7-Day Moving Average', linestyle='--', color='red')
plt.scatter(merged_data['Datetime'][merged_data['Humidity_Anomaly'] == 'Anomaly'],
merged_data['Humidity(%)'][merged_data['Humidity_Anomaly'] == 'Anomaly'],
color='black', label='Anomalies', zorder=5)
plt.title('Humidity Anomalies Detection', fontsize=16)
plt.xlabel('Datetime', fontsize=12)
plt.ylabel('Humidity (%)', fontsize=12)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#impact analysis
         
# Define thresholds for temperature and humidity
temp_threshold_high = 30 # High temperature threshold (°C)
humidity_threshold_high = 60 # High humidity threshold (%)
# Flag the periods where these thresholds are exceeded
merged_data['High_Temperature'] = merged_data['Temperature(C)'].apply(lambda x:
'Yes' if x > temp_threshold_high else 'No')
merged_data['High_Humidity'] = merged_data['Humidity(%)'].apply(lambda x: 'Yes' if
x > humidity_threshold_high else 'No')
# Count the number of instances where these thresholds are exceeded
high_temp_events = merged_data[merged_data['High_Temperature'] == 'Yes']
high_humidity_events = merged_data[merged_data['High_Humidity'] == 'Yes']
# Print the number of events where high temperature and humidity occurred
print(f"Number of High Temperature Events (> {temp_threshold_high}°C):{len(high_temp_events)}")
print(f"Number of High Humidity Events (> {humidity_threshold_high}%):{len(high_humidity_events)}")
# Visualize the periods with high temperature and humidity
plt.figure(figsize=(14, 7))
plt.plot(merged_data['Datetime'], merged_data['Temperature(C)'], label='Temperature')
plt.fill_between(merged_data['Datetime'], merged_data['Temperature(C)'],
temp_threshold_high,
where=(merged_data['Temperature(C)'] > temp_threshold_high),
color='orange', alpha=0.3, label='High Temp')
plt.title('High Temperature Events', fontsize=16)
plt.xlabel('Datetime', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Similarly, visualize high humidity
plt.figure(figsize=(14, 7))
plt.plot(merged_data['Datetime'], merged_data['Humidity(%)'], label='Humidity')
plt.fill_between(merged_data['Datetime'], merged_data['Humidity(%)'],
humidity_threshold_high,
where=(merged_data['Humidity(%)'] > humidity_threshold_high),
color='blue', alpha=0.3, label='High Humidity')
plt.title('High Humidity Events', fontsize=16)
plt.xlabel('Datetime', fontsize=12)
plt.ylabel('Humidity (%)', fontsize=12)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
