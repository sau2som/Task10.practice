def is_leap(year):
    leap = True
    noleap= False
    if (year%4==0)and (year % 100!=0 or year % 400==0):
        return leap
    else:
        return noleap

year = int(input())
print(is_leap(year))