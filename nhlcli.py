""" This is the main entry point for the NHL API command line interface. Displays the main menu to allow access to all functionality."""

# Imports
import requests
import functions.teams as t
from functions.display import display_obj
from functions.menus import menu, teams_menu
from functions.data import teams_dict

def nhl_cli():
    print('Welcome to the NHL API CLI.\n')
    while True:
        menu()
        print('\nEnter the number of the option you wish to execute:')
        choice = input(">> ")

        if choice == '1':
            active = True
            while active:
                teams_menu()
                choice = input(">> ")
                if choice == '1':
                    id_str = input('Enter team IDs separated by commas: ')
                    display_obj(t.get_teams(id_str))
                else:
                    active = False
        elif choice == '0':
            exit()
        else:
            print('Invalid selection')

if __name__ == '__main__':
    nhl_cli()
        
