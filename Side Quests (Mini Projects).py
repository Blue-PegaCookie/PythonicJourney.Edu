from datetime import date

import calendar

name = input("Hey buddy! What's your name? ")
dob = input(f"Hey {name}, What's your date of birth? (DD-MM-YYYY) ")

today = str((date.today()))
current_month = int(today[5:7])
birthday_month = int(dob[-7:-5])

months_lived1 = current_month - birthday_month
months_lived2 = birthday_month - current_month
adv_months_lived = 12 - (int(months_lived2) + 1)

today = str((date.today()))
current_date = int(today[-2:])
birthday_date = int(today[:2])


def calculate_age():
    today = str((date.today()))
    current_year = int(today[0:4])
    years_lived = current_year - int(dob[-4:])

    today = str((date.today()))
    current_month = int(today[5:7])
    birthday_month = int(dob[-7:-5])

    months_lived1 = current_month - birthday_month
    months_lived2 = birthday_month - current_month
    adv_months_lived = 12 - (int(months_lived2) + 1)

    today = str((date.today()))
    current_date = int(today[-2:])
    birthday_date = int(dob[-10:-8])

    if birthday_month < current_month:
        if current_date > birthday_date:
            days_lived = current_date - birthday_date
            print(f"Hey {name} you've lived for {years_lived} years, {months_lived1} months, {days_lived} days! ")
        elif current_date < birthday_date:
            if birthday_month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                days_lived_31 = 31 - int(birthday_date) + int(current_date) - 1
                print(f"Hey {name} you've lived for {years_lived} years, {months_lived1} months, {days_lived_31} days! ")
            elif birthday_month == 4 or 6 or 9 or 11:
                days_lived_30 = 30 - int(birthday_date) + int(current_date) - 1
                print(f"Hey {name} you've lived for {years_lived} years, {months_lived1} months, {days_lived_30} days! ")
            elif birthday_month == 2:
                if calendar.isleap(current_year) is True:
                    days_lived_29 = 29 - int(birthday_date) + int(current_date) - 1
                    print(f"Hey {name} you've lived for {years_lived} years, {months_lived1} months, {days_lived_29} days! ")
                elif calendar.isleap(current_year) is False:
                    days_lived_28 = 28 - int(birthday_date) + int(current_date) - 1
                    print(f"Hey {name} you've lived for {years_lived} years, {months_lived1} months, {days_lived_28} days! ")
    elif birthday_month > current_month:
        print(f"Hey {name}, You've lived {years_lived - 1} years! and {adv_months_lived} months! and {current_date - 1} days! ")
    elif birthday_month == current_month:
        if current_date > birthday_date:
            print(f"Hey {name}, You've lived {years_lived} years! 0 months and {current_date - birthday_date} days! ")
        elif current_date < birthday_date:
            print(f"Hey {name}, You've lived for {years_lived - 1} years!, 11 months and {current_date} days! ")
        elif current_date == birthday_date:
            print(f"Hey {name}, You've lived {years_lived} years! 0 months and 0 days. ")



calculate_age()
