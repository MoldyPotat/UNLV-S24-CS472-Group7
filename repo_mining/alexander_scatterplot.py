import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Reading the CSV file
file_path = 'data/output.csv'  # Replace with the actual file path
df = pd.read_csv(file_path)

# Convert the 'Dates' column to datetime format
df['Dates'] = pd.to_datetime(df['Dates'])

# Create a scatter plot
fig, ax = plt.subplots()

# Loop through unique authors and plot points with different colors
for author, group in df.groupby('Authors'):
    ax.scatter(group['Dates'], group['Filename'], label=author)

# Format the x-axis as dates
ax.xaxis.axis_date()

# Set labels and title
plt.xlabel('Date')
plt.ylabel('Filename')
plt.title('Scatter Plot of Commits By  Over Time')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.show()
