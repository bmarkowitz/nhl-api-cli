import requests
import json
from functions.session import s
from functions.data import teams_dict

""" Functions to handle fetching team data """

base_url = 'https://statsapi.web.nhl.com/api/v1/teams/'

def get_teams(id_str):
    id_list = id_str.split(',')
    results_list = []
    for id_ in id_list:
        json_data = json.loads(s.get(base_url + id_).text)
        try:
            results_list.append(json_data['teams'][0])
        except KeyError:
            continue
            
    return results_list
