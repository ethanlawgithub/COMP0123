import pandas as pd

# Load edges CSV
edges_df = pd.read_csv("edges.csv")

# Load club-to-league mapping (ensure this CSV has columns: 'Club' and 'League')
club_to_league_df = pd.read_csv("gephinodes.csv")

# Create a dictionary for faster lookup of league by club
club_to_league_map = club_to_league_df.set_index("name")["league"].to_dict()

# Replace Source and Target clubs with their respective leagues
edges_df["Source League"] = edges_df["Source"].map(club_to_league_map).fillna("Other")
edges_df["Target League"] = edges_df["Target"].map(club_to_league_map).fillna("Other")

# Aggregate the weights by league-to-league transfers
league_transfers = edges_df.groupby(["Source League", "Target League"])["Weight"].sum().reset_index()

# Rename columns for clarity
league_transfers.columns = ["Source League", "Target League", "Total Transfers"]

# Save the aggregated results to a new CSV file
league_transfers.to_csv("league_transfers.csv", index=False)

# Display the aggregated league-to-league transfers
print(league_transfers)
