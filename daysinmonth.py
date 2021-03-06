def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


def days_in_month(year_num, month_number):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  month_number = month_days[month_number - 1]
  #if leap year index[2] becomes 29 
  if is_leap(year_num):
    month_days[1] = 29
    return month_number
  else:
    return month_number
  

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
