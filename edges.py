import pandas as pd

# Load the dataset
df = pd.read_csv("transfer-network.csv")

# Strip whitespace from club names
df['club_name'] = df['club_name'].str.strip()
df['club_involved_name'] = df['club_involved_name'].str.strip()

# Count the number of transfers between each pair of clubs
transfer_counts = df.groupby(['club_name', 'club_involved_name']).size().reset_index(name='Weight')

# Prepare edges CSV
edges = pd.DataFrame({
    'Source': transfer_counts['club_name'],   # Source node
    'Target': transfer_counts['club_involved_name'],  # Target node
    'Weight': transfer_counts['Weight'],     # Edge weight
    'Type': 'Directed'                      # Edge type
})

# Save the edges to a CSV file
edges.to_csv("edges.csv", index=False)

# Display the first few rows of the edges file
print(edges.head())
