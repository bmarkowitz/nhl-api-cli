def display_obj(obj_list):
    for obj in obj_list:
        if type(obj) == dict:
            for key in obj:
                print(f'{key}: {obj[key]}')
            print('==================================================')
        else:
            display_obj(obj)
