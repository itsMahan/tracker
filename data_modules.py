from datetime import datetime, timedelta
import csv

file = 'data.csv'

def add_tracker(tracking_obj):
    data_list = []
    with open(file, 'r') as f:
        csvreader = csv.DictReader(f)
        for row in csvreader:
            data_list.append(row)

    data_list.append(tracking_obj)

    with open(file, 'w', newline='') as csvfile:
        fields = ['name', 'type', 'start_date', 'end_date_or_event_amount']
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data_list)


def add_start_date():
    print("when is the starting date? ")
    date_choice =  input("1 - now\n2 - select a specific date\n")

    match date_choice.strip():
        case 'now' | '1':
            start_date_result = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        case 'select' | '2':
            print(f"type a date in this format: YYYY-MM-DD (e.g. Current Date: {datetime.now().strftime('%Y-%m-%d')})")
            while True:
                date_str = input('>>> ')
                try:
                    start_date_result = datetime.strptime(date_str, '%Y-%m-%d')
                except ValueError:
                    print("Wrong input, please try again")
                else:
                    break

        case _:
            print("Invalid choice")
            print("present datetime is selected by default")
            start_date_result = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return start_date_result


def add_end_date():
    print("when is the ending date? ")
    date_choice =  input("1 - specify days from now\n2 - select a specific date\n3 - No ending date\n")

    match date_choice.strip():
        case 'specify' | '1':
            days = int(input('>>> '))
            end_date_result = (datetime.now() + timedelta(days=days)).strftime('%Y-%m-%d %H:%M:%S')

        case 'select' | '2':
            print(f"type a date in this format: YYYY-MM-DD (e.g. Current Date: {datetime.now().strftime('%Y-%m-%d')})")
            while True:
                date_str = input('>>> ')
                try:
                    end_date_result = datetime.strptime(date_str, '%Y-%m-%d')
                except ValueError:
                    print("Wrong input, please try again")
                else:
                    if end_date_result < datetime.now():
                        print("Ending date can't be in the past, please try again")
                        ##TODO handle check end date must be after start date
                    else:
                        break

        case 'No' | '3':
            end_date_result = ''

        case _:
            print("Invalid choice")
            print("present datetime is selected by default")
            result = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return end_date_result


# Function to convert string to datetime
def convert(date_time, frmt):
    # format = '%Y-%m-%d %H:%M:%S.%f'
    datetime_str = datetime.strptime(date_time, frmt)

    return datetime_str


def search_data(name):
    data_list = []
    with open(file, 'r') as f:
        csvreader = csv.DictReader(f)
        for row in csvreader:
            data_list.append(row)
    for data in data_list:
        if data['name'] == name:
            return True
    return False

def event_increment(name):
    data_list = []
    with open(file, 'r') as f:
        csvreader = csv.DictReader(f)
        for row in csvreader:
            data_list.append(row)
    for data in data_list:
        if data['name'] == name:
            data['end_date_or_event_amount'] = int(data['end_date_or_event_amount']) + 1
            break

    with open(file, 'w', newline='') as csvfile:
        fields = ['name', 'type', 'start_date', 'end_date_or_event_amount']
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data_list)


def edit_data(name_to_edit, new_track_obj):
    data_list = []
    with open(file, 'r') as f:
        csvreader = csv.DictReader(f)
        for row in csvreader:
            data_list.append(row)
    for data in data_list:
        if data['name'] == name_to_edit:
            data['name'] = new_track_obj['name']
            data['type'] = new_track_obj['type']
            data['start_date'] = new_track_obj['start_date']
            data['end_date_or_event_amount'] = new_track_obj['end_date_or_event_amount']

    with open(file, 'w', newline='') as csvfile:
        fields = ['name', 'type', 'start_date', 'end_date_or_event_amount']
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data_list)


def delete_data(name_to_delete):
    data_list = []
    with open(file, 'r') as f:
        csvreader = csv.DictReader(f)
        for row in csvreader:
            data_list.append(row)
    for data in data_list:
        if data['name'] == name_to_delete:
            data_list.remove(data)

    with open(file, 'w', newline='') as csvfile:
        fields = ['name', 'type', 'start_date', 'end_date_or_event_amount']
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data_list)


def show_data():
    print("\n=========== Tracking ================")
    data_list = []
    with open(file, 'r') as f:
        csvreader = csv.DictReader(f)
        for row in csvreader:
            data_list.append(row)
    if len(data_list) == 0:
        print("No data")
    else:
        for row in data_list:
            row['start_date'] = convert(row['start_date'], '%Y-%m-%d %H:%M:%S')
            passed_date = datetime.now() - row['start_date']

            if row['type'] == 'tracker':
                if row['end_date_or_event_amount']:
                    row['end_date_or_event_amount'] = convert(row['end_date_or_event_amount'], '%Y-%m-%d %H:%M:%S')
                    end_date = row['end_date_or_event_amount'] - row['start_date']
                    row = f"{row['name']}, {row['type']} \t->\t Started {passed_date.days}d,{passed_date.seconds//3600}h,{(passed_date.seconds//60)%60}m ago \t->\t Ends in {end_date.days} days."
                else:
                    row = f"{row['name']}, {row['type']} \t->\t Started {passed_date.days}d,{passed_date.seconds//3600}h,{(passed_date.seconds//60)%60}m ago."
            elif row['type'] == 'daily':
                row = f"{row['name']}, {row['type']} \t->\t {passed_date.days} days passed."
            else:
                row = f"{row['name']}, {row['type']} \t->\t x{row['end_date_or_event_amount']}"
                # row = f"{row['name']}, {row['type']} \t->\t Started {passed_date.days}d,{passed_date.seconds//3600}h,{(passed_date.seconds//60)%60}m ago."
            print(row)
    print("=====================================")

def clear_data():
    f = open(file, 'w')
    f.close()
    print("Data cleared")