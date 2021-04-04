#this program will check the date and
#output whether or not today is a weekday
#Author: Carolyn Moorhouse

import pandas as pd
def is_weekday(date):
    return bool(len(pd.bdate_range(date, date)))
print("Check weekday or not?")
print('2021-04-04:', is_weekday('2021-04-04'))
print('2021-04-05:', is_weekday('2021-04-05'))
print('2021-04-06:', is_weekday('2021-04-06'))