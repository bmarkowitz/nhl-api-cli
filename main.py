""" NHL API wrapper main module """
try:
    import nhlinfo.info
except ImportError:
    print("Imports failed")

def roster(team_id):
    # Get the data
    data = nhlinfo.info.roster(team_id)

    return data

def player(player_id):
    # Get the data
    data = nhlinfo.info.player(player_id)

    return data

