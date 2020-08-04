def GiveWorkingDay(year, month, day):
    #prints the nearest working day
    from datetime import date
    from datetime import timedelta

    #day = date.today()
    day = date(year,month,day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print('working day for',day,'is',workingday)
    return



GiveWorkingDay(year=2020,month=12,day=6)
GiveWorkingDay(day=6,month=12,year=2020)
GiveWorkingDay(2020,3,28)
GiveWorkingDay(2020,5,2)
GiveWorkingDay(2020,6,28)
GiveWorkingDay(2020,7,17)
GiveWorkingDay(2020,8,18)
GiveWorkingDay(2020,9,11)


    
