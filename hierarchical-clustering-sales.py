import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

# Sample sales data
data = {
    'date': pd.date_range(start='2023-01-01', periods=365, freq='D'),
    'sales': np.random.randint(100, 1000, size=365)
}

df = pd.DataFrame(data)


# Function to perform hierarchical clustering and get seasons
def get_seasonal_clusters(df, n_clusters=5):
    # Ensure the dataframe is sorted by date
    df = df.sort_values(by='date').reset_index(drop=True)

    # Perform hierarchical clustering
    Z = linkage(df['sales'].values.reshape(-1, 1), method='ward')

    # Create clusters
    clusters = fcluster(Z, t=n_clusters, criterion='maxclust')

    # Assign clusters to dataframe
    df['season'] = clusters

    # Calculate the average sales for each season
    season_avg_sales = df.groupby('season')['sales'].mean().to_dict()

    # Get dates for each season
    season_dates = df.groupby('season')['date'].apply(list).to_dict()

    # Combine the results into a dictionary
    result = {season: {'average_sales': season_avg_sales[season], 'dates': season_dates[season]} for season in
              season_avg_sales}

    return result


# Get the seasonal clusters
seasons = get_seasonal_clusters(df, n_clusters=5)

# Print the results
for season, info in seasons.items():
    print(f"Season {season}:")
    print(f"  Average Sales: {info['average_sales']:.2f}")
    print(f"  Dates: {info['dates'][:3]} ... {len(info['dates'])} total dates")
    print()

