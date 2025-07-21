from data_modules import *


menu = '''
1 - Add 
2 - show
3 - Clear 
4 - exit

'''

track_obj = dict()

while True:

    print(menu)
    user_choice = input('Your choice: ')

    match user_choice.strip():

        case 'Add' | '1':
            track_obj['name'] = input('Tracking Object Name: ')
            track_obj['start_date'] = add_start_date()
            add_tracker(track_obj)

        case 'show' | '2':
            show_data()

        case 'clear' | '3':
            clear_data()

        case 'exit' | '4':
            print('Bye!')
            exit()

        case _:
            print('Invalid choice')
