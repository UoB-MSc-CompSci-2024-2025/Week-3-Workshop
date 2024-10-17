hourly_wage = float(input("Please enter your hourly wage: "))
hours_worked = float(input("Please enter how many hours you worked: "))
day_of_week = str(input("What day of the week is it? ").lower())

daily_wage = hourly_wage * hours_worked

if day_of_week == "sunday":
    print(daily_wage * 2)
else:
    print(daily_wage)