""" Gets the requested data from the NHL API and returns it in JSON format """

try:
    import requests
except ImportError:
    print("Cannot load module(s)")

s = requests.Session()
BASE_URL = 'https://statsapi.web.nhl.com/api/v1/'
TEAM_ROSTER_URL = 'https://statsapi.web.nhl.com/api/v1/teams/{0}?expand=team.roster'
PLAYER_URL = 'https://statsapi.web.nhl.com/api/v1/people/{0}'

def get_team(team_id):
    r = s.get(TEAM_ROSTER_URL.format(team_id))
    try:
        status = r.raise_for_status() # Raise an error if request is unsucessful
        return r.json()
    except HTTPError:
        raise ValueError("Failed to retrieve team data")

def get_player(player_id):
    r = s.get(PLAYER_URL.format(player_id))
    try:
        status = r.raise_for_status() # Raise an error if request is unsucessful
        return r.json()
    except HTTPError:
        raise ValueError("Failed to retrieve player data")


