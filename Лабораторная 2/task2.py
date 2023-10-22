money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

total_budget = money_capital + salary
month = 0
while total_budget - spend*(1 + increase) > 0:
    if month == 0:
        total_budget += (salary - spend)
    else:
        spend *= (1 + increase)
        total_budget += (salary - spend)
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
