def isYearLeap(year):
    if year % 4 == 0  and  (year % 100 != 0  or  year % 400 == 0):
        return True
    else:
        return False

def daysInMonth(year, month):
    if isYearLeap(year)==1:
        Dias = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        print(Dias[month-1])
        return Dias[month -1]
    if isYearLeap(year)==0:
        Dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        print(Dias[month -1])
        return Dias[month-1]
    else:
        return None

def dayOfYear(year, month, day):
    if isYearLeap(year)==1:
        Dias = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        suma=sum(Dias[0:month-1])+day
        return suma
        
    
    if isYearLeap(year)==0:
        Dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        suma=sum(Dias[0:month-1])+day
        return suma

print(dayOfYear(2000, 12, 31))
