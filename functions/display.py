def display_obj(obj_list):
    for obj in obj_list:
        for key in obj:
            print(f'{key}: {obj[key]}')
        print('==================================================')
