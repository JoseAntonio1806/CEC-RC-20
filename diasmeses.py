def isYearLeap(year):
    if year % 4 == 0  and  (year % 100 != 0  or  year % 400 == 0):
        return 1
    else:
        return 0

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

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
