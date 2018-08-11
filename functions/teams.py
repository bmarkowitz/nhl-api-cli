try:
    import requests
    import json
    from functions.session import s
    from functions.data import teams_dict
except ImportError:
    print('Imports failed')

""" Functions to handle fetching team data """

base_url = 'https://statsapi.web.nhl.com/api/v1/'
linescore_url = 'schedule?expand=schedule.linescore&teamId='

def get_teams(id_str):
    id_list = id_str.split(',')
    results_list = []
    for id_ in id_list:
        json_data = json.loads(s.get(base_url + 'teams/' + id_).text)
        try:
            results_list.append(json_data['teams'][0])
        except KeyError:
            continue
            
    return results_list

def get_prev_game(id_str):
    id_list = id_str.split(',')
    results_list = []
    for id_ in id_list:
        prev_game_data = json.loads(s.get(base_url + 'teams/' + id_ + '?expand=team.schedule.previous').text)
        prev_game_line = base_url + id_ + '&date='
        try:
            games_obj = prev_game_data['teams'][0]['previousGameSchedule']['dates'][0]['games'][0]
            game_date = games_obj['gameDate'][0:10]
            prev_game_line = json.loads(s.get(base_url + linescore_url + id_ + '&date=' + game_date).text)
            result_obj = {
                'teamQueried': f'{id_} ({teams_dict[id_]})',
                'date': game_date,
                'finalPeriod': prev_game_line['dates'][0]['games'][0]['linescore']['currentPeriod'],
                'startTime': games_obj['gameDate'][11:19],
                'location': games_obj['venue']['name'],
                'awayTeam': games_obj['teams']['away']['team']['name'],
                'awayGoals': games_obj['teams']['away']['score'],
                'homeTeam': games_obj['teams']['home']['team']['name'],
                'homeGoals': games_obj['teams']['home']['score'],
            }
            results_list.append(result_obj)
        except KeyError:
            continue
    return results_list

def get_next_game(id_str):
    id_list = id_str.split(',')
    results_list = []
    for id_ in id_list:
        next_game_data = json.loads(s.get(base_url + 'teams/' + id_ + '?expand=team.schedule.next').text)
        try:
            games_obj = next_game_data['teams'][0]['nextGameSchedule']['dates'][0]['games'][0]
            game_date = games_obj['gameDate'][0:10]
            result_obj = {
                'teamQueried': f'{id_} ({teams_dict[id_]})',
                'date': game_date,
                'startTime': games_obj['gameDate'][11:19],
                'location': games_obj['venue']['name'],
                'awayTeam': games_obj['teams']['away']['team']['name'],
                'homeTeam': games_obj['teams']['home']['team']['name'],
            }
            results_list.append(result_obj)
        except KeyError:
            continue
    return results_list

def get_team_roster(id_str):
    id_list = id_str.split(',')
    results_list = []
    for id_ in id_list:
        team_list = []
        team_roster_data = json.loads(s.get(base_url + 'teams/' + id_ + '?expand=team.roster').text)
        try:
            roster = team_roster_data['teams'][0]['roster']['roster']
            for player in roster:
                player_name = player['person']['fullName']
                try:
                    player_num = player['jerseyNumber']
                except KeyError:
                    player_num = '00'
                player_pos = player['position']['code']
                player_obj = {
                    'number': player_num,
                    'fullName':player_name,
                    'position': player_pos
                }
                team_list.append(player_obj)
        except KeyError:
            continue
        results_list.append(team_list)
    return results_list