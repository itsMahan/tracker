from data_modules import *


menu = '''
1 - Add 
2 - show
3 - Clear 
4 - exit

'''

track_obj = dict()

while True:
    track_obj.clear()
    print(menu)
    user_choice = input('Your choice: ')

    match user_choice.strip():

        case 'Add' | '1':
            print('1 - Counter\n2 - Tracker')
            user_add_choice = input('>>> ')
            match user_add_choice.strip():
                case '1' | 'counter':
                    track_obj['name'] = input('Tracking Object Name: ')
                    track_obj['start_date'] = add_start_date()
                    print('Counter Started...')
                case '2' | 'tracker':
                    track_obj['name'] = input('Tracking Object Name: ')
                    track_obj['start_date'] = add_start_date()
                    track_obj['end_date'] = add_end_date()
                case _:
                    print('Invalid choice')
                    break

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
