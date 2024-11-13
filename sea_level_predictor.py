import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import the data
df = pd.read_csv("epa-sea-level.csv")

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label="Data", color='blue')

# Line of best fit for the entire dataset
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
x_pred = pd.Series(range(1880, 2051))  # years from 1880 to 2050
y_pred = intercept + slope * x_pred
plt.plot(x_pred, y_pred, color='orange', label="Best Fit Line (1880-2050)")

# Line of best fit for data from 2000 onwards
recent_df = df[df['Year'] >= 2000]
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
    recent_df['Year'], recent_df['CSIRO Adjusted Sea Level']
)
x_pred_recent = pd.Series(range(2000, 2051))  # years from 2000 to 2050
y_pred_recent = intercept_recent + slope_recent * x_pred_recent
plt.plot(x_pred_recent, y_pred_recent, color='green', label="Best Fit Line (2000-2050)")

# Customize plot
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
plt.legend()

# Save plot and display
plt.savefig("sea_level_plot.png")
plt.show()
