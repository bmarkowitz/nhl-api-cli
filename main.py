""" NHL API wrapper main module """

import nhlinfo.info

def roster(team_id):
    # Get the data
    data = nhlinfo.info.roster(team_id)
    
    return data

