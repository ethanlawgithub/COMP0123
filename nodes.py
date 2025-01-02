import pandas as pd

# Load the dataset
df = pd.read_csv("transfer-network.csv")

# Strip whitespace from club names, leagues, and nations
df['club_name'] = df['club_name'].str.strip()
df['club_involved_name'] = df['club_involved_name'].str.strip()
df['league_name'] = df['league_name'].str.strip()  # Assuming 'league_name' column exists in the dataset
df['country'] = df['country'].str.strip()  # Assuming 'country' column exists in the dataset

# Get unique clubs from both 'club_name' and 'club_involved_name'
unique_clubs = pd.concat([df['club_name'], df['club_involved_name']]).unique()

# Create a dictionary to store the league_name and country for each unique club
club_info = {}

# Loop through the dataset to assign league_name and country to each club (only from 'club_name')
for club in unique_clubs:
    # Find the first occurrence of the club in the 'club_name' column for league_name and country
    club_data = df[df['club_name'] == club].iloc[0] if club in df['club_name'].values else None
    if club_data is not None:
        # Store the league_name and country of the club
        club_info[club] = {
            'League': club_data['league_name'],
            'Nation': club_data['country']
        }
    else:
        # If the club is not in 'club_name', leave it blank (NaN)
        club_info[club] = {
            'League': None,
            'Nation': None
        }

# Create a DataFrame for nodes (clubs)
nodes = pd.DataFrame({
    'Id': unique_clubs,  # Node ID (club name)
    'Label': unique_clubs,  # Node label (same as Id or a descriptive name)
})

# Add league_name and country columns to the nodes DataFrame (using NaN where necessary)
nodes['League'] = nodes['Id'].map(lambda club: club_info[club]['League'])
nodes['Nation'] = nodes['Id'].map(lambda club: club_info[club]['Nation'])

# Save the nodes DataFrame to a CSV file
nodes.to_csv("nodes.csv", index=False)

# Display the first few rows of the nodes DataFrame
print(nodes.head())
