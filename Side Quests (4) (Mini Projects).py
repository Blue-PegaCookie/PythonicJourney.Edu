# Family Finder

# The below code allows you to find any person if you enter a database

# Enter the database

Families = [Family1, Family2, Family3, Family4, Family5, Family6, Family7, Family8, Family9, Famil10]

Family1 = [f1, m1, s1, d1]

f1 = ('John', "1969-05-31", ("Paris, France"), "male", "Santander")
m1 = ('Olivia', "1989-7-21",  ("Paris, France"), "female", "Barclays")
s1 = ('Liam', )
d1 = ()


Family2 = [f2, m2, s2, d2]

f2
m2
s2
d2


Family3 = [f3, m3, s3_1, s3_2]

f3
m3
s3_1
s3_2


Family4 = [f4, m4, d4_1, d4_2]

f4
m4
dr_1
d4_2


Family5 = [f5, m5, s5]

f5
m5
s5


Family6 = [f6, m6, d6]

f6
m6
d6


Family7 = [f7, m7]

f7
m7


Family8 = [f8, s8, d8]

f8
s8
d8


Family9 = [m9, s9, d9]

m9
s9
d9

Family10 = [f10, sm10, m10, ss10, s10, d10_1, d10_2]

f10
sm10
m10
ss10
s10
d10_1
d10_2

"""

1. 1969-05-31
2. 1977-08-27
3. 1960-04-05
4. 1964-09-19
5. 1973-03-17
6. 1968-06-13
7. 1970-04-05
8. 1967-04-26
9. 1976-04-06
10. 1964-09-10
'John', 'Peter', 'Michael', 'James', 'David', 'Richard', 'William', 'Joseph', 'Thomas', 'Charles'

"""

'''

1. 1989/7/21
2. 1978/7/26
3. 1993/8/20
4. 1989/5/25
5. 1966/12/5
6. 1993/3/31
7. 1989/5/26
8. 1969/2/4
9. 1977/3/30
10. 1992/9/4

'''
# This is where I test codes then I add it to the main lessons!

# Predefined list of female names
female_names = ['Olivia', 'Ava', 'Sophia', 'Charlotte', 'Emma', 'Harper', 'Amelia', 'Evelyn', 'Mia', 'Abigail',
                'Emily', 'Madison', 'Ella', 'Avery', 'Isabella', 'Harper', 'Chloe', 'Lily', 'Aria', 'Grace']

# Predefined list of male names
male_names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'Ethan', 'Mason', 'Logan', 'Alexander', 'James', 'William',
              'Benjamin', 'Lucas', 'Michael', 'Elias', 'Aiden', 'Joseph', 'Matthew', 'David', 'Daniel']

import random
from datetime import datetime, timedelta

def generate_date_of_birth():
    random_year = random.randint(2001, 2020)
    random_month = random.randint(1, 12)
    random_day = random.randint(1, 28)
    return datetime(random_year, random_month, random_day)

def generate_mothers_dates_of_birth():
    mothers_dobs = []
    for _ in range(20):
        mothers_dobs.append(generate_date_of_birth() - timedelta(random.randint(0, 365*20)))
    return mothers_dobs

mothers_dobs = generate_mothers_dates_of_birth()

for i, dob in enumerate(mothers_dobs):
    print(f"{i+1}. {dob.year}/{dob.month}/{dob.day}")