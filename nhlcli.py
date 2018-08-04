""" This is the main entry point for the NHL API command line interface. Displays the main menu to allow access to all functionality."""

# Imports
from functions.nhlcli_main import menu

def nhl_cli():
    print('Welcome to the NHL API CLI. \nEnter the number of the option you wish to execute: \n')
    while True:
        menu()
        choice = input(">> ")

        if choice == '1':
            print('You chose option 1.')
        elif choice == '0':
            exit()
        else:
            print('Invalid selection')


nhl_cli()
        
