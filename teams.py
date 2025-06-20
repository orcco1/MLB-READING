### teams.py

import statsapi as mlbstats

print(mlbstats.standings(leagueId="103,104", division="all", include_wildcard=True, season=None, standingsTypes=None, date=None))