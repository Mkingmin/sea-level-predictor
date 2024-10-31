import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='r', s=100)

    # Create first line of best fit
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope = result.slope
    intercept = result.intercept
    x = pd.Series([i for i in range(1880, 2051)])
    y = [slope * xi + intercept for xi in x]
    plt.plot(x, y, color='b')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    result_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    slope_2000 = result_2000.slope
    intercept_2000 = result_2000.intercept
    x_2000 = pd.Series([i for i in range(2000, 2051)])
    y_2000 = [slope_2000 * xi + intercept_2000 for xi in x_2000]
    plt.plot(x_2000, y_2000, color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()