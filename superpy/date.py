from maintenance import check_if_date
from datetime import datetime, timedelta, date


# Sets the day in date.txt
def set_date(day=None):

    if day is not None:
        check_if_date(day)
    if day is None:
        day = date.today()
    day = str(day)

    with open('date.txt', 'w') as file:
        file.write(day)


# Get the date from date.txt
def get_date():
    with open('date.txt', 'r') as file:
        return file.read()


# Update the date in date.txt
def advance_date(num):

    if not isinstance(num, int):
        raise TypeError(f"{num} is not a whole number")

    advance = timedelta(days=num)
    current_date = get_date()

    c_date = datetime.strptime(current_date, '%Y-%m-%d')
    new_date = c_date + advance
    new_date = new_date.date()
    new_date = str(new_date)

    with open('date.txt', 'w') as file:
        file.write(new_date)
