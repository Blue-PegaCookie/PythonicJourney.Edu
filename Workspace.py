from datetime import date

today = str((date.today()))
current_date = int(today[-2:])

print(current_date)