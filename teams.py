import statsapi
import pandas as pd

# Obtain MLB teams
teams = statsapi.get('teams', {'sportIds': 1})

# Format data
teams_data = [
    {
        'ID': team['id'],
        'Name': team['name'],
        'Abreviation': team['abbreviation'],
        'City': team['locationName'],
        'League': team['league']['name'],
        'Division': team['division']['name']
    }
    for team in teams['teams']
]

# Create dataframe
df = pd.DataFrame(teams_data)

# Save CSV
df.to_csv('mlb-teams.csv', index=False)
