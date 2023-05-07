import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Replace this line with the actual file path if needed
df = pd.read_csv('timed.csv')

# Convert 'Date' column to pandas datetime format
df['Date'] = pd.to_datetime(df['Date'])


# Group the data by month and calculate the total time worked per day (in hours)
df['total_seconds'] = pd.to_timedelta(df['Time']).dt.total_seconds()
daily_total_seconds = df.groupby(['Date'])['total_seconds'].sum()
daily_total_hours = daily_total_seconds / 3600

# Split the data into October-March and the rest of the year
oct_mar = daily_total_hours[(daily_total_hours.index.month >= 10) | (daily_total_hours.index.month <= 3)]
apr_sep = daily_total_hours[(daily_total_hours.index.month >= 4) & (daily_total_hours.index.month <= 9)]

# Create the side-by-side histograms
fig, ax = plt.subplots()

bins = np.arange(0, daily_total_hours.max() + 1, 1)

ax.hist([oct_mar, apr_sep], bins=bins, alpha=0.7, label=['October-March', 'April-September'], color=['b', 'g'], align='left')
ax.set_title('Days Worked X-Hours by Season')
ax.set_xlabel('Hours Worked')
ax.set_ylabel('Number of Days')
ax.legend(loc='upper right')

plt.show()

