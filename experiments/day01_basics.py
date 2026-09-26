print("HelLo AJ, How are you?")
name = "AJ"
city = "Faridabad"
learning_month = 5
serious = True
personality = 9.9
age = 28
height = 5.7
learning_ai = True
print(name)
print(city)
print(learning_month)
print(serious)
print(personality)
print(age)
print(height)
print(learning_ai)
print(type(name))
print(type(city))
print(type(learning_month))
print(type(serious))
print(type(personality))
print(type(age))
print(type(height))
print(type(learning_ai))
a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
hours = "hours per day"
days = "days per month" 
months = "number of months"
total = "total study hours"
a = 3
b = 30
c = 5
print("hours:", hours, a)
print("days:", days, b)
print("months:", months, c)
print("total:", a*b*c)

hours_per_day = 3
days_per_month = 30
number_of_months = 5
total_study_hours = hours_per_day * days_per_month * number_of_months
print("Total Study Hours", total_study_hours)

print(total_study_hours > 300)
print(total_study_hours < 300)
print(total_study_hours == 450)
print(total_study_hours != 450)
print(total_study_hours >= 300)
print(total_study_hours <= 300)
target_hours = 500
target_reached = total_study_hours >= target_hours
print("Target Reached", target_reached)
if total_study_hours >= 500:
    print("Expert lever target achived")
elif total_study_hours >= 300:
    print("Strong progress")
else:
    print("keep building consistancy")

study_hours = 450
project_completed = 2
consistent = True

if total_study_hours >= 400 and project_completed >= 3 and consistent:
    print("Ready for advance AI")
else:
    print("Keep Building")