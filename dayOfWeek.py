'''Homework 01 task dayOfWeek* Необходимо написать программу, которая принимая входные
данные день в году и день недели выдает день недели соответсвующий заданому дню в году.'''

day_year = int(input("Please, insert the number of the day in the year: "))
partic_day = int(input("Please, insert the number of the first day of the year: "))
day_week = [0, 1, 2, 3, 4, 5, 6]
z = int(0)
if day_year > len(day_week):
    while day_year > len(day_week):
        day_week.extend(day_week)
while not z == day_year:
    partic_day += 1
    z += 1
print(day_week[partic_day])