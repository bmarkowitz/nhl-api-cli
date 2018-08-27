""" Gets the requested data from the NHL API and returns it in JSON format """

try:
    import requests
except ImportError:
    print("Cannot load module(s)")

s = requests.Session()
BASE_URL = 'https://statsapi.web.nhl.com/api/v1/'
TEAM_ROSTER_URL = 'https://statsapi.web.nhl.com/api/v1/teams/{0}?expand=team.roster'

def get_team(team_id):
    r = s.get(TEAM_ROSTER_URL.format(team_id))
    try:
        status = r.raise_for_status()
        return r.json()
    except HTTPError:
        raise ValueError("Failed to retrieve team data")
