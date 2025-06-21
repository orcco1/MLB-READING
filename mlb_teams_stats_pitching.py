import statsapi
import pandas as pd

# Configuration
season = 2025
group = 'pitching'
stat_type = 'season'

# Call to endpoint
response = statsapi.get(
    'teams_stats',
    {
        'season': season,
        'group': group,
        'stats': stat_type,
        'sportIds': 1  # MLB only
    }
)

# Format data
teams_stats = []
for team in response['stats'][0]['splits']:
    row = {
        'TeamID': team['team']['id'],
        'TeamName': team['team']['name'],
        'Season': season
    }
    row.update(team['stat'])
    teams_stats.append(row)

# Crete dataframe
df = pd.DataFrame(teams_stats)

# Save CSV
df.to_csv(f'mlb_teams_stats_{season}_{group}.csv', index=False)

print(f"mlb_teams_stats_{season}_{group}.csv saved.")
