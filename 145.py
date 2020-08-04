def GiveWorkingDay():
    #prints the nearest working day
    from datetime import date
    from datetime import timedelta

    day = date.today()
    #day = date(2020,3,29)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print('working day for',day,'is',workingday)
    return

GiveWorkingDay()

def DayToNewYear():
    from datetime import date
    from datetime import timedelta

    today = date.today()
    current_year = today.year
    end_year = date(current_year, 12, 31)
    delta = end_year - today
    print(delta.days)
    return

DayToNewYear()

    
