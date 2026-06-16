import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 1. Load your data
df = pd.read_csv('./datasets/commute_home_data.csv')

# 2. Convert 'Time' column to datetime objects
df['Time'] = pd.to_datetime(df['Time'])

# 3. Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['Time'], df['Duration_Minutes'], marker='o', linestyle='-', color='b')

# 4. Format the x-axis to show hourly intervals
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))
plt.gcf().autofmt_xdate() # Rotates dates to prevent overlapping

# 5. Add labels and title
plt.title('Commute Time Throughout the Day')
plt.xlabel('Time of Day')
plt.ylabel('Commute Duration (Minutes)')
plt.grid(True, linestyle='--', alpha=0.7)

# 6. Save and Show
plt.tight_layout()
plt.savefig('./plots/commute_home_plot.png', dpi=300)
print("Plot saved as commute_home_plot.png")