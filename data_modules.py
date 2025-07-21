from datetime import datetime
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
        fields = ['name', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data_list)


def add_date():
    print("when is the starting date? ")
    date_choice =  input("1 - now\n2 - select a specific date\n")

    match date_choice.strip():
        case 'now' | '1':
            result = datetime.now()

        case 'select' | '2':
            print("Not Implemented Yet ...")
            exit()

        case _:
            print("Invalid choice")
            print("present datetime is selected by default")
            result = datetime.now()

    return result


# Function to convert string to datetime
def convert(date_time):
    format = '%Y-%m-%d %H:%M:%S.%f'
    datetime_str = datetime.strptime(date_time, format)

    return datetime_str


def show_data():
    data_list = []
    with open(file, 'r') as f:
        csvreader = csv.DictReader(f)
        for row in csvreader:
            data_list.append(row)
    if len(data_list) == 0:
        print("No data")
    else:
        for row in data_list:
            row['date'] = convert(row['date'])
            passed_date = datetime.now() - row['date']
            # print(f"{row['name']} -> {row['date'].strftime('%H:%M:%S %A, %B %d, %Y')} -> {passed_date.days} days, {passed_date.seconds//3600} hours, {passed_date.seconds//60} minuets ago")
            print(f"{row['name']} \t->\t Started {passed_date.days}d,{passed_date.seconds//3600}h,{passed_date.seconds//60}m ago")

def clear_data():
    f = open(file, 'w')
    f.close()
    print("Data cleared")