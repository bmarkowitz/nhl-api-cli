def display_obj(obj_list):
    if obj_list:
        for obj in obj_list:
            for key in obj:
                print(f'{key}: {obj[key]}')
            print('==================================================')

def display_roster(roster_list):
    for lst in roster_list:
        for obj in lst:
            for key in obj:
                print(f'{key}: {obj[key]}')
            print('=========================')
        if roster_list.index(lst) < len(roster_list) - 1:
            print('==================================================')
        