import calendar
import random
from datetime import datetime


def generate_day():
    start_year = 1970
    current_year = datetime.now().year
    rand_year = random.randrange(start_year, current_year)
    start_month = 1
    end_month = 12
    rand_month = random.randrange(start_month, end_month)
    start_day = 1
    end_day = calendar.monthrange(rand_year, rand_month)
    rand_day = random.randrange(start_day, end_day[1])
    weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
               'Saturday', 'Sunday']
    weekday_number = calendar.weekday(rand_year, rand_month, rand_day)
    correct_day = weekday[weekday_number]
    return rand_year, rand_month, rand_day, correct_day


def init_date():
    init_year, init_month, init_day, correct_day = generate_day()
    output_string = '%1i %1i %1i' % (init_year, init_month, init_day)
    return output_string, correct_day


def user_input():
    user_day = input('Enter day: ')
    return user_day


def output():
    init_output, correct_output = init_date()
    print(init_output)
    user = user_input()
    actual = correct_output
    if user == actual:
        print('Correct')
    else:
        print('Wrong. Correct answer was', actual)
    end_input = input('Press enter to try again or type exit to quit ')
    if end_input == 'exit':
        print('Adios!')
        exit()
    else:
        output()



output()

#TODO add 'show stats' option