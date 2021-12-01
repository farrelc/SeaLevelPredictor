import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    X1 = df['Year']
    y1 = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,5))
    plt.scatter(X1,y1)
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(X1,y1)
    X_1 = list(range(X1.min(), 2051))
    y_1= []

    for year in X_1: y_1.append(intercept + slope * year)
        
    plt.plot(X_1, y_1, label = 'Best Fit Line 1', color='red')
    plt.legend()
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    # Create second line of best fit
    X2 = df['Year'][df['Year'] >= 2000 ]
    y2 = df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000 ]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(X2, y2)

    X_2 = list(range(2000, 2051))
    y_2 = []

    for year in X_2: y_2.append(intercept2 + slope2 * year)

    plt.plot(X_2, y_2, label = 'Best Fit Line 2', color='green')
    plt.legend()

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()