""" Handles parsing/manipulation of the data from the data module """

try:
    import nhlinfo.data
except ImportError:
    print("Imports failed")

def roster(team_id):
    # Get the data
    data = nhlinfo.data.get_team(team_id)

    # Parse the data
    roster = data['teams'][0]['roster']['roster']
    return roster
