from data_modules import *


menu = '''
1 - Add 
2 - edit
3 - delete
4 - show
5 - Clear 
6 - exit

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
                    is_found = search_data(track_obj['name'])
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

        case 'edit' | '2':
            name_to_edit = input('Name to edit: ')
            is_found = search_data(name_to_edit)
            if not is_found:
                print('not fount!')
            else:
                new_track_obj = dict()
                new_track_obj['type'] = input('New Tracking Object Type(daily/event/tracker): ')
                match new_track_obj['type']:
                    case 'daily':
                        new_track_obj['name'] = input('New Daily Counter Name: ')
                        new_track_obj['type'] = 'daily'
                        new_track_obj['start_date'] = add_start_date()
                        new_track_obj['end_date_or_event_amount'] = ''
                    case 'event':
                        new_track_obj['name'] = input('New Event Counter Name: ')
                        new_track_obj['type'] = 'event'
                        new_track_obj['start_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        new_track_obj['end_date_or_event_amount'] = '1'
                        print('New Event Counter Started...')
                    case 'tracker':
                        new_track_obj['name'] = input('New Tracking Object Name: ')
                        new_track_obj['type'] = 'tracker'
                        new_track_obj['start_date'] = add_start_date()
                        new_track_obj['end_date_or_event_amount'] = add_end_date()

                print("data successfully updated!")
                edit_data(name_to_edit, new_track_obj)

        case 'delete' | '3':
            name_to_delete = input('Name to delete: ')
            is_found = search_data(name_to_delete)
            if not is_found:
                print('not fount!')
            else:
                print("data successfully deleted!")
                delete_data(name_to_delete)

        case 'show' | '4':
                show_data()

        case 'clear' | '5':
            clear_data()

        case 'exit' | '6':
            print('Bye!')
            exit()

        case _:
            print('Invalid choice')
