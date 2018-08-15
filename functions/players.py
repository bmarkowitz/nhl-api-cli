try:
    import requests
    import json
    from functions.session import s
    from functions.data import teams_dict
except ImportError:
    print('Imports failed')

players_url = 'https://statsapi.web.nhl.com/api/v1/teams?expand=team.roster'

def get_players(name_str):
    try:
        first, last = name_str.split(' ')
        first = first[0].upper() + first[1:]
        last = last[0].upper() + last[1:]
        name_str = first + ' ' + last
    except ValueError:
        name_str = name_str[0].upper() + name_str[1:] # Sets first letter of input to uppercase so only beginning of first or last names are matched
    json_data = json.loads(s.get(players_url).text)
    results_list = []

    for team in json_data['teams']:
        team_id = team['id']
        players = team['roster']['roster']
        for player in players:
            player_name = player['person']['fullName']
            if name_str in player_name:
                try:
                    player_num = player['jerseyNumber']
                except KeyError:
                    player_num = '00'
                player_pos = player['position']['code']

                results_list.append({
                    'name': player_name,
                    'jerseyNumber': player_num,
                    'position': player_pos,
                })
    return results_list