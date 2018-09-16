
def check_leap(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return 28
    else:
        return 29

def check_first_sun(month, year, j, week_day, start_year):
    day = j+1
    if day == 1 and week_day == "sun" and year > start_year:
        return True
    else:
        return False

def count_first_suns(months, month_days, start_year, end_year, week_days):
    num_week_days = len(week_days)
    num_months = len(months)

    track = 0
    total = 0

    for year in range(start_year, end_year+1):
        month_days[1] = check_leap(year)
        for i in range(num_months):
            month = months[i]
            for j in range(month_days[i]):
                week_day = week_days[track%num_week_days]
                if check_first_sun(month, year, j, week_day, start_year):
                    total += 1
                track += 1
    return total



def main():
    months = ["jan", "feb", "mar", "apr", "may", "june", "jul", "aug", "sep", "oct", "nov", "dec"]
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week_days = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]

    start_year, end_year = 1900, 2000
    
    return count_first_suns(months, month_days, start_year, end_year, week_days)

ans = main()
print "ANSWER: " + str(ans)
