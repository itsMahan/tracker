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
            print('1 - Daily Counter\n2 - Event Counter\n3 - Tracker')
            user_add_choice = input('>>> ')
            match user_add_choice.strip():
                case '1' | 'daily':
                    track_obj['name'] = input('Daily Counter Name: ')
                    track_obj['type'] = 'daily'
                    track_obj['start_date'] = add_start_date()
                    add_tracker(track_obj)
                    print('Daily Counter Started...')
                case '2' | 'event':
                    track_obj['name'] = input('Event Counter Name: ')
                    track_obj['type'] = 'event'
                    is_found = search_event(track_obj['name'])
                    if is_found:
                        print('Event Found! and Incremented...')
                        event_increment(track_obj['name'])
                    else:
                        track_obj['start_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        track_obj['end_date_or_event_amount'] = '1'
                        add_tracker(track_obj)
                        print('Event Counter Started...')
                case '3' | 'tracker':
                    track_obj['name'] = input('Tracking Object Name: ')
                    track_obj['type'] = 'tracker'
                    track_obj['start_date'] = add_start_date()
                    track_obj['end_date_or_event_amount'] = add_end_date()
                    add_tracker(track_obj)
                case _:
                    print('Invalid choice')
                    break

        case 'show' | '2':
            show_data()

        case 'clear' | '3':
            clear_data()

        case 'exit' | '4':
            print('Bye!')
            exit()

        case _:
            print('Invalid choice')
