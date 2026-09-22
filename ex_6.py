#convert time in seconds to years, months, days, hours, minutes and seconds

#input
time_in_seconds = int(input("Insert the time in seconds: "))


#years
years = time_in_seconds // (60 * 60 * 24 * 30 * 12)
time_without_years = time_in_seconds % (60 * 60 * 24 * 30 * 12)

#months
months = time_without_years // (60 * 60 * 24 * 30)
time_without_months = time_without_years % (60 * 60 * 24 * 30)

#days
days = time_without_months // (60 * 60 * 24)
time_without_days = time_in_seconds % (60 * 60 * 24)

#hours
hours = time_without_days // (60 * 60)
time_without_hours = time_without_days % (60 * 60)

#minutes
minutes = time_without_hours // (60)
time_without_minutes = time_without_hours % (60)

#seconds
seconds = time_without_minutes


#final output
print("It has passed", years, "years,", months, "months,", days, "days,", hours, "hours,", minutes, "minutes and", seconds, "seconds!")