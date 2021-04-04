#this program will check the date and
#output whether or not today is a weekday
#Author: Carolyn Moorhouse

import pandas as pd
def check_weekday(date):
    res=len(pd.bdate_range(date, date))

    if res == 0:
        print("This is the weekend :)")
    else:
        print("This is a weekday")

date = "2021-04-04"
check_weekday(date)
date = "2021-04-07"
check_weekday(date)
