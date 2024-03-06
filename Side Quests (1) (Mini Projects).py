from datetime import date

import calendar


def calculate_age():
    name = input("Hey buddy! What's your name? ")
    dob = input(f"Hey {name}, What's your date of birth? (DD-MM-YYYY) ")

    today_x = str((date.today()))
    current_year = int(today_x[0:4])
    years_lived = current_year - int(dob[-4:])

    today_x = str((date.today()))
    current_month_x = int(today_x[5:7])
    birthday_month_x = int(dob[-7:-5])

    months_lived1_x = current_month_x - birthday_month_x
    months_lived2_x = birthday_month_x - current_month_x
    adv_months_lived_x = 12 - (int(months_lived2_x) + 1)

    today_x = str((date.today()))
    current_date_x = int(today_x[-2:])
    birthday_date_x = int(dob[-10:-8])

    while years_lived >= 0:
        if birthday_month_x < current_month_x:
            if current_date_x > birthday_date_x:
                days_lived = current_date_x - birthday_date_x
                print(f"Hey {name} you've lived for {years_lived} years, {months_lived1_x} months, {days_lived} days! ")
            elif current_date_x < birthday_date_x:
                if birthday_month_x == 1 or 3 or 5 or 7 or 8 or 10 or 12:
                    days_lived_31 = 31 - int(birthday_date_x) + int(current_date_x) - 1
                    print(
                        f"Hey {name} you've lived for {years_lived} years, {months_lived1_x} months,"
                        f" {days_lived_31} days! ")
                elif birthday_month_x == 4 or 6 or 9 or 11:
                    days_lived_30 = 30 - int(birthday_date_x) + int(current_date_x) - 1
                    print(
                        f"Hey {name} you've lived for {years_lived} years, {months_lived1_x} months,"
                        f" {days_lived_30} days! ")
                elif birthday_month_x == 2:
                    if calendar.isleap(current_year) is True:
                        days_lived_29 = 29 - int(birthday_date_x) + int(current_date_x) - 1
                        print(
                            f"Hey {name} you've lived for {years_lived} years, {months_lived1_x} months,"
                            f" {days_lived_29} days! ")
                    elif calendar.isleap(current_year) is False:
                        days_lived_28 = 28 - int(birthday_date_x) + int(current_date_x) - 1
                        print(
                            f"Hey {name} you've lived for {years_lived} years, {months_lived1_x} months,"
                            f" {days_lived_28} days! ")
        elif birthday_month_x > current_month_x:
            print(
                f"Hey {name}, You've lived {years_lived - 1} years! and {adv_months_lived_x} months!"
                f" and {current_date_x - 1} days! ")
        elif birthday_month_x == current_month_x:
            if current_date_x > birthday_date_x:
                print(f"Hey {name}, You've lived {years_lived} years! 0 months and "
                      f"{current_date_x - birthday_date_x} days! ")
            elif current_date_x < birthday_date_x:
                print(f"Hey {name}, You've lived for {years_lived - 1} years!, 11 months and {current_date_x - 1} days! ")
            elif current_date_x == birthday_date_x:
                print(f"Hey {name}, You've lived {years_lived} years! 0 months and 0 days. ")
        break

    while years_lived < 0:
        print(f"{name}, You've entered a year where it's still hasn't occurred "
              f"Which means you've entered year in the future. Please try again")
        return


calculate_age()
